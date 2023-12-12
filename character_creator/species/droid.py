from .species import Species
# from ..constants import TalentNames


class Droid(Species):
    def __init__(self):
        super().__init__("Droid", starting_xp=175)
        self.implant_cap_override = 6
        self.starting_career_skill_override = 6
        self.starting_specialization_skill_override = 3

    def starting_ranks(self, char):
        # char.add_talent(TalentNames.ENDURANCE)
        pass

    def species_passive(self):
        return """
        - Inorganic: Droids must be repaired with a Mechanics check rather \
            than a medicine check. Emergency repair patches may be used to repair \
            damage, like a stimpack on organic beings.
        - Mechanical Being: Droids cannot become Force sensitive, nor acquire a \
            force rating by any means. Droids cannot use force powers, and also \
            cannot be affected by mind-altering Force powers."""
