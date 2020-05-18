import os
import json


def change_name(json_name):
    with open(json_name, 'r') as f:
        anns = json.load(f)

        class_names = anns['categories']
        phone = class_names[1]
        phone['name'] = 'cellphone'

    with open(json_name, 'w') as f:
        json.dump(anns, f)


if __name__ == "__main__":
    jsons = ['jd.json', 'train.json', 'val.json', 'test.json']
    for json_name in jsons:
        change_name(json_name)
