# ez2bruteforce [![codecov](https://codecov.io/gh/syheliel/ez2bruteforce/branch/main/graph/badge.svg?token=CD20F10MRO)](https://codecov.io/gh/syheliel/ez2bruteforce)
**ez2bruteforce** is a python package that allows you to bruteforce the POW(proof of the work) stage in CTF game.
You can specify the char table, bruteforce length and the position and then use bruteforce to crack its hash digtest.

pypi home page：https://pypi.org/project/ez2bruteforce/



## Example
If you have known the hash of the digtest, like this:
```python
import hashlib
cipher = hashlib.sha1(b"Dear XXX:")
# cipher = b"\xf0\x1d\xb9\xe9|Xh\x84\xdb\r\xb0'\xa7\x80\xdc\x07\xbc\xca_`"
```

Then you can use ez2bruteforce to crack it.
`BfItem(3, string.ascii_letters)` means the bruteforce length is 3, and the char table is " all ascii letter.
`sha1_solver(problem,cipher)` will return the original string if the hash is correct.
```python
from ez2bruteforce import BfItem,Problem,sha1_solver
import string
cipher = b"\xf0\x1d\xb9\xe9|Xh\x84\xdb\r\xb0'\xa7\x80\xdc\x07\xbc\xca_`"
problem = Problem(["Dear ",BfItem(3,string.ascii_letters),":"])
result = sha1_solver(problem,cipher)
# result = b'Dear abc:'
```
Also, you can pass your own hash function into the `generic_solver`.
```python
from ez2bruteforce import BfItem,Problem,generic_solver
from base64 import b64decode,b64encode
cipher = b64encode(b'abc')
problem = Problem([BfItem(3,"abcdefg")])
result = generic_solver(problem,cipher,b64encode)
# result = b'abc'
```

## TODO
- [x] tpye-stub support
- [ ] Muti-threading support
- [ ] Add `import *` support