import argparse


class Cmd:
    parser = argparse.ArgumentParser(description='test of cmd parse')
    first_call = True
    args = None

    @classmethod
    def get_args(cls):
        if Cmd.first_call:
            Cmd.args = Cmd.parser.parse_args()
            Cmd.first_call = False

    def __init__(self, f, name, name2, default):
        self.name = name
        self.name2 = name2
        self.f = f
        self.default = default
    
    def add_option(self):
        args = [self.name]
        kwargs = {'default': self.default, 'help': 'option help'}
        if self.name2 is not None:
            args.append(self.name2)

        try:
            Cmd.parser.add_argument(*args, **kwargs)
        except argparse.ArgumentError as e:
            print(e.__class__.__name__)
            print('message:\n {0}'.format(e.message))
            print(' there are many same options')
            exit()

    def add_argument(self):
        args = [self.name]
        kwargs = {'metavar': self.name.upper(), 'help': 'arg help'}
        if self.default is not None:
            kwargs.update({'default': self.default, 'nargs': '?'})
        try:
            Cmd.parser.add_argument(*args, **kwargs)
        except argparse.ArgumentError as e:
            print(e.__class__.__name__)
            print('message:\n {0}'.format(e.message))
            print(' there are many same options')
            exit()

    def __call__(self, *args, **kwargs):
        Cmd.get_args()
        kname = self.name[2:] if self.name.startswith('--') else self.name
        opname = Cmd.args.__dict__[kname]
        kwargs[kname] = opname
        self.f(*args, **kwargs)


def option(name, name2=None, default=None):
    def iner(f):
        cmd = Cmd(f, name, name2, default)
        cmd.add_option()
        return cmd
    return iner


def argument(name, default=None):
    def iner(f):
        cmd = Cmd(f, name, None, default)
        cmd.add_argument()
        return cmd
    return iner
