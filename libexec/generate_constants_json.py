#!/usr/bin/python

import json
import imp

pca = imp.load_source('*', 'lib/pca_constants.py')

pca_items = {}
for k,v in pca.__dict__.items():
    if k[0] is not "_":
        pca_items[k] = v

print json.dumps(pca_items, indent=4)
