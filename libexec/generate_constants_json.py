#!/usr/bin/python

import json
import imp

eca = imp.load_source('*', 'lib/eca_constants.py')

eca_items = {}
for k,v in eca.__dict__.items():
    if k[0] is not "_":
        eca_items[k] = v

print json.dumps(eca_items, indent=4)
