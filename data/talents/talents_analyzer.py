import json

source_names = ("eote", "aor", "fnd")

talents_dict = {}
trees = set()
talent_set = set()

for source in source_names:
    with open(f"raw_talents_{source}.json", "r") as f:
        talentlist = json.load(f)
        for talent in talentlist:
            name = talent["name"]
            talent_set.add(name)
            talent["source"] = source
            if name in talents_dict:
                talents_dict[name].append(talent)
            else:
                talents_dict[name] = [talent]
            for tree in talent["trees"]:
                trees.add(tree)


canonical_talents_list = []

for name, talents in talents_dict.items():
    talent_trees = set()
    desc = ""

    for talent in talents:
        if bool(talent["description"]):
            desc = talent["description"]
        talent_trees = talent_trees.union(talent["trees"])

    canonical_talents_list.append({
        "name": name,
        "activation": talents[0]["activation"],
        "ranked": talents[0]["ranked"],
        "trees": list(talent_trees),
        "description": desc,
    })

######## FILE WRITERS ##########

    
"""Generates a checklist of duplicated talents (for source checking purposes)"""
# with open("todolist_dump.txt", "w") as f:
#     duplicate_talents = []
#     for name, talents in talents_dict.items():
#         if len(talents) > 1:
#             sources = list(map(lambda x: x["source"], talents))
#             duplicate_talents.append(f"{name} ({', '.join(sources)})")

#     talents_todolist = ""
#     for talent in duplicate_talents:
#         talents_todolist += f"- [ ] {talent}\n"

#     f.write(talents_todolist)



"""Generates a JSON list of all talents"""
with open("canonical_talents.json", "w") as f:
    json.dump(canonical_talents_list, f, indent=4)


"""Generates a lookup json object with talent names as keys"""
with open("canonical_talents_lookup.json", "w") as f:
    talent_lookup = {}
    for talent in sorted(canonical_talents_list, key=lambda x: x["name"]):
        talent_lookup[talent["name"]] = talent

    json.dump(talent_lookup, f, indent=4)


"""Generates a TalentNames class txt file"""
# with open("talentnames_dump.txt", "w") as f:
#     talentnames = "class TalentNames:\n"

#     for talent in sorted(canonical_talents_list, key=lambda x: x["name"]):
#         talent_name_var = "_".join(talent["name"].upper().split(' '))
#         talent_name_var = "".join(
#             filter(lambda x: x not in "()'!", talent_name_var))
#         talent_name_var = talent_name_var.replace('-', '_')
#         talentnames += f'    {talent_name_var} = "{talent["name"]}"\n'

#     f.write(talentnames)

"""Generates a TreeNames class txt file"""
# with open("treenames_dump.txt", "w") as f:
#     treenames = "class TreeNames:\n"

#     for tree in sorted(list(trees)):
#         tree_name = "_".join(tree.upper().split(' ')).replace('-', '_')
#         treenames += f'    {tree_name} = "{tree}"\n'

#     f.write(treenames)
