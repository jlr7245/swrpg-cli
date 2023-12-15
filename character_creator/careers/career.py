import PyInquirer

from ..constants import SkillNames
from ..utils.validated_question import validated_question


class Career:
    def __init__(self, name, career_skills=[]):
        if len(career_skills) != 8:
            raise ValueError("Each career should have 8 skills.")
        self.name = name
        self.career_skills = career_skills

    def _validate_skillchosen_length(self, skills_chooseable, field):
        """validation helper for starting_career_skills"""
        def validator(answer):
            """validator for making sure user has chosen the right number of skills"""
            choice_num = len(answer[field])
            if choice_num < skills_chooseable:
                return f"You need to choose {skills_chooseable - choice_num} more skills, for a total of {skills_chooseable}."
            elif choice_num > skills_chooseable:
                return f"You've chosen too many skills! Please only pick {skills_chooseable}."
            else:
                return True
        return validator

    def starting_career_skills(self, char):
        """Runs when a career is first added to a character to set up free skills"""
        skills_chooseable = 4 if not char.species.starting_career_skill_override \
            else char.species.starting_career_skill_override
        chosen_skills = validated_question(
            [{
                "type": "checkbox", "name": "chosen_skills",
                "message": f"You may choose {skills_chooseable} skills for {char.name}.",
                "choices": [{"name": sk} for sk in self.career_skills],
            }],
            self._validate_skillchosen_length(
                skills_chooseable, "chosen_skills")
        )["chosen_skills"]
        for skill in chosen_skills:
            char.upgrade_skill(skill, is_free=True)
