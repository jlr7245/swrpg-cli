from __future__ import print_function, unicode_literals

import PyInquirer
from pyfiglet import Figlet

from character_creator.character import Character
from character_creator.constants import SkillNames
from character_creator.utils import dice_roller, pickler
from .interface_constants import TermFormat, Actions
from .interface_character_creation import create_character



def ask_type():
    font = Figlet(font='starwars')
    print(font.renderText("SWCLI"))

    init_answers = PyInquirer.prompt([
        {"type": "list", "name": "action",
         "message": "Welcome to the SWRPG command line tool! What would you like to do?",
         "choices": [Actions.CREATE_CHARACTER, Actions.LOAD_CHARACTER, Actions.ROLL_DICE, Actions.EXIT]}
    ])
    match init_answers["action"]:
        case Actions.ROLL_DICE:
            roll_dice()
        case Actions.CREATE_CHARACTER:
            create_character_option()
        case Actions.LOAD_CHARACTER:
            load_character()
        case Actions.EXIT, _:
            print("👋 Bye!")


def roll_dice():

    color_coded_die_types = (f"{TermFormat.LIGHT_CYAN}{TermFormat.BOLD}b{TermFormat.ENDC}, "
                             f"{TermFormat.GRAY}{TermFormat.BOLD}s{TermFormat.ENDC}, "
                             f"{TermFormat.GREEN}{TermFormat.BOLD}a{TermFormat.ENDC}, "
                             f"{TermFormat.PURPLE}{TermFormat.BOLD}d{TermFormat.ENDC}, "
                             f"{TermFormat.YELLOW}{TermFormat.BOLD}p{TermFormat.ENDC}, "
                             f"{TermFormat.RED}{TermFormat.BOLD}c{TermFormat.ENDC}, "
                             f"{TermFormat.BOLD}f{TermFormat.ENDC}")
    print(f"> Available dice: {color_coded_die_types}")

    init_answers = PyInquirer.prompt([
        {"type": "input", "name": "dice_input",
         "message": f"Please enter the dice you'd like to roll."}
    ])
    output = dice_roller.dice_roller_swrpg(init_answers["dice_input"])
    print(f"> You rolled: {TermFormat.PURPLE}{TermFormat.BOLD}{output}{TermFormat.ENDC}")

    now_what(Actions.ROLL_AGAIN, roll_dice)


def create_character_option():
    create_character()
    now_what(Actions.CREATE_CHARACTER, create_character_option)


def load_character():
    base_character_info = PyInquirer.prompt([{
        "type": "input", "name": "character_name",
        "message": "Character name"
    }])
    char_to_load = base_character_info["character_name"]
    char: Character = pickler.unpickle_character(char_to_load)
    char.upgrade_skill(SkillNames.COOL)
    print(char.get_skill_rank(SkillNames.COOL))


def now_what(current_action: str, action: Actions, character: Character=None):
    what_next = PyInquirer.prompt([{
        "type": "list", "name": "up_next",
        "message": "What would you like to do?",
        "choices": [current_action, Actions.RETURN_HOME, Actions.EXIT]
    }])
    next_action = what_next["up_next"]
    if next_action == current_action:
        action() if not character else action(character)
    elif next_action == Actions.RETURN_HOME:
        ask_type()
    else:
        print("👋 Bye!")


if __name__ == "__main__":
    ask_type()
