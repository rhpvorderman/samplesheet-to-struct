#!/usr/bin/env python3

import yaml
import json


def nested_dicts_to_lists(dictionary):
    new_dict = dict()
    for key, value in dictionary.items():
        if type(value) == dict:
            new_dict[key] = dict_to_item_list_with_id(value)
        else:
            new_dict[key] = value
    return new_dict


def dict_to_item_list_with_id(dictionary):
    items = []
    for sub_key, sub_dictionary in dictionary.items():
        item_dict = dict(id=sub_key, **nested_dicts_to_lists(sub_dictionary))
        items.append(item_dict)
    return items


with open("samples.example.yml", "r") as samplesheet:
    samplesheet_dict = yaml.load(samplesheet)

sample_struct = nested_dicts_to_lists(samplesheet_dict)

with open("output.json", "w") as output_json:
    output_json.write(json.dumps(sample_struct))
