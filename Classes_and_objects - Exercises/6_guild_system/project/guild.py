from typing import List
from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player.guild == 'Unaffiliated' or player.guild == self.name:
            if player not in self.players:
                player.guild = self.name
                self.players.append(player)
                return f"Welcome player {player.name} to the guild {self.name}"
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        try:
            player = next((p for p in self.players if p.name == player_name))
            self.players.remove(player)
            player.guild = 'Unaffiliated'
            return f"Player {player_name} has been removed from the guild."
        except StopIteration:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = [f"Guild: {self.name}", ", ".join(p.player_info() for p in self.players)]
        return '\n'.join(result)