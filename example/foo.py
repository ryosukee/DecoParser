import decoparser

@decoparser.option('--h1')
@decoparser.option('--h2')
def hoge(h1, h2):
      print(h1, h2)

@decoparser.option('--f')
def fuga(f):
    print(f)

hoge()
fuga()
