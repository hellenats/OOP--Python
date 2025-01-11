
class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.curr_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.curr_idx += 1
        if self.curr_idx < self.number:
            i = self.curr_idx % len(self.sequence)
            return self.sequence[i]
        raise StopIteration()

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
