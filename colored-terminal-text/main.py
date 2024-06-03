#!/usr/bin/env python3

"""
Colored terminal text
using ANSI escape sequence and Colorama
Version: 1.0
Python 3.12+
Date created: Jun2 3rd, 2024
Date modified: -
"""

from colorama import Fore, Back, Style


def print_colored_text_ansi() -> None:
    """Print colored text
    """
    print()
    print(f"\033[91m{"Hello, World"}")  # red
    print(f"\033[92m{"Hello, World"}")  # green
    print(f"\033[93m{"Hello, World"}")  # yellow
    print(f"\033[94m{"Hello, World"}")  # blue
    print(f"\033[95m{"Hello, World"}")  # purple
    print(f"\033[96m{"Hello, World"}")  # light blue

    print()

    # Colored background
    print(f"\033[41m{"red background"}\033[0m")
    print(f"\033[42m{"green background"}\033[0m")
    print(f"\033[43m{"yellow background"}\033[0m")
    print(f"\033[44m{"blue background"}\033[0m")
    print(f"\033[45m{"purple background"}\033[0m")
    print(f"\033[46m{"cyan background"}\033[0m")
    print(f"\033[47m{"white background"}\033[0m")


def print_colored_text_colorama() -> None:
    print()
    print(Fore.RED + 'red text')
    print(Fore.GREEN + 'green text')
    print(Fore.YELLOW + 'yellow text')
    print(Fore.BLUE + 'blue text')
    print(Fore.MAGENTA + 'magenta text')

    print()

    print(Back.RED + 'red background' + Style.RESET_ALL)
    print(Back.GREEN + 'green background' + Style.RESET_ALL)
    print(Back.YELLOW + 'yellow background' + Style.RESET_ALL)
    print(Back.BLUE + 'blue background' + Style.RESET_ALL)
    print(Back.MAGENTA + 'magenta background' + Style.RESET_ALL)


def main() -> None:
    print_colored_text_ansi()
    print_colored_text_colorama()


if __name__ == "__main__":
    main()
