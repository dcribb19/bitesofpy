import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from dataclasses import dataclass
from os import urandom
from typing import ByteString


@dataclass
class ClamyFernet:
    """Fernet implementation by clamytoe

    Takes a bytestring as a password and derives a Fernet
    key from it. If a key is provided, that key will be used.

    :param password: ByteString of the password to use
    :param key: ByteString of the key to use, else defaults to None

    Other class variables that you should implement that are hard set:

    salt, algorithm, length, iterations, backend, and generate a base64
    urlsafe_b64encoded key using self.clf().
    """
    password: ByteString = b"pybites"
    key: ByteString = None
    algorithm = hashes.SHA256()
    length: int = 32
    salt: str = urandom(16)
    iterations: int = 100000
    backend = default_backend()

    def __post_init__(self):
        if not self.key:
            self.key = base64.urlsafe_b64encode(self.kdf.derive(self.password))

    @property
    def kdf(self):
        """Derives the key from the password

        Uses PBKDF2HMAC to generate a secure key. This is where you will
        use the salt, algorithm, length, iterations, and backend variables.
        """
        kdf = PBKDF2HMAC(
                algorithm=self.algorithm,
                length=self.length,
                salt=self.salt,
                iterations=self.iterations,
                backend=self.backend
            )
        return kdf

    @property
    def clf(self):
        """Generates a Fernet object

        Key that is derived from cryptogrophy's fermet.
        """
        return Fernet(self.key)

    def encrypt(self, message: str) -> ByteString:
        """Encrypts the message passed to it"""
        return self.clf.encrypt(message.encode('utf-8'))

    def decrypt(self, token: ByteString) -> str:
        """Decrypts the encrypted message passed to it"""
        return self.clf.decrypt(token).decode()
