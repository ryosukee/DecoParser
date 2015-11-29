This is a simple command line parser.  
It can be used as decorator like [Click][].  
The differences from [Click][] are below.  


1. You can use multiple function for each option and argument.  
Hence, you only have to add decorator to a function requiring arguments and options.  
The example is illustrated as following foo.py.  


  ```python
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
The results of `python foo.py -h` is 
  ```
usage: foo.py [-h] --h2 H2 --h1 H1 --f F

test of cmd parse

optional arguments:
  -h, --help  show this help message and exit
  --h2 H2     test
  --h1 H1     test
  --f F       test
```
The results of `python foo.py --h1 hoge1 --h2 hoge2 --f fuga` is
 ```
hoge1 hoge2
fuga
```



[Click]: http://click.pocoo.org/
