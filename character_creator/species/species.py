from ..constants import Abilities


def generate_stats_dict(brawn: int, agility: int, intellect: int,
                        cunning: int, willpower: int, presence: int):
    return {
        Abilities.BRAWN.value: brawn,
        Abilities.AGILITY.value: agility,
        Abilities.INTELLECT.value: intellect,
        Abilities.CUNNING.value: cunning,
        Abilities.WILLPOWER.value: willpower,
        Abilities.PRESENCE.value: presence,
    }


class Species:
    def __init__(self, name,
                 stats={e.value: 1 for e in Abilities},
                 wound_threshold_modifier=10, strain_threshold_modifier=10,
                 starting_xp=90):
        self.name = name
        self.brawn = stats[Abilities.BRAWN.value]
        self.agility = stats[Abilities.AGILITY.value]
        self.intellect = stats[Abilities.INTELLECT.value]
        self.cunning = stats[Abilities.CUNNING.value]
        self.willpower = stats[Abilities.WILLPOWER.value]
        self.presence = stats[Abilities.PRESENCE.value]
        self.wound_threshold_modifier = wound_threshold_modifier
        self.strain_threshold_modifier = strain_threshold_modifier
        self.starting_xp = starting_xp

        self.starting_career_skill_override = None
        self.implant_cap_override = None
        self.starting_specialization_skill_override = None

    def starting_ranks(self, char):
        pass

    def species_passive(self):
        pass

    def species_bonus_choice(self, char):
        pass
