from src.ez2bruteforce.problem import Problem, BfItem
from src.ez2bruteforce.solver import *
import hashlib
import string


def test_sha1():
    plaintext = b"Dear lihua"
    cipher = hashlib.sha1(plaintext).digest()
    problem = Problem(
        ["Dear ", BfItem(length=5, char_table=string.ascii_lowercase)])
    assert sha1_solver(problem, cipher) == plaintext


def test_sha224():
    plaintext = b"Dear lihua"
    cipher = hashlib.sha224(plaintext).digest()
    problem = Problem(
        ["Dear ", BfItem(length=5, char_table=string.ascii_lowercase)])
    assert sha224_solver(problem, cipher) == plaintext


def test_sha256():
    plaintext = b"Dear lihua"
    cipher = hashlib.sha256(plaintext).digest()
    problem = Problem(
        ["Dear ", BfItem(length=5, char_table=string.ascii_lowercase)])
    assert sha256_solver(problem, cipher) == plaintext


def test_sha384():
    plaintext = b"Dear lihua"
    cipher = hashlib.sha384(plaintext).digest()
    problem = Problem(
        ["Dear ", BfItem(length=5, char_table=string.ascii_lowercase)])
    assert sha384_solver(problem, cipher) == plaintext


def test_sha512():
    plaintext = b"Dear lihua"
    cipher = hashlib.sha512(plaintext).digest()
    problem = Problem(
        ["Dear ", BfItem(length=5, char_table=string.ascii_lowercase)])
    assert sha512_solver(problem, cipher) == plaintext
