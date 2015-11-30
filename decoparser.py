import argparse
import inspect


class Cmd:
    parser = argparse.ArgumentParser()
    first_call = True
    args = None
    pre_args = list()
    
    @classmethod
    def get_args(cls):
        if Cmd.first_call:
            for args, kwargs in Cmd.pre_args:
                try:
                    Cmd.parser.add_argument(*args, **kwargs)
                except argparse.ArgumentError as e:
                    print(e.__class__.__name__)
                    print('message:\n {0}'.format(e.message))
                    print(' there are many same options')
                    exit()
            Cmd.args = Cmd.parser.parse_args()
            Cmd.first_call = False

    def __init__(self, f, name, name2, default, help, type):
        self.name = name
        self.name2 = name2
        self.f = f
        self.default = default
        self.help = help
        self.type = type
    
    def add_option(self):
        args = [self.name]
        kwargs = {'default': self.default, 'help': self.help}
        if self.name2 is not None:
            args.append(self.name2)
        if self.type is not None:
            kwargs.update({'type': self.type})
        Cmd.pre_args.append((args, kwargs))

    def add_argument(self):
        args = [self.name]
        kwargs = {'metavar': self.name.upper(), 'help': self.help}
        if self.default is not None:
            kwargs.update({'default': self.default, 'nargs': '?'})
        if self.type is not None:
            kwargs.update({'type': self.type})
        Cmd.pre_args.append((args, kwargs))

    def __call__(self, *args, **kwargs):
        Cmd.get_args()
        kname = self.name[2:] if self.name.startswith('--') else self.name
        opname = Cmd.args.__dict__[kname]
        kwargs[kname] = opname
        if inspect.getargspec(self.f).args[0] == 'self':
            self.f(self, *args, **kwargs)
        else:
            self.f(*args, **kwargs)


def option(name, name2=None, default=None, help='', type=None):
    def iner(f):
        cmd = Cmd(f, name, name2, default, help, type)
        cmd.add_option()
        return cmd
    return iner


def argument(name, default=None, help='', type=None):
    def iner(f):
        cmd = Cmd(f, name, None, default, help, type)
        cmd.add_argument()
        return cmd
    return iner


def add_description(massage):
    Cmd.parser.description = massage


def add_version(version):
    Cmd.pre_args.insert(0, (['--version'],
                            {'action': 'version', 'version': version}))
