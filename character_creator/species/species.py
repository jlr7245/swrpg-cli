from ..constants import Characteristics


def generate_stats_dict(brawn: int, agility: int, intellect: int,
                        cunning: int, willpower: int, presence: int):
    return {
        Characteristics.BRAWN: brawn,
        Characteristics.AGILITY: agility,
        Characteristics.INTELLECT: intellect,
        Characteristics.CUNNING: cunning,
        Characteristics.WILLPOWER: willpower,
        Characteristics.PRESENCE: presence,
    }


class Species:
    def __init__(self, name,
                 stats={e.value: 1 for e in Characteristics},
                 wound_threshold_modifier=10, strain_threshold_modifier=10,
                 starting_xp=90):
        self.name = name
        self.brawn = stats[Characteristics.BRAWN]
        self.agility = stats[Characteristics.AGILITY]
        self.intellect = stats[Characteristics.INTELLECT]
        self.cunning = stats[Characteristics.CUNNING]
        self.willpower = stats[Characteristics.WILLPOWER]
        self.presence = stats[Characteristics.PRESENCE]
        self.wound_threshold_modifier = wound_threshold_modifier
        self.strain_threshold_modifier = strain_threshold_modifier
        self.starting_xp = starting_xp

    def starting_ranks(self):
        pass

    def species_passive(self):
        pass

    def species_bonus_choice(self):
        pass
