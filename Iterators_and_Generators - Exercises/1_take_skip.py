
class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.curr_num = 0 - self.step
        self.curr_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.curr_idx += 1
        self.curr_num += self.step
        if self.curr_idx <= self.count:
            return self.curr_num
        raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
