from ..constants import SkillNames
from .species import Species, generate_stats_dict

class Bothan(Species):
    def __init__(self):
        super().__init__("Bothan",
                         stats=generate_stats_dict(1, 2, 2, 3, 2, 2),
                         wound_threshold_modifier=10, strain_threshold_modifier=10,
                         starting_xp=100)

    def starting_ranks(self, char):
        char.upgrade_skill(SkillNames.STREETWISE, is_free=True)
        # char.add_talent(TalentName.CONVINCING_DEMEANOR, is_free=True)
