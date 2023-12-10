from ....utils.super_enum import SuperEnum

class TalentNames(SuperEnum):
    # Edge of the Empire
    ADVERSARY = "Adversary"
    ANATOMY_LESSONS = "Anatomy Lessons"
    ARMOR_MASTER = "Armor Master"

class TalentAct(SuperEnum):
    PASSIVE = "Passive"
    ACT_I = "Active (Incidental)"
    ACT_A = "Active (Action)"
    ACT_M = "Active (Maneuver)"
    ACT_IO = "Active (Incidental, Out of Turn)"

