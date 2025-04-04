import random
from colorama import init, Fore, Style
import time

# Initialize colorama
init()

# List of fun words to guess with Chinese translations and hints
WORDS = [
    {
        "word": "PYTHON",
        "chinese": "Python编程语言",
        "hint": "一种流行的编程语言，以其简单易读的语法著称"
    },
    {
        "word": "JAVASCRIPT",
        "chinese": "JavaScript编程语言",
        "hint": "网页开发中最常用的编程语言，可以制作交互式网站"
    },
    {
        "word": "PROGRAMMING",
        "chinese": "编程",
        "hint": "编写计算机程序的过程"
    },
    {
        "word": "COMPUTER",
        "chinese": "计算机",
        "hint": "用于处理和存储数据的电子设备"
    },
    {
        "word": "ALGORITHM",
        "chinese": "算法",
        "hint": "解决问题的一系列步骤或指令"
    },
    {
        "word": "DATABASE",
        "chinese": "数据库",
        "hint": "存储和组织数据的系统"
    },
    {
        "word": "NETWORK",
        "chinese": "网络",
        "hint": "连接计算机和其他设备的系统"
    },
    {
        "word": "INTERNET",
        "chinese": "互联网",
        "hint": "全球性的计算机网络系统"
    },
    {
        "word": "KEYBOARD",
        "chinese": "键盘",
        "hint": "用于输入文字和命令的输入设备"
    },
    {
        "word": "MONITOR",
        "chinese": "显示器",
        "hint": "显示计算机输出的屏幕设备"
    },
    {
        "word": "DEVELOPER",
        "chinese": "开发者",
        "hint": "创建和维护软件的人"
    },
    {
        "word": "CODING",
        "chinese": "编码",
        "hint": "编写计算机程序的过程"
    },
    {
        "word": "HACKER",
        "chinese": "黑客",
        "hint": "精通计算机系统的人，可以是安全专家"
    },
    {
        "word": "GAMING",
        "chinese": "游戏",
        "hint": "玩电子游戏的活动"
    }
]

def print_hangman(tries):
    stages = [
        f"""
           {Fore.RED}💀{Style.RESET_ALL}
          /|\\
         / | \\
        /  |  \\
           |
           |
          / \\
         /   \\
        """,
        f"""
           {Fore.YELLOW}😱{Style.RESET_ALL}
          /|\\
         / | \\
        /  |  \\
           |
           |
          / \\
         /   
        """,
        f"""
           {Fore.YELLOW}😨{Style.RESET_ALL}
          /|\\
         / | \\
        /  |  \\
           |
           |
          / 
         /   
        """,
        f"""
           {Fore.YELLOW}😰{Style.RESET_ALL}
          /|\\
         / | \\
        /  |  \\
           |
           |
          
          /   
        """,
        f"""
           {Fore.YELLOW}😅{Style.RESET_ALL}
          /|\\
         / | \\
        /  |  \\
           |
           |
          
          
        """,
        f"""
           {Fore.YELLOW}😊{Style.RESET_ALL}
          /|\\
         / | \\
        /  |  \\
           |
           
          
          
        """,
        f"""
           {Fore.GREEN}😎{Style.RESET_ALL}
          /|\\
         / | \\
        /  |  
           |
           
          
          
        """
    ]
    return stages[tries]

def play_game():
    word_data = random.choice(WORDS)
    word = word_data["word"]
    word_letters = set(word)
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters = set()
    tries = 6
    hint_used = False

    print(f"\n{Fore.CYAN}欢迎来到单词猜猜猜游戏！{Style.RESET_ALL}")
    print("我正在想一个单词... 你能猜出来吗？")
    time.sleep(1)
    print("加载中", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

    while len(word_letters) > 0 and tries > 0:
        print(f"\n{Fore.CYAN}你还有 {tries} 次机会{Style.RESET_ALL}")
        print(f"已使用的字母: {Fore.YELLOW}{' '.join(sorted(used_letters))}{Style.RESET_ALL}")

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(f"单词: {Fore.GREEN}{' '.join(word_list)}{Style.RESET_ALL}")
        print(print_hangman(tries))

        if not hint_used:
            print(f"{Fore.MAGENTA}提示: 输入 'hint' 获取提示{Style.RESET_ALL}")
        
        user_input = input(f"{Fore.CYAN}猜一个字母: {Style.RESET_ALL}").upper()

        if user_input == 'HINT' and not hint_used:
            print(f"\n{Fore.MAGENTA}中文翻译: {word_data['chinese']}{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}提示: {word_data['hint']}{Style.RESET_ALL}")
            hint_used = True
            continue

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
                print(f"{Fore.GREEN}正确！{Style.RESET_ALL}")
            else:
                tries -= 1
                print(f"{Fore.RED}错误！这个字母不在单词中。{Style.RESET_ALL}")
        elif user_input in used_letters:
            print(f"{Fore.YELLOW}你已经用过这个字母了。再试一次！{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}无效的字符。请输入一个字母。{Style.RESET_ALL}")

    if tries == 0:
        print(print_hangman(0))
        print(f"{Fore.RED}抱歉，你的机会用完了。这个单词是 {word}！{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}中文翻译: {word_data['chinese']}{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}恭喜！你猜对了单词 {word}！{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}中文翻译: {word_data['chinese']}{Style.RESET_ALL}")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input(f"\n{Fore.CYAN}要再玩一次吗？(y/n): {Style.RESET_ALL}").lower()
        if play_again != 'y':
            print(f"{Fore.GREEN}谢谢参与！再见！{Style.RESET_ALL}")
            break