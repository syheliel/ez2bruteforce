from src.ez2bruteforce.problem import Problem, BfItem
from src.ez2bruteforce.solver import sha1_solver
import hashlib
import string


def test_sha1():
    plaintext = b"Dear lihua"
    cipher = hashlib.sha1(plaintext).digest()
    problem = Problem(["Dear ", BfItem(length=5, char_table=string.ascii_lowercase)])
    assert sha1_solver(problem, cipher) == plaintext
