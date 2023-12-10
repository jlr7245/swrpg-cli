import PyInquirer

from character_creator.character import Character
from character_creator.utils import pickler

def create_character():
    base_character_info = PyInquirer.prompt([{
        "type": "input", "name": "character_name",
        "message": "Character name"
    }])
    new_char = Character(base_character_info["character_name"])
    should_save = PyInquirer.prompt([{
        "type": "confirm", "name": "should_save",
        "message": f"Save character {new_char.name}?"
    }])["should_save"]
    if should_save:
        pickler.pickle_character(new_char, new_char.name)
    

