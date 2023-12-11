import PyInquirer

from .species import Species, generate_stats_dict
from ..constants import SkillNames

class Gand(Species):
    def __init__(self):
        super().__init__("Gand",
                         stats=generate_stats_dict(2, 2, 2, 2, 3, 1),
                         starting_xp=100)
        
    def starting_ranks(self, char):
        char.upgrade_skill(SkillNames.DISCIPLINE, is_free=True)

    def species_bonus_choice(self, char):
        has_lungs = PyInquirer.prompt([{
            "type": "list", "name": "has_lungs",
            "message": "Gands have two subspecies: one with lungs and one without. Which are you?",
            "choices": [
                "Without lungs (immune to suffocation)",
                "With lungs (gain an ammonia respirator; oxygen atmospheres are Rating 8 for you; +10 XP)"]
        }])["has_lungs"]
        if not "Without" in has_lungs:
            self.starting_xp += 10
            char.add_equipment("Ammonia respirator")

