import PyInquirer

from ..constants import SkillNames


class Career:
    def __init__(self, name, career_skills=[]):
        if len(career_skills) != 8:
            raise ValueError("Each career should have 8 skills.")
        self.name = name
        self.career_skills = career_skills

    def validate_skillchosen_length(self, skills_chooseable):
        print("making_validator")
        def validator(answer):
            print("vaildating")
            print(answer)
            choice_num = len(answer)
            if choice_num < skills_chooseable:
                return f"You need to choose {skills_chooseable - choice_num} more skills, for a total of {skills_chooseable}."
            elif choice_num > skills_chooseable:
                return f"You've chosen too many skills! Please only pick {skills_chooseable}."
            else:
                return True
        return validator

    def starting_career_skills(self, char):
        skills_chooseable = 4 if not char.species.starting_career_skill_override \
            else char.species.starting_career_skill_override
        chosen_skills = PyInquirer.prompt([{
            "type": "checkbox", "name": "chosen_skills",
            "message": f"You may choose {skills_chooseable} skills for {char.name}.",
            "choices": [{"name": sk} for sk in self.career_skills],
            "validate": self.validate_skillchosen_length(skills_chooseable)
        }])["chosen_skills"]
        print(chosen_skills)
