import os
import re
import sys


def handle_latex_code(filename: str, print_content=False) -> int:
    word_count = 0
    latex_free_code = ''
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for elem in words:
                elem = remove_code_fragments(elem)
                if elem not in ['\\\\', '\\']:
                    word_count += 1
                latex_free_code += elem + ' '
            # print("current wc: ", word_count, latex_free_code)

    if print_content:
        for elem in latex_free_code:
            print(elem, end='')
            if elem == '.':
                print()
        print();
        print()

    # print(f"{Fore.YELLOW}The word count for this section is {word_count}")
    print(f"The word count for this section is {word_count}")
    return word_count


def ask_for_file_name() -> str:
    for i in range(3):
        if i == 0:
            file_name = input(
                'Welcome to this little script. It calculates and displays the words count given a LaTeX code.\n'
                'For this, the file must be on your Desktop.\n'
                'Enter name of dummy file:\n'
            )
        else:
            file_name = input(
                '\n'
                'File could not be found.\n'
                'Please enter file name again:\n'
            )

        # check whether file exists => if so, stop loop
        if os.path.isfile(file_name):
            return file_name

    print('\n'
          'FILE COULD NOT BE FOUND.\n'
          'Please ensure that you have the correct file name.'
          )
    sys.exit(1)


def remove_code_fragments(elem: str) -> str:
    elem = re.sub('\\\\[\\w]+{', '', elem)
    elem = elem.strip('}')
    elem = elem.strip('\\')
    return elem
