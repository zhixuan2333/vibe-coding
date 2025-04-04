import asyncio
import websockets
import json
import random
from typing import Dict, Set

# Game state
games: Dict[str, dict] = {}
connected_players: Dict[str, Set[str]] = {}

# Word list from the existing game
WORDS = [
    {
        "word": "PYTHON",
        "english": "Python Programming Language",
        "chinese": "Python编程语言",
        "japanese": "Pythonプログラミング言語",
        "korean": "파이썬 프로그래밍 언어",
        "hint": "A popular programming language known for its simple and readable syntax"
    },
    # ... (other words from the existing game)
]

async def create_game(game_id: str):
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

async def handle_player(websocket, path):
    game_id = path.split('/')[-1]
    player_id = None
    
    try:
        # Handle initial connection
        async for message in websocket:
            data = json.loads(message)
            
            if data["type"] == "join":
                player_id = data["player_id"]
                player_name = data["player_name"]
                
                if game_id not in games:
                    await create_game(game_id)
                
                games[game_id]["players"][player_id] = {
                    "name": player_name,
                    "tries": 6,
                    "guessed_letters": set()
                }
                connected_players[game_id].add(player_id)
                
                # Notify all players about the new player
                await broadcast_game_state(game_id)
            
            elif data["type"] == "guess":
                if game_id in games and player_id in games[game_id]["players"]:
                    letter = data["letter"].upper()
                    game = games[game_id]
                    
                    if letter not in game["guessed_letters"]:
                        game["guessed_letters"].add(letter)
                        player = game["players"][player_id]
                        player["guessed_letters"].add(letter)
                        
                        if letter not in game["word"]:
                            player["tries"] -= 1
                            
                            if player["tries"] == 0:
                                game["game_over"] = True
                                game["winner"] = None
                        
                        # Check if word is complete
                        if all(letter in game["guessed_letters"] for letter in game["word"]):
                            game["game_over"] = True
                            game["winner"] = player_id
                        
                        await broadcast_game_state(game_id)
            
            elif data["type"] == "hint":
                if game_id in games and player_id in games[game_id]["players"]:
                    game = games[game_id]
                    await websocket.send(json.dumps({
                        "type": "hint",
                        "translation": game["word_data"]["english"],
                        "hint": game["word_data"]["hint"]
                    }))
    
    except websockets.exceptions.ConnectionClosed:
        pass
    
    finally:
        if game_id in games and player_id:
            if player_id in games[game_id]["players"]:
                del games[game_id]["players"][player_id]
            if player_id in connected_players[game_id]:
                connected_players[game_id].remove(player_id)
            
            # Clean up empty games
            if not games[game_id]["players"]:
                del games[game_id]
                del connected_players[game_id]
            else:
                await broadcast_game_state(game_id)

async def broadcast_game_state(game_id: str):
    if game_id not in games:
        return
    
    game = games[game_id]
    game_state = {
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
    
    message = json.dumps(game_state)
    for player_id in connected_players[game_id]:
        # Find the websocket for this player and send the message
        # This would require maintaining a mapping of player_id to websocket
        pass

async def main():
    async with websockets.serve(handle_player, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main()) 