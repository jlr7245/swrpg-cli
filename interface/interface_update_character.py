from character_creator.character import Character
from character_creator.utils import pickler

def update_character(char: Character):
    print(f"Updating {char.name} the {char.species.name}")
    pickler.pickle_character(char, char.name)
    
