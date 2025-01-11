from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    INITIAL_SHIP_VOLUME = 10

    def __init__(self, code):
        super().__init__(code, RoyalZone.INITIAL_SHIP_VOLUME)

        self.zone_type = 'RoyalZone'

    def zone_info(self):
        total_ships = self.get_ships()
        pirate_ships = sum(1 for s in total_ships if s.ship_type == 'PirateBattleship')
        ship_names = ', '.join(ship.name for ship in total_ships) if total_ships else ''

        result = ("@Royal Zone Statistics@\n"
                f"Code: {self.code}; Volume: {self.volume}\n"
                f"Battleships currently in the Royal Zone: {len(total_ships)}, "
                f"{pirate_ships} out of them are Pirate Battleships.")

        return result + f"\n#{ship_names}#" if ship_names else result