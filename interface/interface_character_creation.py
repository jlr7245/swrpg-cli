import PyInquirer

from character_creator.character import Character
from character_creator.utils import pickler
from character_creator.species import SpeciesName, species_lookup
from character_creator.careers import CareerName, careers_lookup


def create_character():
    base_character_info = PyInquirer.prompt([{
        "type": "input", "name": "name",
        "message": "Character name"
    }, {
        "type": "list", "name": "species",
        "message": "Choose a species",
        "choices": SpeciesName.values()
    }, {
        "type": "list", "name": "career",
        "message": "Choose a career",
        "choices": CareerName.values()
    }])
    name = base_character_info["name"]
    species = species_lookup[base_character_info["species"]]
    career = careers_lookup[base_character_info["career"]]

    new_char = Character(name, species(), career())

    new_char.setup_from_species()

    should_save = PyInquirer.prompt([{
        "type": "confirm", "name": "should_save",
        "message": f"Save character {new_char.name}?"
    }])["should_save"]
    if should_save:
        pickler.pickle_character(new_char, new_char.name)
