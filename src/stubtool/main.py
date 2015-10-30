import sys


def create_context(out_dir):
    from .emitters.null import NullEmitter
    from .emitters.six_moves import SixMovesEmitter
    from .context import Context

    factories = {
        'six.moves': SixMovesEmitter,
    }
    return Context(out_dir, NullEmitter, factories)


def main(args=None):
    if args is None:
        args = sys.argv
    assert len(args) >= 3
    # TODO actually parse arguments with argparse or something.
    ctx = create_context(args[1])
    done = set()
    todo = args[2:]
    for mod in todo:
        if mod in done:
            continue
        # I'm not very happy with this.
        todo.extend(ctx.do_emit(mod))
        done.add(mod)
