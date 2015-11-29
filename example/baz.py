import decoparser

@decoparser.option('--h')
def hoge(normal_arg, h):
    print(normal_arg, h)

hoge('normal')
