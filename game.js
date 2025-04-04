// Game data with translations in multiple languages
const WORDS = [
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
    {
        "word": "PROGRAMMING",
        "english": "Programming",
        "chinese": "编程",
        "japanese": "プログラミング",
        "korean": "프로그래밍",
        "hint": "The process of creating computer programs"
    },
    {
        "word": "COMPUTER",
        "english": "Computer",
        "chinese": "计算机",
        "japanese": "コンピュータ",
        "korean": "컴퓨터",
        "hint": "An electronic device for processing and storing data"
    },
    {
        "word": "ALGORITHM",
        "english": "Algorithm",
        "chinese": "算法",
        "japanese": "アルゴリズム",
        "korean": "알고리즘",
        "hint": "A step-by-step procedure for solving a problem"
    },
    {
        "word": "DATABASE",
        "english": "Database",
        "chinese": "数据库",
        "japanese": "データベース",
        "korean": "데이터베이스",
        "hint": "A system for storing and organizing data"
    },
    {
        "word": "NETWORK",
        "english": "Network",
        "chinese": "网络",
        "japanese": "ネットワーク",
        "korean": "네트워크",
        "hint": "A system that connects computers and other devices"
    },
    {
        "word": "INTERNET",
        "english": "Internet",
        "chinese": "互联网",
        "japanese": "インターネット",
        "korean": "인터넷",
        "hint": "A global system of interconnected computer networks"
    },
    {
        "word": "KEYBOARD",
        "english": "Keyboard",
        "chinese": "键盘",
        "japanese": "キーボード",
        "korean": "키보드",
        "hint": "An input device for typing text and commands"
    },
    {
        "word": "MONITOR",
        "english": "Monitor",
        "chinese": "显示器",
        "japanese": "モニター",
        "korean": "모니터",
        "hint": "A display device for computer output"
    },
    {
        "word": "DEVELOPER",
        "english": "Developer",
        "chinese": "开发者",
        "japanese": "開発者",
        "korean": "개발자",
        "hint": "A person who creates and maintains software"
    },
    {
        "word": "CODING",
        "english": "Coding",
        "chinese": "编码",
        "japanese": "コーディング",
        "korean": "코딩",
        "hint": "The process of writing computer programs"
    },
    {
        "word": "HACKER",
        "english": "Hacker",
        "chinese": "黑客",
        "japanese": "ハッカー",
        "korean": "해커",
        "hint": "A person skilled in computer systems, can be a security expert"
    },
    {
        "word": "GAMING",
        "english": "Gaming",
        "chinese": "游戏",
        "japanese": "ゲーミング",
        "korean": "게이밍",
        "hint": "The activity of playing electronic games"
    }
];

// UI text translations
const UI_TEXT = {
    english: {
        title: "Word Guessing Game",
        usedLetters: "Used Letters:",
        keyboard: "Keyboard:",
        hint: "Get Hint",
        newGame: "New Game",
        triesLeft: "Tries Left:",
        win: "Congratulations! You won!\nWord was:",
        lose: "Game Over!\nWord was:",
        hintUsed: "Hint already used",
        letterUsed: "This letter has already been used",
        translation: "Translation:"
    },
    chinese: {
        title: "单词猜猜猜游戏",
        usedLetters: "已使用的字母:",
        keyboard: "键盘:",
        hint: "获取提示",
        newGame: "新游戏",
        triesLeft: "剩余次数:",
        win: "恭喜！你赢了！\n单词是:",
        lose: "游戏结束！\n单词是:",
        hintUsed: "提示已使用",
        letterUsed: "这个字母已经用过了",
        translation: "中文翻译:"
    },
    japanese: {
        title: "単語当てゲーム",
        usedLetters: "使用済みの文字:",
        keyboard: "キーボード:",
        hint: "ヒントを取得",
        newGame: "新しいゲーム",
        triesLeft: "残り回数:",
        win: "おめでとう！勝ちました！\n単語は:",
        lose: "ゲームオーバー！\n単語は:",
        hintUsed: "ヒントは既に使用されています",
        letterUsed: "この文字は既に使用されています",
        translation: "日本語訳:"
    },
    korean: {
        title: "단어 맞추기 게임",
        usedLetters: "사용된 글자:",
        keyboard: "키보드:",
        hint: "힌트 얻기",
        newGame: "새 게임",
        triesLeft: "남은 횟수:",
        win: "축하합니다! 승리했습니다!\n단어는:",
        lose: "게임 오버!\n단어는:",
        hintUsed: "힌트가 이미 사용되었습니다",
        letterUsed: "이 글자는 이미 사용되었습니다",
        translation: "한국어 번역:"
    }
};

let currentWord = null;
let guessedLetters = new Set();
let triesLeft = 6;
let gameOver = false;
let currentLanguage = 'english';
let hintUsed = false;

function generateId() {
    return Math.random().toString(36).substr(2, 9);
}

function getRandomWord() {
    return WORDS[Math.floor(Math.random() * WORDS.length)];
}

function updateGameState() {
    // Update word display
    const wordDisplay = document.getElementById("word-display");
    wordDisplay.innerHTML = currentWord.word.split("").map(letter => 
        `<div class="letter-box">${guessedLetters.has(letter) ? letter : '_'}</div>`
    ).join("");

    // Update tries left
    document.getElementById("tries").textContent = `${UI_TEXT[currentLanguage].triesLeft} ${triesLeft}`;

    // Update used letters
    const usedLettersDiv = document.getElementById("used-letters");
    usedLettersDiv.innerHTML = Array.from(guessedLetters).sort().map(letter =>
        `<span class="px-2 py-1 bg-gray-200 rounded">${letter}</span>`
    ).join("");

    // Update keyboard
    const keyboard = document.getElementById("keyboard");
    keyboard.innerHTML = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("").map(letter =>
        `<button class="keyboard-key px-2 py-1 bg-indigo-100 rounded ${
            guessedLetters.has(letter) ? 'used' : ''
        }" ${guessedLetters.has(letter) ? 'disabled' : ''}>${letter}</button>`
    ).join("");

    // Add keyboard event listeners
    keyboard.querySelectorAll("button").forEach(button => {
        button.onclick = () => {
            if (!button.disabled && !gameOver) {
                const letter = button.textContent;
                makeGuess(letter);
            }
        };
    });

    // Check win condition
    if (currentWord.word.split("").every(letter => guessedLetters.has(letter))) {
        gameOver = true;
        alert(`${UI_TEXT[currentLanguage].win} ${currentWord.word}`);
    }
}

function makeGuess(letter) {
    if (guessedLetters.has(letter)) {
        alert(UI_TEXT[currentLanguage].letterUsed);
        return;
    }

    guessedLetters.add(letter);
    
    if (!currentWord.word.includes(letter)) {
        triesLeft--;
        if (triesLeft === 0) {
            gameOver = true;
            alert(`${UI_TEXT[currentLanguage].lose} ${currentWord.word}`);
        }
    }

    updateGameState();
}

function showHint() {
    if (hintUsed) {
        alert(UI_TEXT[currentLanguage].hintUsed);
        return;
    }

    const hintContent = document.getElementById("hint-content");
    const translationEl = document.getElementById("translation");
    const hintTextEl = document.getElementById("hint-text");
    
    translationEl.textContent = `${UI_TEXT[currentLanguage].translation} ${currentWord[currentLanguage]}`;
    hintTextEl.textContent = currentWord.hint;
    hintContent.classList.remove("hidden");
    hintUsed = true;
}

function startNewGame() {
    currentWord = getRandomWord();
    guessedLetters.clear();
    triesLeft = 6;
    gameOver = false;
    hintUsed = false;
    document.getElementById("hint-content").classList.add("hidden");
    updateGameState();
}

// Initialize the game when the page loads
document.addEventListener('DOMContentLoaded', () => {
    // Set up language selector
    document.querySelectorAll('.language-selector').forEach(selector => {
        selector.addEventListener('click', () => {
            document.querySelectorAll('.language-selector').forEach(s => s.classList.remove('active'));
            selector.classList.add('active');
            currentLanguage = selector.dataset.lang;
            updateUIText();
        });
    });

    // Set up hint button
    document.getElementById('hint-btn').addEventListener('click', showHint);

    // Set up new game button
    document.getElementById('new-game-btn').addEventListener('click', startNewGame);

    // Start the first game
    startNewGame();
});

function updateUIText() {
    document.querySelector('h1').textContent = UI_TEXT[currentLanguage].title;
    document.getElementById('used-letters-title').textContent = UI_TEXT[currentLanguage].usedLetters;
    document.getElementById('keyboard-title').textContent = UI_TEXT[currentLanguage].keyboard;
    document.getElementById('hint-btn').textContent = UI_TEXT[currentLanguage].hint;
    document.getElementById('new-game-btn').textContent = UI_TEXT[currentLanguage].newGame;
} 