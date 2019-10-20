#!/usr/bin/python3

import argparse
import base64
from cryptography import fernet
from cryptography.hazmat import backends
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf import pbkdf2
import getpass
import secrets
import sys


def _derive_key(password: bytes) -> bytes:
    kdf = pbkdf2.PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=b'',
        iterations=pow(10, 7), backend=backends.default_backend())
    return base64.urlsafe_b64encode(kdf.derive(password))


def password_encrypt(message: bytes, password: str) -> bytes:
    key = _derive_key(password.encode())
    return fernet.Fernet(key).encrypt(message)


if __name__ == '__main__':
    message = sys.stdin.read()
    password = getpass.getpass()
    ciphertext = password_encrypt(message.encode(), password)
    print(ciphertext.decode())
