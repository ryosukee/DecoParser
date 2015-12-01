import sys
import os
sys.path.append(os.pardir)
import decoparser
import not_main


@decoparser.option('--age', type=int, default=10)
def hoge(age):
    print(age, not_main.get_name())


hoge()
