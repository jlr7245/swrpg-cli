import random
from operator import attrgetter
from data import dice_sides

def dice_roller(sides: int) -> int:
    rolled_number = random.randrange(1, sides)
    return rolled_number

def dice_roller_swrpg(types: str) -> str:
    """Rolls a number of swrpg type dice. For example, a roll with three
    advantage dice, two challenge dice, and a setback die would be represented
    with the string '3a 2c 1s'. Valid types are b, s, a, d, p, c, f"""
    results_list = []
    for die in types.split():
        [i, d] = list(die)
        if d not in dice_sides.key:
            raise ValueError(f"{d} not a valid SWRPG die type.")
        for _num in range(int(i)):
            num_sides = dice_sides.num_sides[d]
            rolled_num = dice_roller(num_sides)
            results_list.append(dice_sides.key[d][rolled_num])
    reconciled = reconcile_results(results_list)
    return stringify_results(reconciled)

def reconcile_results(results_list):
    raw = {
        "success": 0,
        "failure": 0,
        "advantage": 0,
        "threat": 0,
        "triumph": 0,
        "despair": 0,
        "dark": 0,
        "light": 0,
    }
    for result in results_list:
        for key, value in result.items():
            raw[key] += value
    print(raw)
    total_success = (raw["success"] + raw["triumph"]) - (raw["failure"] + raw["despair"])
    total_advantage = raw["advantage"] - raw["threat"]
    success_results = { "success": total_success } if total_success > 0 else { "failure": abs(total_success) }
    advantage_results = { "advantage": total_advantage} if total_advantage > 0 else {"disadvantage": abs(total_advantage)}
    final_results = {
        "triumph": raw["triumph"], "despair": raw["despair"],
        "dark": raw["dark"], "light": raw["light"],
        **success_results,
        **advantage_results
    }
    return final_results

def stringify_results(results):
    results_list = []
    print(results)
    for key, value in results.items():
        if value > 0:
            results_list.append(f"{value} {key}")
    return "; ".join(results_list)



