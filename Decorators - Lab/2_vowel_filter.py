
def vowel_filter(func):

    def wrapper():
        result = func()
        return [el for el in result if el.lower() in 'aeuioy']

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "C", "d", "E"]

print(get_letters())
