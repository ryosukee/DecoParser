import argparse
import inspect


class Cmd:
    parser = argparse.ArgumentParser(description='test of cmd parse')
    first_call = True
    args = None

    @classmethod
    def get_args(cls):
        if Cmd.first_call:
            Cmd.args = Cmd.parser.parse_args()
            Cmd.first_call = False

    def __init__(self, f, name, name2):
        self.name = name
        self.f = f
        # args = inspect.getargspec(f)
        try:
            if name2 is not None:
                Cmd.parser.add_argument(
                    name, name2,
                    required=True,
                    help='test',
                )
            else:
                Cmd.parser.add_argument(
                    name,
                    required=True,
                    help='test',
                )
        except argparse.ArgumentError as e:
            print(e.__class__.__name__)
            print('message:\n {0}'.format(e.message))
            print(' there are many same options')
            exit()

    def __call__(self, *args, **kwargs):
        Cmd.get_args()
        kname = self.name[2:]
        opname = Cmd.args.__dict__[kname]
        kwargs[kname] = opname
        self.f(*args, **kwargs)


def option(name, name2=None):
    def iner(f):
        cmd = Cmd(f, name, name2)
        return cmd
    return iner
