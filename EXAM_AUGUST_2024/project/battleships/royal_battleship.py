from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):
    INITIAL_AMMUNITION = 100
    AMMUNITION_DECREASE = 25

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, RoyalBattleship.INITIAL_AMMUNITION)

        self.ship_type = 'RoyalBattleship'

    def attack(self):
        self.ammunition -= RoyalBattleship.AMMUNITION_DECREASE
        if self.ammunition <= 0:
            self.ammunition = 0
