#!/usr/bin/python

import json
import imp
import argparse
import os

pca = imp.load_source('*', 'lib/pca_constants.py')

argp = argparse.ArgumentParser(description='Generate a runlist json file')
argp.add_argument('datadirs', help='Run directories to include in the index',
                  nargs="+")
args = argp.parse_args()

index = []

for raw_search_dir in args.datadirs:
    search_dir = os.path.normpath(raw_search_dir)
    dir_name = os.path.split(search_dir)[-1]

    rat_path = os.path.sep.join([search_dir, 'general_cache.py'])
    if not os.path.isfile(rat_path):
        #print "Skipping {}".format(search_dir)
        continue

    rat = imp.load_source('*', rat_path)
    rat_date = str(rat.data['PCA_date'])

    index.append({
        'date': "{}-{}-{}".format(rat_date[0:4], rat_date[4:6], rat_date[6:8]),
        'timewalk_pass': bool(rat.data['PCA_gen_status'] & 2**1),
        'gainfit_pass': bool(rat.data['PCA_gen_status'] & 2**2),
        'rat_available': bool(os.path.isfile(os.path.sep.join([search_dir, 'IN_RAT']))),
        'run_name': dir_name})

print json.dumps(index, indent=4)

# PCA_gen_limits
# PCA_runnumber
# PCA_GF_limits
# valid_begin
# name
# PCA_TW_limits
# PCA_date
# PCA_gen_status
# valid_end


# [
#   {
#     "date": "2014-09-19", 
#     "timewalk_pass": false, 
#     "gainfit_pass": false, 
#     "rat_available": false, 
#     "run_name": "run100000-2"
#   }, 
