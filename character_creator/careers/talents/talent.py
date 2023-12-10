class TalentSet:
    def __init__(self):
        self.talents = []

    def add_talent(self, talent):
        self.talents.append(talent)
        self[talent.name] = talent
