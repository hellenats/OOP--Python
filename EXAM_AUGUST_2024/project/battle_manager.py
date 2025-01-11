from typing import List
from project.zones.royal_zone import RoyalZone
from project.zones.pirate_zone import PirateZone
from project.battleships.royal_battleship import RoyalBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.base_battleship import BaseBattleship
from project.zones.base_zone import BaseZone


class BattleManager:
    VALID_ZONES = {
        "RoyalZone": RoyalZone,
        "PirateZone": PirateZone
    }
    VALID_SHIPS = {
        'RoyalBattleship': RoyalBattleship,
        'PirateBattleship': PirateBattleship
    }
    ALLIES = {
        "RoyalZone": "RoyalBattleship",
        "PirateZone": "PirateBattleship"
    }

    def __init__(self):
        self.zones: List[BaseZone] = []
        self.ships: List[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        try:
            zone = BattleManager.VALID_ZONES[zone_type](zone_code)
        except KeyError:
            raise Exception("Invalid zone type!")

        try:
            next(z for z in self.zones if z.code == zone_code)
            raise Exception("Zone already exists!")
        except StopIteration:
            self.zones.append(zone)
            return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        try:
            ship = BattleManager.VALID_SHIPS[ship_type](name, health, hit_strength)
        except KeyError:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        self.ships.append(ship)
        return f"A new {ship_type} was successfully added."

    @staticmethod
    def add_ship_to_zone(zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if BattleManager.ALLIES[zone.zone_type] == ship.ship_type:
            ship.is_attacking = True
        else:
            ship.is_attacking = False

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        ship = next((s for s in self.ships if s.name == ship_name), None)

        if ship is None:
            return "No ship with this name!"

        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        attacker = max((s for s in zone.ships if s.is_attacking), key=lambda s: s.hit_strength, default=None)
        enemy = max((ship for ship in zone.ships if not ship.is_attacking), key=lambda s: s.health, default=None)

        if not attacker or not enemy:
            return "Not enough participants. The battle is canceled."

        attacker.attack()
        enemy.take_damage(attacker)

        if enemy.health <= 0:
            zone.ships.remove(enemy)
            self.ships.remove(enemy)
            return f"{enemy.name} lost the battle and was sunk."

        if attacker.ammunition <= 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships = [s for s in self.ships if s.is_available]
        available_ships_name = ', '.join(s.name for s in available_ships) if available_ships else ''
        zones = sorted(self.zones, key= lambda x: x.code)

        zones_info = "\n".join(z.zone_info() for z in self.zones)

        result = f"Available Battleships: {len(available_ships)}\n"
        result += f"#{available_ships_name}#\n" if available_ships else ''
        result += (f"***Zones Statistics:***\n"
                   f"Total Zones: {len(zones)}\n"
                   f"{zones_info}")

        return result.strip()