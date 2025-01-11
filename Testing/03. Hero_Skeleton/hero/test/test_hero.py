from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero('Niko', 1, 100.0, 100)
        self.enemy = Hero('Karlos', 1, 50.0, 100)

    def test_correct_init_(self):
        self.assertEqual("Niko", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_when_enemy_has_the_same_name_as_hero_raises_exception(self):
        self.enemy.username = 'Niko'

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_hero_has_negative_or_zero_health_raises_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_when_enemy_has_negative_or_zero_health_raises_value_error(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Karlos. He needs to rest", str(ve.exception))

    def test_battle_when_players_health_drops_to_zero_or_less_results_in_draw(self):
        self.hero.health = 50
        draw_res = self.hero.battle(self.enemy)

        self.assertEqual("Draw", draw_res)

    def test_battle_when_hero_beats_enemy_increases_hero_stats(self):
        self.enemy.damage = 1

        expected_enemy_health = self.enemy.health - self.hero.damage
        expected_hero_health = (self.hero.health - self.enemy.damage) + 5
        expected_hero_level = self.hero.level + 1
        expected_hero_damage = self.hero.damage + 5

        expected_win_message = self.hero.battle(self.enemy)

        self.assertEqual(expected_enemy_health, self.enemy.health)
        self.assertEqual(expected_hero_level, self.hero.level)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_hero_damage, self.hero.damage)
        self.assertEqual("You win", expected_win_message)

    def test_battle_when_enemy_wins_increases_enemy_stats(self):
        self.hero.damage = 1

        expected_enemy_health = self.enemy.health - self.hero.damage + 5
        expected_hero_health = self.hero.health - self.enemy.damage
        expected_enemy_level = self.enemy.level + 1
        expected_enemy_damage = self.enemy.damage + 5

        expected_win_message = self.hero.battle(self.enemy)

        self.assertEqual(expected_enemy_health, self.enemy.health)
        self.assertEqual(expected_enemy_level, self.enemy.level)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_enemy_damage, self.enemy.damage)
        self.assertEqual("You lose", expected_win_message)

    def test_str_returns_correct_message(self):
        expected_message = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                           f"Health: {self.hero.health}\n" \
                           f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected_message, str(self.hero))

if __name__ == '__main__':
    main()