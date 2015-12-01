import sys
import os
sys.path.append(os.pardir)
import decoparser
import not_main


@decoparser.option('--age', type=int, default=10)
def hoge(age):
    print(age, not_main.get_name())


@decoparser.option('--f', type=decoparser.FileType())
def fuga(f):
    global gf
    gf = f
    print('f: ', f.closed)

gf = None
hoge()
fuga()
print('gf: ', gf.closed)
