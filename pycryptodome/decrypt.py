#!/usr/bin/env python3

"""
Data decryption (pycryptodome, AES256 CFB mode)
Python 3.13+
Date created: October 27th, 2025
Date modified: -
"""

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

from pathlib import Path

file = Path.home() / "Desktop" / "Textdatei.txt.enc"
password = "my_secret_password"

with open(file, "rb") as f:
    encrypted_data = f.read()

    retrieved_salt = encrypted_data[:16]
    retrieved_iv = encrypted_data[16:32]
    retrieved_ciphertext = encrypted_data[32:]

    key = PBKDF2(password, retrieved_salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_CFB, iv=retrieved_iv)
    decrypted_data = cipher.decrypt(retrieved_ciphertext)

    # Remove the `.enc` extension to get the original filename
    dec_file_path = file.with_suffix("")

with open(dec_file_path, "wb") as f:
    f.write(decrypted_data)
    print(f"File decrypted: {dec_file_path}")
