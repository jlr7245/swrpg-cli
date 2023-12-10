import random
from data import dice_sides

def dice_roller(sides: int) -> int:
    rolled_number = random.randrange(1, sides)
    return rolled_number

def dice_roller_swrpg(types: str) -> str:
    """Rolls a number of swrpg type dice. For example, a roll with three
    advantage dice, two challenge dice, and a setback die would be represented
    with the string '3a 2c 1s'. Valid types are b, s, a, d, p, c, f"""
    individual_dice = types.split()
    for die in individual_dice:
        [i, d] = list(die)
        if d not in dice_sides.key:
            raise ValueError("#{d} not a valid SWRPG die type")
    return True

