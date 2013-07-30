#!/usr/bin/python

import json
import imp
import argparse
import os

eca = imp.load_source('*', 'lib/eca_constants.py')

argp = argparse.ArgumentParser(description='Generate a runlist json file')
argp.add_argument('datadirs', help='Run directories to include in the index',
                  nargs="+")
args = argp.parse_args()

index = []

pdst_bool = False
tslp_bool = False

for raw_search_dir in args.datadirs: #loop over data directories, runXXXXX
    search_dir = os.path.normpath(raw_search_dir)
    dir_name = os.path.split(search_dir)[-1]

    if os.path.exists(os.path.sep.join([search_dir, 'pdst_cache.py'])): 
        rat_path = os.path.sep.join([search_dir, 'pdst_cache.py']) #full path to pdst cache.py file
        pdst_bool = True
    elif os.path.exists(os.path.sep.join([search_dir, 'tslp_cache.py'])):
        rat_path = os.path.sep.join([search_dir, 'tslp_cache.py']) #full path to tslp cache.py file
        tslp_bool = True
    if not os.path.isfile(rat_path):
        #print "Skipping {}".format(search_dir)
        continue

    #rat = imp.load_source('*', rat_path)
    #rat_date = str(rat.data['PDST_date'])

    index.append({
        #'date': "{}-{}-{}".format(rat_date[0:4], rat_date[4:6], rat_date[6:8]),
        'date': dir_name,
        'pdst_pass': pdst_bool,
        'tslp_pass': tslp_bool,
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
