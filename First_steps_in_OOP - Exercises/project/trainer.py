from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        pokemon = next((p for p in self.pokemons if p.name == pokemon_name), None)
        if pokemon:
            self.pokemons.remove(pokemon)
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for pokemon in self.pokemons:
            result += f'- {pokemon.pokemon_details()}\n'
        return result

