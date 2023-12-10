from ..constants import Characteristics, SkillNames

class Bothan:
    def __init__(self):
        self[Characteristics.BRAWN] = 1
        self[Characteristics.AGILITY] = 2
        self[Characteristics.INTELLECT] = 2
        self[Characteristics.CUNNING] = 3
        self[Characteristics.WILLPOWER] = 2
        self[Characteristics.PRESENCE] = 2
        self.wound_threshold_modifier = 10
        self.strain_threshold_modifier = 11
        self.starting_experience = 100

    def starting_ranks(self, char):
        char.upgrade_skill(SkillNames.STREETWISE)
        # char.add_talent(TalentName.CONVINCING_DEMEANOR)
