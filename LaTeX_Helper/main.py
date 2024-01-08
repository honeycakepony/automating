import os
from pathlib import Path

from internal_logic.functions import handle_latex_code, ask_for_file_name

# from colorama import init as colorama_init
# from colorama import Fore


HOME_DIRECTORY = os.path.join(Path.home(), 'Desktop')
POSITIVE_ANSWER = ['true', 'yes', 'y', 'ja', 'j']

if __name__ == '__main__':
    os.chdir(HOME_DIRECTORY)

    # user interaction:
    #   1. provide file name
    #   2. ask for print option
    file_name = ask_for_file_name()
    user_input = input("Do you want the plaintext printed?\n")
    print_content = True if (user_input.lower() in POSITIVE_ANSWER) else False
    handle_latex_code(file_name, print_content)
