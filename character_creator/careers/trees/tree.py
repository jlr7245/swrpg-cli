class Tree:
    tree = {1: {1: None, 2: None, 3: None, 4: None},
            2: {1: None, 2: None, 3: None, 4: None},
            3: {1: None, 2: None, 3: None, 4: None},
            4: {1: None, 2: None, 3: None, 4: None},
            5: {1: None, 2: None, 3: None, 4: None}}

    def __init__(self, name):
        self.name = name

    def progress(self):
        # something about checking what's been unlocked
        # and then spitting out all the applicable upgrades
        pass
