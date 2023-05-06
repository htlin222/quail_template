#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# title: index
# date: "2023-05-06"

import yaml
import json

with open('index.yaml', 'r') as f:
    data = yaml.safe_load(f)

output = {}
for item in data:
    sub = item['sub']
    start = int(item['start'])
    end = int(item['end'])
    for i in range(start, end+1):
        output[f'{i:03d}'] = {"0": sub}

with open('index.json', 'w') as f:
    json.dump(output, f, indent=4)
