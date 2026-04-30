#!/usr/bin/env python3

"""
This script interacts with the Ollama API to generate text based on a given prompt.
The output will be printed to the console and saved to a Markdown file named `generated_output.md`.
Version: 1.1
Python 3.13+
Date created: April 30th, 2026
Date modified: -
"""

import json
import sys

import requests  # type: ignore
from requests.exceptions import RequestException  # type: ignore

# Endpoint of Ollama API
URL = "http://localhost:11434/api/generate"

data = {
    "model": "qwen2.5-coder",
    "prompt": "Write a Python class called `Cameras` with the field `manufacturer`.",
    "max_tokens": 1000,
    "temperature": 0.6,
    "top_p": 0.9,
    "n": 1,
    "stream": False,
}


def fetch_generated_text() -> str:
    """
    Fetch generated text from the Ollama API.
    """

    generated_text = ""

    try:
        # Make a POST request to the Ollama API
        response: requests.Response = requests.post(URL, json=data, stream=True)
    except RequestException as e:
        print(f"Error message:\n{e}")
        sys.exit("No connection to Ollama API. Exit program!")

    for line in response.iter_lines():
        if line:
            decoded_line = line.decode("utf-8")
            result = json.loads(decoded_line)
            # Get the generated text from the response
            generated_text = result.get("response", "")

    return generated_text


def main() -> None:
    """Main function to execute the script."""

    answer: str = fetch_generated_text()

    print(answer, end="", flush=True)

    # Save the generated text to a Markdown file
    with open("generated_output.md", "a", encoding="utf-8") as md_file:
        md_file.write(answer)


if __name__ == "__main__":
    main()
