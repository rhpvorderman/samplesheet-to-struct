#!/usr/bin/env python3

import yaml
import json



def dict_of_dicts_to_list_of_dicts(dictionary):



with open("samples.example.yml", "r") as samplesheet:
    samplesheet_dict = yaml.load(samplesheet)["samples"]
    print(deconstruct_dict(yaml.load(samplesheet)))
samples = []

for sample in samplesheet_dict.items():
    print sample
    sample_dict = dict(id=sample[0])
    for samplekeys in sample[1].items():
        sample_dict[samplekeys[0]] = []
        for librarykeys in samplekeys[1].items():
            library_dict = dict(id=librarykeys[0])
            for library in librarykeys[1].items():
                library_dict[library[0]] = []
                for readgroupkeys in library[1].items():
                    readgroup_dict = dict(id=readgroupkeys[0], **readgroupkeys[1])
                    library_dict[library[0]].append(readgroup_dict)
            sample_dict[samplekeys[0]].append(library_dict)
    samples.append(sample_dict)

with open("output.json", "w") as output_file:
    output_file.write((json.dumps(samples)))