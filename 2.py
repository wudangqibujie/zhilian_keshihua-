import json
with open("data.json","r",encoding="utf-8") as f:
    load_dict = json.load(f)
    print(load_dict)
