import functools


def deprecated(func=None, since=None, will_be_removed=None):
    if func is None:
        return functools.partial(deprecated, since=since, will_be_removed=will_be_removed)

    @functools.wraps(func)
    def g(*args, **kwargs):
        print(f"Warning: function {g.__name__} is deprecated {'' if since is None else f'since version {since}'}.")
        print(f"It will be removed in {'future versions' if will_be_removed is None else f'version {will_be_removed}'}.")
        return func(*args, **kwargs)
    return g


@deprecated
def foo():
    print("Hello from foo")


@deprecated(since="4.2.0", will_be_removed="5.0.1")
def bar():
    print("Hello from bar")


if __name__ == '__main__':
    foo()
    bar()
