# pycatj

Flattens json/yaml files into python compatible paths

## Installation

```
pip install git+https://github.com/dbarrosop/pycatj.git
```

## Usage

```
$ pycatj -h
usage: pycatj [-h] [--format {json,yaml}] filepath

Displays JSON files in a flat format (inspired by mattleibow/catj)

positional arguments:
  filepath              File to process

optional arguments:
  -h, --help            show this help message and exit
  --format {json,yaml}  Format of the file
  --root ROOT           This is the root of your path, the var where you will
                        load your data

$ cat tests/data/test_1.json
{
    "somekey": "somevalue",
    "somenumber": 123,
    "a_dict": {
        "asd": "123",
        "qwe": [1, 2, 3],
        "nested_dict": {
            "das": 31,
            "qwe": "asd"
        }
    }
}

$ pycatj --root my_var tests/data/test_1.json
my_var["somekey"] = "somevalue"
my_var["somenumber"] = 123
my_var["a_dict"]["asd"] = "123"
my_var["a_dict"]["qwe"][0] = 1
my_var["a_dict"]["qwe"][1] = 2
my_var["a_dict"]["qwe"][2] = 3
my_var["a_dict"]["nested_dict"]["das"] = 31
my_var["a_dict"]["nested_dict"]["qwe"] = "asd"

$ cat tests/data/test_1.yaml
---
"somekey": "somevalue"
"somenumber": 123
"a_dict":
    "asd": "123"
    "qwe":
    - 1
    - 2
    - 3
    "nested_dict":
        "das": 31
        "qwe": "asd"

$ pycatj --root my_var tests/data/test_1.yaml
my_var["somekey"] = "somevalue"
my_var["somenumber"] = 123
my_var["a_dict"]["asd"] = "123"
my_var["a_dict"]["qwe"][0] = 1
my_var["a_dict"]["qwe"][1] = 2
my_var["a_dict"]["qwe"][2] = 3
my_var["a_dict"]["nested_dict"]["das"] = 31
my_var["a_dict"]["nested_dict"]["qwe"] = "asd"
```
