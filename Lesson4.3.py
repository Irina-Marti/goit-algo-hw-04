import sys
from pathlib import Path
from colorama import Fore, Back, Style


def directory_structure(path:Path):
    if not path.exists():
        print(Fore.RED + f"The path {path} does not exist.")
        return
    if not path.is_dir():
        print(Fore.RED + f"{path} is not a directory.")
        return

    for item in path.iterdir():
        if item.is_dir():
            print(Fore.GREEN + f"{item.name}")
            directory_structure(item)
        else:
            print(Fore.BLUE + item.name)


def main():
    if len(sys.argv) < 2:
        print(Fore.BLACK + "Please provide a path to a directory")

    directory_path = Path(sys.argv[1])
    directory_structure(directory_path)

if __name__ == "__main__":
    main()