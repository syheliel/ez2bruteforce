from src.ez2bruteforce.problem import BfItem, ConstItem


def test_bruteforce_item():
    # test str and duplication's elimination
    _ = BfItem(length=3, char_table="abcabd")
    assert _.length == 3 and len(_.char_table) == 4
    # test bytes and duplication's elimination
    _ = BfItem(length=100, char_table=b"xxxyz")
    assert _.length == 100 and len(_.char_table) == 3
    # test lists and duplication's elimination
    _ = BfItem(length=3, char_table=["abca", "xyz", b"!@#"])
    assert _.length == 3 and len(_.char_table) == 9

def test_const_item():
    ConstItem("abcd")
    ConstItem(b"abcde")
