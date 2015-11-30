import sys, os
sys.path.append(os.pardir)
import decoparser


class Test:
    @decoparser.option('--name')
    def __init__(self, name):
        print(name)


t = Test()
