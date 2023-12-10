from ..utils.super_enum import SuperEnum

class TermFormat(SuperEnum):
    GRAY = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    PURPLE = '\033[94m'
    BLUE = '\033[34m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    LIGHT_CYAN = '\033[36m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    DESATURATED = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    SLOW_BLINK = '\033[5m'

class Actions(SuperEnum):
    ROLL_DICE = "Roll some dice"
    ROLL_AGAIN = "Roll again"
    CREATE_CHARACTER = "Make a character"
    LOAD_CHARACTER = "Load a character"
    EXIT = "Exit"
    RETURN_HOME = "Return home"

