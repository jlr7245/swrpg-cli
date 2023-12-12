import unittest

from character_creator.careers.career import Career
from character_creator.character import Character
from character_creator.species import Human, Droid
from character_creator.constants import SkillNames


class TestCareer(unittest.TestCase):

    def test_career__starting_skills(self):
        beau = Character("beauregard", Human())
        r2d2 = Character("beauregard", Droid())

        empty_career = Career("any",
                              [SkillNames.ATHLETICS, SkillNames.BRAWL, SkillNames.PERCEPTION, 
                               SkillNames.PILOTING_PLANETARY, SkillNames.PILOTING_SPACE, 
                               SkillNames.RANGED_HEAVY, SkillNames.STREETWISE, SkillNames.VIGILANCE])
        
        empty_career.starting_career_skills(beau)
        empty_career.starting_career_skills(r2d2)


if __name__ == '__main__':
    unittest.main()
