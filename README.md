# SWRPG CLI

Project for me, a person who wanted to build something complex in python.

### Running it

- You should have Python3 and pip installed on your machine.
- Start up a virtual environment: `python -m venv venv` and `source venv/bin/activate`
- Install requirements: `pip install -r requirements.txt`
- Run the program: `python interface.py`

> You may run into an error along the lines of `Cannot import name "Mapping" from "collections"`. As per [this stackoverflow post](https://stackoverflow.com/questions/71595728/pip-importerror-cannot-import-name-mapping-from-collections), the solution here is to go into `path/to/venv/lib/python3.11/site-packages/prompt_toolkit/styles/from_dict.py` and change ln 9 from `from collections import Mapping` to `from collections.abc import Mapping`. 


## Character Creator

Coming soon!

## Dice Roller

Star Wars RPG has a fairly unique dice system:

![Diagram of SWRPG dice](https://static.wikia.nocookie.net/star-wars-rpg-ffg/images/a/a8/FFG-StarWarsRPG_DICE%2BGUIDE.jpg/revision/latest/scale-to-width-down/1000?cb=20181218073231)

The CLI dice roller allows you to input the number and type of dice you'd like to use. For example, a roll with two Ability dice, one Proficiency die, two Challenge dice, and one Boost die would be formatted as `2a 1p 2c 1b`.
