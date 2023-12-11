from .species import Species, generate_stats_dict

class Human(Species):
    def __init__(self):
        super().__init__("Human", stats=generate_stats_dict(2, 2, 2, 2, 2, 2),
                         starting_xp=90)
        self.starting_noncareer_skills_override = 2
