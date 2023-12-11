from .species import Species, generate_stats_dict
from ..constants import SkillNames

class Rodian(Species):
    def __init__(self):
        super.__init__("Rodian", stats=generate_stats_dict(2, 3, 2, 2, 1, 2),
                       starting_xp=100)
        
    def starting_ranks(self, char):
        char.upgrade_skill(SkillNames.SURVIVAL)
        # char.add_talent(TalentNames.EXPERT_TRACKER)
