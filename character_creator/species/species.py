from ..constants import Abilities


def generate_stats_dict(brawn: int, agility: int, intellect: int,
                        cunning: int, willpower: int, presence: int):
    return {
        Abilities.BRAWN: brawn,
        Abilities.AGILITY: agility,
        Abilities.INTELLECT: intellect,
        Abilities.CUNNING: cunning,
        Abilities.WILLPOWER: willpower,
        Abilities.PRESENCE: presence,
    }


class Species:
    def __init__(self, name,
                 stats={e.value: 1 for e in Abilities},
                 wound_threshold_modifier=10, strain_threshold_modifier=10,
                 starting_xp=90):
        self.name = name
        self.brawn = stats[Abilities.BRAWN]
        self.agility = stats[Abilities.AGILITY]
        self.intellect = stats[Abilities.INTELLECT]
        self.cunning = stats[Abilities.CUNNING]
        self.willpower = stats[Abilities.WILLPOWER]
        self.presence = stats[Abilities.PRESENCE]
        self.wound_threshold_modifier = wound_threshold_modifier
        self.strain_threshold_modifier = strain_threshold_modifier
        self.starting_xp = starting_xp

    def starting_ranks(self, char):
        pass

    def species_passive(self):
        pass

    def species_bonus_choice(self, char):
        pass
