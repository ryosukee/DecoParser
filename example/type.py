import sys, os
sys.path.append(os.pardir)
import decoparser


@decoparser.option('--name', type=int)
def hoge(name):
    print(name)
    print(type(name))

decoparser.add_version('1.0')
hoge()
