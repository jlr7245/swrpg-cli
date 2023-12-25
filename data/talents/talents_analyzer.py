import json

source_names = ("eote", "aor", "fnd")

talents_dict = {}
trees = set()

for source in source_names:
    with open(f"raw_talents_{source}.json", "r") as f:
        talentlist = json.load(f)
        for talent in talentlist:
            name = talent["name"]
            talent["source"] = source
            if name in talents_dict:
                talents_dict[name].append(talent)
            else:
                talents_dict[name] = [talent]
            for tree in talent["trees"]:
                trees.add(tree)

duplicate_talents = []
for name, talents in talents_dict.items():
    if len(talents) > 1:
        sources = list(map(lambda x: x["source"], talents))
        duplicate_talents.append(f"{name} ({', '.join(sources)})")

print(trees)
print(duplicate_talents)

talents_todolist = ""
for talent in duplicate_talents:
    talents_todolist += f"- [ ] {talent}\n"

with open("todolist_dump.txt", "w") as f:
    f.write(talents_todolist)

