import unittest
from character_creator.utils import dice_roller

class TestDiceRoller(unittest.TestCase):

    def test_dice_roller(self):
        d8_roll = dice_roller.dice_roller(8)
        self.assertIn(d8_roll, range(1,8))

    def test_dice_roller_swrpg(self):
        result = dice_roller.dice_roller_swrpg("2b 3c 1a 2d 1p 1c 2f")
        print(result)
        self.assertIsInstance(result, str)

    def test_dice_roller_swrpg__invalid_input(self):
        with self.assertRaises(ValueError) as context1:
            dice_roller.dice_roller_swrpg("2b 4n")
        with self.assertRaises(ValueError) as context2:
            dice_roller.dice_roller_swrpg("1j 9f")
        self.assertTrue("n not a valid" in str(context1.exception))
        self.assertTrue("j not a valid" in str(context2.exception))

if __name__ == '__main__':
    unittest.main()
