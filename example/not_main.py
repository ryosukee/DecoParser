import sys
import os
sys.path.append(os.pardir)
import decoparser


@decoparser.argument('name')
def get_name(name):
    return name
