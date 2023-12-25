import requests
from bs4 import BeautifulSoup
import json

page = requests.get("https://sw-eote-srd.vercel.app/talents")

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text

all_h4s = soup.select("h4")
talent_titles = all_h4s[4:]

list_blocks = soup.select("h4 ~ div ul")
talent_blocks = list(
    filter(lambda talent: "Activation: " in talent.text, list_blocks[3:]))
print(len(talent_titles), len(talent_blocks))

parsed_talents = []
for i, talent in enumerate(talent_titles):

    new_talent = {
        "name": talent.text,
        "i": i,
        # "description": description,
        # "ranked": ranked,
        # "trees": trees,
        # "activation": activation,
    }

    info = talent_blocks[i]
    for i, child in enumerate(info.children):
        if "Activation: " in child.text:
            activation = child.text.split("Activation: ")[1]
            new_talent["activation"] = activation
        elif "Ranked: " in child.text:
            ranked = child.text.split("Ranked: ")[1]
            new_talent["ranked"] = True if ranked == "Yes" else False
        elif "Trees: " in child.text:
            trees = child.text.split("Trees: ")[1]
            if trees == "(all)":
                trees = "Assassin, Bodyguard, Doctor, Force Sensitive Exile, Fringer, Gadgeteer, Marauder, Mechanic, Outlaw Tech, Pilot, Politico, Scholar, Scoundrel, Scout, Slicer, Mercenary Soldier, Survivalist, Thief, Trader"
            new_talent["trees"] = trees.split(',').strip()
        elif i == 7:
            new_talent["description"] = child.text.strip()

    parsed_talents.append(new_talent)

with open("talents_dump.json", "w") as f:
    json.dump(parsed_talents, f, indent=4)
