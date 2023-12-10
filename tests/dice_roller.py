import unittest
from character_creator.utils import dice_roller

class TestDiceRoller(unittest.TestCase):

    def test_dice_roller(self):
        d8_roll = dice_roller.dice_roller(8)
        self.assertIn(d8_roll, range(1,8))

    def test_dice_roller_swrpg(self):
        result = dice_roller.dice_roller_swrpg("3a 2c 1s")
        self.assertTrue(result)
