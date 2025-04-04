# Word Guessing Game

A fun web-based word guessing game with colorful interface, emoji hangman, and multilingual support!

## Features

- Modern, responsive web interface
- Colorful UI with animations
- Emoji-based hangman display
- Word list focused on tech-related terms
- Multilingual support (Chinese and Japanese)
- Helpful hints for each word
- Multiple attempts to guess the word
- Play again option
- On-screen keyboard
- Visual feedback for guesses
- Language switching between Chinese and Japanese

## Deployment

This game is designed to be deployed on Vercel. To deploy:

1. Fork this repository
2. Sign up for a [Vercel account](https://vercel.com/signup) if you don't have one
3. Connect your GitHub account to Vercel
4. Import this repository in Vercel
5. Deploy!

Or use the Vercel CLI:
```bash
npm install -g vercel
vercel
```

## Local Development

You can also run the game locally without any server:

1. Simply open the `index.html` file in your browser
2. Or use a simple HTTP server:
```bash
npx serve
```

## How to Play

1. The game will display a word with underscores for each letter
2. Click on the on-screen keyboard to guess letters
3. You have 6 tries to guess the word
4. Click "获取提示" or "ヒントを取得" to get the translation and a helpful hint
5. The hangman will be drawn progressively as you make wrong guesses
6. Try to guess the word before the hangman is complete!
7. Click "新游戏" or "新しいゲーム" to start a new game
8. Switch between Chinese and Japanese using the language selector at the top

## Game Rules

- You can only guess one letter at a time
- You have 6 tries to guess the word
- The game will show you which letters you've already guessed
- You can get one hint per game (shows translation and description)
- The word is always related to technology or programming
- You can play multiple rounds
- You can switch languages at any time

Have fun playing! 🎮