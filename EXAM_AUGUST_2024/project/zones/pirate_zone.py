from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_SHIP_VOLUME = 8

    def __init__(self, code):
        super().__init__(code, PirateZone.INITIAL_SHIP_VOLUME)

        self.zone_type = 'PirateZone'

    def zone_info(self):
        total_ships = self.get_ships()
        royal_ships = sum(1 for s in total_ships if s.ship_type == 'RoyalBattleship')
        ship_names = ', '.join(ship.name for ship in total_ships) if total_ships else ''

        result = ("@Pirate Zone Statistics@\n"
                f"Code: {self.code}; Volume: {self.volume}\n"
                f"Battleships currently in the Pirate Zone: {len(total_ships)}, "
                f"{royal_ships} out of them are Royal Battleships.")

        return result + f"\n#{ship_names}#" if ship_names else result
