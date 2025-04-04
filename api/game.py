from http.server import BaseHTTPRequestHandler
import json
import random
from typing import Dict, Set
import time

# Game state
games: Dict[str, dict] = {}
connected_players: Dict[str, Set[str]] = {}

# Word list
WORDS = [
    {
        "word": "PYTHON",
        "english": "Python Programming Language",
        "chinese": "Python编程语言",
        "japanese": "Pythonプログラミング言語",
        "korean": "파이썬 프로그래밍 언어",
        "hint": "A popular programming language known for its simple and readable syntax"
    },
    {
        "word": "JAVASCRIPT",
        "english": "JavaScript Programming Language",
        "chinese": "JavaScript编程语言",
        "japanese": "JavaScriptプログラミング言語",
        "korean": "자바스크립트 프로그래밍 언어",
        "hint": "The most commonly used programming language for web development"
    },
    # ... (other words from the existing game)
]

def create_game(game_id: str):
    word_data = random.choice(WORDS)
    games[game_id] = {
        "word": word_data["word"],
        "word_data": word_data,
        "guessed_letters": set(),
        "players": {},
        "game_over": False,
        "winner": None
    }
    connected_players[game_id] = set()

def get_game_state(game_id: str):
    if game_id not in games:
        return None
    
    game = games[game_id]
    return {
        "type": "game_state",
        "word_display": ["_" if letter not in game["guessed_letters"] else letter for letter in game["word"]],
        "players": {
            pid: {
                "name": data["name"],
                "tries": data["tries"],
                "guessed_letters": list(data["guessed_letters"])
            }
            for pid, data in game["players"].items()
        },
        "game_over": game["game_over"],
        "winner": game["winner"]
    }

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/api/game/'):
            game_id = self.path.split('/')[-1]
            
            # Set headers for SSE
            self.send_response(200)
            self.send_header('Content-Type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Connection', 'keep-alive')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            # Send initial game state
            if game_id not in games:
                create_game(game_id)
            
            game_state = get_game_state(game_id)
            self.wfile.write(f"data: {json.dumps(game_state)}\n\n".encode())
            
            # Keep connection alive
            while True:
                time.sleep(1)
                self.wfile.write(f"data: {json.dumps({'type': 'ping'})}\n\n".encode())
                self.wfile.flush()
    
    def do_POST(self):
        if self.path.startswith('/api/game/'):
            game_id = self.path.split('/')[-1]
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode())
            
            if game_id not in games:
                create_game(game_id)
            
            game = games[game_id]
            
            if data["type"] == "join":
                player_id = data["player_id"]
                player_name = data["player_name"]
                
                game["players"][player_id] = {
                    "name": player_name,
                    "tries": 6,
                    "guessed_letters": set()
                }
                connected_players[game_id].add(player_id)
            
            elif data["type"] == "guess":
                player_id = data["player_id"]
                letter = data["letter"].upper()
                
                if player_id in game["players"] and letter not in game["guessed_letters"]:
                    game["guessed_letters"].add(letter)
                    player = game["players"][player_id]
                    player["guessed_letters"].add(letter)
                    
                    if letter not in game["word"]:
                        player["tries"] -= 1
                        
                        if player["tries"] == 0:
                            game["game_over"] = True
                            game["winner"] = None
                    
                    if all(letter in game["guessed_letters"] for letter in game["word"]):
                        game["game_over"] = True
                        game["winner"] = player_id
            
            elif data["type"] == "hint":
                player_id = data["player_id"]
                if player_id in game["players"]:
                    return {
                        "type": "hint",
                        "translation": game["word_data"]["english"],
                        "hint": game["word_data"]["hint"]
                    }
            
            # Send response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(get_game_state(game_id)).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers() 