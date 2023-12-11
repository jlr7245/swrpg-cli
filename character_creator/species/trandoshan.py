from .species import Species, generate_stats_dict
from ..constants import SkillNames

class Trandoshan(Species):
    def __init__(self):
        super().__init__("Trandoshan", stats=generate_stats_dict(3, 1, 2, 2, 2, 2),
                         wound_threshold_modifier=12, strain_threshold_modifier=9)
        
    def starting_ranks(self, char):
        char.upgrade_skill(SkillNames.PERCEPTION, is_free=True)

    def species_passive(self):
        return """
- Regeneration: Whenever a Trandoshan would recover one or more wounds from natural \
    rest or recuperation in a Bacta tank, they recover one additional wound.
- Claws: When a Trandoshan makes Brawl checks to deal damage to an opponent, they deal \
    +1 damage and have a Critical Rating of 3."""
