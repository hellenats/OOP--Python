from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    INITIAL_AMMUNITION = 80
    AMMUNITION_DECREASE = 10

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, PirateBattleship.INITIAL_AMMUNITION)

        self.ship_type = 'PirateBattleship'

    def attack(self):
        self.ammunition -= PirateBattleship.AMMUNITION_DECREASE
        if self.ammunition <= 0:
            self.ammunition = 0
