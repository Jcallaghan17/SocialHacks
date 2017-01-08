import json


def organize():
    buildings = {}
    with open("nyu_building_db.json", 'r') as db:
        b_dict = json.load(db)
        for entry in b_dict:
            buildings[entry["name"]] = {"address": entry["address"],
                                        "lat": entry["coordinates"]["lat"],
                                        "long": entry["coordinates"]["lng"]}
    with open("better_building_db.json", "w") as js:
        json.dump(buildings, js)

organize()
