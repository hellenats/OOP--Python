from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed

class Hen(Bird):

    @property
    def increment_weight(self):
        return 0.35

    @property
    def foods_list(self):
        return [Meat, Vegetable, Fruit, Seed]

    @staticmethod
    def make_sound():
        return 'Cluck'


class Owl(Bird):
    @property
    def increment_weight(self):
        return 0.25

    @property
    def foods_list(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return 'Hoot Hoot'
