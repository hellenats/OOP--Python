
def create_row(size, row):
    result = f'{" " * (size - row)}{"* " * row}'
    print(result[:-1])


def upper_part(size):
    for row in range(1, size + 1):
        create_row(size, row)


def bottom_part(size):
    for row in range(size - 1, 0, -1):
        create_row(size, row)


def print_rhombus(size):
    upper_part(size)
    bottom_part(size)


n = int(input())
print_rhombus(n)