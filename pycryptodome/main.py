#!/usr/bin/env python3

"""
Data encryption (pycryptodome, AES256 CFB mode)
Python 3.13+
Date created: October 25th, 2025
Date modified: -
"""

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

from pathlib import Path

file = Path.home() / "Desktop" / "Textdatei.txt"
password = "my_secret_password"

with open(file, "rb") as f:
    data = f.read()

    salt = get_random_bytes(16)
    iv = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    encrypted_data = salt + iv + cipher.encrypt(data)
    enc_file_path = file.with_suffix(file.suffix + ".enc")

with open(enc_file_path, "wb") as f:
    f.write(encrypted_data)
    print(f"File encrypted: {enc_file_path}")
