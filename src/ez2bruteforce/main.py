from typing import *
from itertools import chain, product
import hashlib


def to_bytes(x: Union[str, bytes], encoding: str) -> bytes:
    if isinstance(x, str):
        return x.encode(encoding)
    else:
        return x


class bruteforce_item:
    def __init__(self, length: int, char_table: Union[str, bytes, List[Union[str, bytes]]], encoding: str = 'utf-8'):
        self.length = length
        self.char_table: bytearray = bytearray()
        if isinstance(char_table, str):
            self.char_table.extend(to_bytes(char_table, encoding))
        elif isinstance(char_table, bytes):
            self.char_table.extend(char_table)
        elif isinstance(char_table, list):
            self.char_table.extend(chain(*map(lambda x: to_bytes(x, encoding), char_table)))
        else:
            raise TypeError(f'char_table must be str, bytes or list, not {type(char_table)}')

    def __len__(self):
        return self.length


class const_item:
    def __init__(self, string: Union[str, bytes], encoding='utf-8'):
        self.string: bytearray = bytearray()
        if isinstance(string, str):
            self.string.extend(to_bytes(string, encoding))
        elif isinstance(string, bytes):
            self.string.extend(string)
        else:
            raise TypeError(f'string must be str or bytes, not {type(string)}')

    def __len__(self):
        return len(self.string)


class Problem():
    def __init__(self, item_list: List[Union[bruteforce_item, str, bytes]], encoding='utf-8'):
        self.item_list: List[Union[bruteforce_item, const_item]] = list()
        for item in item_list:
            if isinstance(item, bruteforce_item):
                self.item_list.append(item)
            elif isinstance(item, str) or isinstance(item, bytes):
                self.item_list.append(const_item(item, encoding))
            else:
                raise TypeError(f'item must be bruteforce_item or str or bytes, not {type(item)}')


def solve(problem: Problem, cipher: bytes, hash_func: Callable[[bytearray], bytes]) -> Optional[bytes]:
    assert isinstance(cipher,bytes)
    plaintext = bytearray()
    pos_index: List[int] = []
    char_table_list = []
    for item in problem.item_list:
        item_len = len(item)  # all item class implement __len__ to return length in the plaintext
        if isinstance(item, bruteforce_item):
            current_index = len(plaintext)
            pos_index.extend(range(current_index, current_index + item_len))
            plaintext.extend(b'\x00' * item_len)  # append useless bytes
            char_table_list.extend([item.char_table] * item_len)

        elif isinstance(item, const_item):
            plaintext.extend(item.string)

    assert len(char_table_list) == len(pos_index)
    for product_item in product(*char_table_list):
        for pos, c in zip(pos_index, product_item):
            plaintext[pos] = c
        print(plaintext, hash_func(plaintext))
        if hash_func(plaintext) == cipher:
            return bytes(plaintext)
    return None


if __name__ == "__main__":
    problem = Problem([bruteforce_item(2, 'abc'), "HH", bruteforce_item(2, 'abc')])
    cipher = hashlib.sha256(b"ccHHcc").digest()
    res = solve(problem, cipher, lambda x:hashlib.sha256(x).digest())
    print(res)
    print(cipher)

