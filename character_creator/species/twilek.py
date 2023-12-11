import PyInquirer

from .species import Species, generate_stats_dict
from ..constants import SkillNames

class Twilek(Species):
    def __init__(self):
        super().__init__("Twi'lek", stats=generate_stats_dict(1, 2, 2, 2, 2, 3),
                         strain_threshold_modifier=11,
                         starting_xp=100)
        
    def species_passive(self):
        return """
- Desert Acclimatization: When making skill checks, Twi'leks may remove Setback dice \
    imposed due to arid or hot environmental conditions."""
    
    def species_bonus_choice(self, char):
        bonus_skill = PyInquirer.prompt([{
            "type": "list", "name": "bonus_skill",
            "message": "As a Twi'lek, you gain a rank in either Skill or Deception.",
            "choices": [SkillNames.CHARM, SkillNames.DECEPTION]
        }])["bonus_skill"]
        char.upgrade_skill(bonus_skill, is_free=True)
