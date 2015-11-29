import sys, os
sys.path.append(os.pardir)
import decoparser


@decoparser.option('--hoge')
def hoge(hoge):
    print(hoge)
