from .species import Species, generate_stats_dict
from ..constants import SkillNames

class Wookiee(Species):
    def __init__(self):
        super().__init__("Wookiee", stats=generate_stats_dict(3, 2, 2, 2, 1, 2),
                         wound_threshold_modifier=14, strain_threshold_modifier=8)
        
    def starting_ranks(self, char):
        char.upgrade_skill(SkillNames.BRAWL, is_free=True)

    def species_passive(self):
        return """
- Wookiee Rage: When a Wookiee has suffered any wounds, they deal +1 damage to \
    Brawl and Melee attacks. When a Wookiee is Critically Injured, they instead \
    deal +2 damage to Brawl and Melee attacks."""
