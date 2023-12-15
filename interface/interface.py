from __future__ import print_function, unicode_literals

import PyInquirer
from pyfiglet import Figlet

from character_creator.character import Character
from character_creator.constants import SkillNames
from character_creator.utils import dice_roller, pickler
from .interface_constants import TermFormat, CLIActions
from .interface_character_creation import create_character
from .interface_update_character import update_character

class Interface:
    def __init__(self):
        self.has_been_started = False
        self.character = None

    def ask_type(self):
        font = Figlet(font='starwars')
        if not self.has_been_started:
            print(font.renderText("SWCLI"))
            self.has_been_started = True

        init_answers = PyInquirer.prompt([
            {"type": "list", "name": "action",
            "message": "Welcome to the SWRPG command line tool! What would you like to do?",
            "choices": [CLIActions.CREATE_CHARACTER, CLIActions.LOAD_CHARACTER, CLIActions.ROLL_DICE, CLIActions.EXIT]}
        ])
        match init_answers["action"]:
            case CLIActions.ROLL_DICE:
                self.roll_dice()
            case CLIActions.CREATE_CHARACTER:
                self.create_character_option()
            case CLIActions.LOAD_CHARACTER:
                self.load_character()
            case CLIActions.EXIT, _:
                print("👋 Bye!")


    def roll_dice(self):

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

        self.now_what(CLIActions.ROLL_AGAIN, self.roll_dice)


    def create_character_option(self):
        self.character = create_character()
        self.now_what(CLIActions.SETUP_CHARACTER, self.update_character_option)

    def update_character_option(self):
        update_character(self.character)
        self.now_what(CLIActions.UPDATE_CHARACTER, self.update_character_option)


    def load_character(self):
        base_character_info = PyInquirer.prompt([{
            "type": "input", "name": "character_name",
            "message": "Character name"
        }])
        char_to_load = base_character_info["character_name"]
        self.character = pickler.unpickle_character(char_to_load)
        print(f"> Loaded {TermFormat.UNDERLINE}{self.character.name}{TermFormat.ENDC} the {self.character.species.name}")
        print(self.character.list_ranked_skills())
        self.now_what(CLIActions.UPDATE_CHARACTER, self.update_character_option)


    def now_what(self, current_action: CLIActions, action,):
        what_next = PyInquirer.prompt([{
            "type": "list", "name": "up_next",
            "message": "What would you like to do?",
            "choices": [current_action, CLIActions.RETURN_HOME, CLIActions.EXIT]
        }])
        next_action = what_next["up_next"]
        if next_action == current_action:
            action() if not self.character else action(self.character)
        elif next_action == CLIActions.RETURN_HOME:
            self.ask_type()
        else:
            print("👋 Bye!")


if __name__ == "__main__":
    session = Interface()
    print(session)
    session.ask_type()
