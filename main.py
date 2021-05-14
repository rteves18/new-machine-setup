import os
from shutil import copyfile


def copy_to_main_dir(file_path, file_transfer):
    if not os.path.isfile(file_path):
        copyfile(file_transfer, file_path)


def main():
    vim_color_file = "atom-dark-256.vim"
    vim_color_path = "~/.vim/colors/"
    vim_rc = "~/.vimrc"

    # Copy vim color
    if not os.path.isdir(vim_color_path):
        os.mkdir(vim_color_path)
    if not os.path.isfile(f"{vim_color_path}{vim_color_file}"):
        copyfile(vim_color_file, f"{vim_color_path}{vim_color_file}")
    # Copy vim rc
    if not os.path.isfile(vim_rc):
        copyfile(".vimrc", vim_rc)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
