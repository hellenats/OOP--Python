
class dictionary_iter:
    def __init__(self, dictionary):
        self.dict_tuples = tuple(dictionary.items())
        self.curr_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.curr_idx += 1
        if self.curr_idx < len(self.dict_tuples):
            return self.dict_tuples[self.curr_idx]
        raise StopIteration()

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

