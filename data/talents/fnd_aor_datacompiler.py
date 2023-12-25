import csv
import json

# these are from this google doc: https://docs.google.com/spreadsheets/d/1WUAHDC6rI2cSnry4rRi9gmlIgUxor4DupZOiUnQ_jds/edit#gid=0
files = [("raw_talents_aor.csv", "aor"), ("raw_talents_fnd.csv", "fnd")]


for (talentfile, talentset) in files:
    talents = []
    with open(talentfile, newline="") as csvfile:
        talentsreader = csv.DictReader(csvfile)

        for row in talentsreader:
            talentobj = {
                "name": row["Name"],
                "activation": row["Activation"],
                "ranked": True if row["Ranked"] == "TRUE" else False,
                "trees": row["Trees"].split(", "),
                "description": row["Description"]
            }

            talents.append(talentobj)
        
    with open(f"raw_talents_{talentset}.json", "w") as f:
        json.dump(talents, f, indent=4)

