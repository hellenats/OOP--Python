
class vowels:

    def __init__(self, text):
        self.text = text
        self.only_vowels = [el for el in self.text if el.lower() in 'aeiuyo']
        self.current_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_idx += 1
        if self.current_idx < len(self.only_vowels):
            return self.only_vowels[self.current_idx]
        raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
