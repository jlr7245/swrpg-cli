import pickle
import os

def pickle_character(obj, char_name):
    with open(f"data/pickled_characters/{char_name}.pkl", "wb") as file:
        pickle.dump(obj, file)

def unpickle_character(char_name):
    with open(f"data/pickled_characters/{char_name}.pkl", "rb") as file:
        character = pickle.load(file)
        return character
