
class reverse_iter:
    def __init__(self, items):
        self.items = items
        self.curr_end_idx = len(self.items)

    def __iter__(self):
        return self

    def __next__(self):

        if self.curr_end_idx > 0:
            self.curr_end_idx -= 1
            return self.items[self.curr_end_idx]
        raise StopIteration

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
