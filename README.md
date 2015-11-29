## This is not release version yet.

This is a simple command line parser.  
It can be used as decorator like [Click][].  
The differences from [Click][] are below.  


1. You can use multiple function for each option and argument.  
Hence, you only have to add decorator to a function requiring arguments and options.  

  foo.py
  ```python
import decoparser

@decoparser.option('--h1')
@decoparser.option('--h2')
def hoge(h1, h2):
  print(h1, h2)

@decoparser.option('--f')
def fuga(f):
  print(f)

hoge()
fuga()
```

  python foo.py -h
  ```
usage: foo.py [-h] --h2 H2 --h1 H1 --f F

test of cmd parse

optional arguments:
  -h, --help  show this help message and exit
  --h2 H2     test
  --h1 H1     test
  --f F       test
```
python foo.py --h1 hoge1 --h2 hoge2 --f fuga
 ```
hoge1 hoge2
fuga
```

2. You can use both type of argument - command line options and normal arguments - in one function.  
  baz.py
  ```python
  import decoparser
  
  @decoparser.option('h')
  def hoge(normal_arg, h):
    print(normal_arg, h)
  
  hoge('normal')
  ```
  python baz.py --h hoge
  ```
  normal hoge
  ```



[Click]: http://click.pocoo.org/
