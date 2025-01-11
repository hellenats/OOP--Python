class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    @property
    def free_space(self):
        free_space = self.size - self.quantity
        return free_space

    def fill(self, quantity):
        if quantity <= self.free_space:
            self.quantity += quantity

    def status(self):
        return self.free_space


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
