#!/usr/bin/env python3


"""
Small Python Projects for Beginners
Main menu example

Version: 1.0
Python 3.12+
Date created: February 29th, 2024
Date modified: -
"""

import sys


def quit_application():
    sys.exit("Goodbye!")


def main():
    print()
    print("----------------------------------------------------------")
    print("Choose an option:")
    print()
    print("Start simulation: -1-")
    print("Do something else: -2-")
    # More code goes here ...
    print("Exit program: -6-")
    print("----------------------------------------------------------")

    while True:
        choice = input("Your choice: ")

        if choice == "1":
            pass
            break
        elif choice == "2":
            pass
            break
        elif choice == "3":
            pass
            break
        elif choice == "4":
            pass
            break
        elif choice == "5":
            pass
            break
        elif choice == "6":
            quit_application()
        else:
            print("Unknown input! Try again.")
            continue


if __name__ == "__main__":
    main()
