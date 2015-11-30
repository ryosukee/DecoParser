import sys, os
sys.path.append(os.pardir)
import decoparser


@decoparser.option('--name', help='name da')
@decoparser.option('--name2')
@decoparser.option('--name3')
@decoparser.option('--name4')
def hoge(name, name2, name3, name4):
    print(name, name2, name3, name4)

decoparser.add_description('help massage')
hoge()
