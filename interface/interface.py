from __future__ import print_function, unicode_literals

import PyInquirer
from pyfiglet import Figlet

from character_creator.character import Character
from character_creator.constants import SkillNames
from character_creator.utils import dice_roller, pickler
from .interface_constants import TermFormat, CLIActions
from .interface_character_creation import create_character
from .interface_update_character import update_character



def ask_type():
    font = Figlet(font='starwars')
    print(font.renderText("SWCLI"))

    init_answers = PyInquirer.prompt([
        {"type": "list", "name": "action",
         "message": "Welcome to the SWRPG command line tool! What would you like to do?",
         "choices": [CLIActions.CREATE_CHARACTER, CLIActions.LOAD_CHARACTER, CLIActions.ROLL_DICE, CLIActions.EXIT]}
    ])
    match init_answers["action"]:
        case CLIActions.ROLL_DICE:
            roll_dice()
        case CLIActions.CREATE_CHARACTER:
            create_character_option()
        case CLIActions.LOAD_CHARACTER:
            load_character()
        case CLIActions.EXIT, _:
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

    now_what(CLIActions.ROLL_AGAIN, roll_dice)


def create_character_option():
    create_character()
    now_what(CLIActions.CREATE_CHARACTER, create_character_option)

def update_character_option(character):
    update_character(character)
    now_what(CLIActions.UPDATE_CHARACTER, update_character_option, character)


def load_character():
    base_character_info = PyInquirer.prompt([{
        "type": "input", "name": "character_name",
        "message": "Character name"
    }])
    char_to_load = base_character_info["character_name"]
    char: Character = pickler.unpickle_character(char_to_load)
    print(f"> Loaded {TermFormat.UNDERLINE}{char.name}{TermFormat.ENDC} the {char.species.name}")
    print(char.list_ranked_skills())
    now_what(CLIActions.UPDATE_CHARACTER, update_character_option, char)


def now_what(current_action: CLIActions, action, character: Character=None):
    what_next = PyInquirer.prompt([{
        "type": "list", "name": "up_next",
        "message": "What would you like to do?",
        "choices": [current_action, CLIActions.RETURN_HOME, CLIActions.EXIT]
    }])
    next_action = what_next["up_next"]
    if next_action == current_action:
        action() if not character else action(character)
    elif next_action == CLIActions.RETURN_HOME:
        ask_type()
    else:
        print("👋 Bye!")


if __name__ == "__main__":
    ask_type()
