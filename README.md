# FactorDB CLI (and Python library)
[![Travis](https://img.shields.io/travis/ryo-san470/factordb-pycli.svg?style=flat-square)]()

The [FactorDB](https://factordb.com) is the database to store known factorizations for any number.
This tool can use on your command line. 
And also you can use this tool with python 2 & 3 scripts.

## Basic Usage

### CLI
If you want to know the result of factorization of 16, you should type like this:

```bash
$ factordb 16
```

Then, you can get the answer from factordb.com.

```bash
$ factordb 16
2 2 2 2
```

If you want to know more detail of result, you can get an answer of JSON format.

```bash
$ factordb --json 16
{"id": "https://factordb.com/?id=2", "status": "FF", "factors": [2, 2, 2, 2]}
```

### Library usage
If you want to use this script with Python, you should type `import` statement on your code like this:

```
import factordb
# or
from factordb import FactorDB
```

Then, you can get the answer with Python lists.

```
In [1]: from factordb import FactorDB

In [2]: f = FactorDB(16)

In [3]: f.get_factor_list()
Out[3]: [2, 2, 2, 2]
```

# License
MIT
