import sys, os
sys.path.append(os.pardir)
import decoparser


@decoparser.argument('name', default='hogehoge')
@decoparser.argument('name2')
def hoge(name, name2):
    print(name, name2)

hoge()
