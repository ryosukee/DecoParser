import decoparser
import test2


@decoparser.option('--a')
def a(a):
    print(a)


@decoparser.option('--b')
def b(bbb, b):
    print(b, bbb)

a()
b('fuga')
test2.hoge()

