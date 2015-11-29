import sys, os
sys.path.append(os.pardir)
import decoparser


@decoparser.option('--a', '-a', default=20)
def test(b, a):
    print(a, b)

test('test: ')
