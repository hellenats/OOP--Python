
def even_parameters(function):

    def wrapper(*args):
        for n in args:
            if isinstance(n, str) or n % 2 != 0:
                return "Please use only even numbers!"

        return function(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add(3, 1))
