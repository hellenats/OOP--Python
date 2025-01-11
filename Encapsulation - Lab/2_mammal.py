class Mammal:
    __kingdom = 'animals'

    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


spider = Mammal('Pipo', 'spider', 'psss')
print(spider.get_kingdom())
print(spider.info())
print(spider.make_sound())
spider._Mammal__kingdom = 'spiders'
print(spider.get_kingdom())