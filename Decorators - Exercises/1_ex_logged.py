
def logged(func):

    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        func_name = func.__name__

        output = [f'you called {func_name}{args}', f"it returned {func_result}"]

        return '\n'.join(output)
    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
