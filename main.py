import functools


def deprecated(func=None, since=None, will_be_removed=None):
    if not func:
        return functools.partial(deprecated, since=since, will_be_removed=will_be_removed)

    @functools.wraps(func)
    def g():
        if since:
            print(f"Warning: function {g.__name__} is deprecated since version {since}.")
        else:
            print(f"Warning: function {g.__name__} is deprecated.")
        if will_be_removed:
            print(f"It will be removed in version {will_be_removed}")
        else:
            print("It will be removed in future versions.")
        return func()
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
