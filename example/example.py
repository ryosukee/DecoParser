import sys
import os
sys.path.append(os.pardir)
import decoparser
import not_main


@decoparser.option('--age', type=int, default=10)
def hoge(age):
    print(age, not_main.get_name())


@decoparser.option('--f', type=decoparser.FileType())
@decoparser.option('--f2', type=decoparser.FilePath(exists=True, absolute=True))
def fuga(f, f2):
    global gf
    gf = f
    print('f: ', f.closed)
    print(f2)

gf = None
hoge()
fuga()
print('gf: ', gf.closed)
