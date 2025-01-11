
class Stack:
    def __init__(self, *args):
        self.data: list = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


s = Stack()
s.push('box')
s.push('cup')
print(s.top())
print(s)
print(s.is_empty())
s.pop()
s.pop()
print(s.is_empty())