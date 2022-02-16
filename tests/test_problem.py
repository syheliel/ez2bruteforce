from src.ez2bruteforce.problem import Problem,BfItem
import string
def test_problem():

    # test prue str
    problem = Problem(["abcde","abcd"])
    assert problem.length == 9 and len(problem.item_list) == 2
    assert problem.item_pos == [0,5]

    # test mixed bytes and str
    problem = Problem([b"abc", "ddd", b"acdc"])
    assert problem.length == 10 and len(problem.item_list) == 3
    assert problem.item_pos == [0, 3, 6]

    # test add bruteforce_item
    problem = Problem([b"Dear ", BfItem(length=4, char_table=string.ascii_lowercase + string.ascii_uppercase)])
    assert problem.length == 5 + 4 and len(problem.item_list) == 2
    assert problem.item_pos == [0, 5]