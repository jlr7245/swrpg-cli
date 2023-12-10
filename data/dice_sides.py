boost = {
    1: {}, 2: {},
    3: {"success": 1},
    4: {"success": 1, "advantage": 1},
    5: {"advantage": 2},
    6: {"advantage": 1},
}

setback = {
    1: {}, 2: {},
    3: {"failure": 1}, 4: {"failure": 1},
    5: {"threat": 1}, 6: {"threat": 1},
}

ability = {
    1: {},
    2: {"success": 1}, 3: {"success": 1},
    4: {"success": 2},
    5: {"advantage": 1}, 6: {"advantage": 1},
    7: {"success": 1, "advantage": 1},
    8: {"advantage": 2}
}

difficulty = {
    1: {},
    2: {"failure": 1},
    3: {"failure": 2},
    4: {"threat": 1}, 5: {"threat": 1}, 6: {"threat": 1},
    7: {"threat": 2},
    8: {"failure": 1, "threat": 1}
}

proficiency = {
    1: {},
    2: {"success": 1}, 3: {"success": 1},
    4: {"success": 2}, 5: {"success": 2},
    6: {"advantage": 1},
    7: {"success": 1, "advantage": 1},
    8: {"success": 1, "advantage": 1},
    9: {"success": 1, "advantage": 1},
    10: {"advantage": 2}, 11: {"advantage": 2},
    12: {"triumph": 1}
}

challenge = {
    1: {},
    2: {"failure": 1}, 3: {"failure": 1},
    4: {"failure": 2}, 5: {"failure": 2},
    6: {"threat": 1}, 7: {"threat": 1},
    8: {"failure": 1, "threat": 1},
    9: {"failure": 1, "threat": 1},
    10: {"threat": 2}, 11: {"threat": 2},
    12: {"despair": 1}
}

force = {
    1: {"dark": 1}, 2: {"dark": 1}, 3: {"dark": 1},
    4: {"dark": 1}, 5: {"dark": 1}, 6: {"dark": 1},
    7: {"dark": 2},
    8: {"light": 1}, 9: {"light": 1},
    10: {"light": 2}, 11: {"light": 2}, 12: {"light": 2},
}

num_sides = {
    "b": 6, "s": 6,
    "a": 8, "d": 8,
    "p": 12, "c": 12, "f": 12,
}

key = {
    "b": boost,
    "s": setback,
    "a": ability,
    "d": difficulty,
    "p": proficiency,
    "c": challenge,
    "f": force,
}
