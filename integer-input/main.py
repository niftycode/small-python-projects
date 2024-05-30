#!/usr/bin/env python3

"""
Description goes here...
Version: 1.0
Python 3.12+
Date created: May 30th, 2024
Date modified: -
"""

import logging
from get_integer import get_integer

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def main() -> None:
    print(
        get_integer(
            prompt="Please enter an integer: ", error_message="n must be an integer"
        )
    )


if __name__ == "__main__":
    main()
