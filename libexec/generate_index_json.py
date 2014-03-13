#!/usr/bin/python
'''
Takes the runs in data/runXXXX and makes an index.json that lists the run numer, whether its pdst or tslp, etc.
This index.json file is what is used to make the run table on the website.
'''

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

    pdst_found = False
    tslp_found = False

    for f in os.listdir(search_dir):
        filename = str(f)
        isPDST = 'PDST_' in filename
        isTSLP = 'TSLP_' in filename
        if(isPDST):
            #print filename
            rat_path = os.path.sep.join([search_dir, f]) #full path to pdst ratdb file
            pdst_found = True
        elif(isTSLP):
            #print filename
            rat_path = os.path.sep.join([search_dir, f]) #full path to tslp ratdb file
            tslp_found = True
        if not isPDST | isTSLP:
            continue
    pdst_bool = pdst_found
    tslp_bool = tslp_found
    #print 'pdst', pdst_bool, 'tslp', tslp_bool

    #i'm going to make the plots without translating .ratdb to yaml because it takes FOREVER
##########################
#    if os.path.exists(os.path.sep.join([search_dir, 'pdst_cache.py'])): 
#        rat_path = os.path.sep.join([search_dir, 'pdst_cache.py']) #full path to pdst cache.py file
#        pdst_bool = True
#    elif os.path.exists(os.path.sep.join([search_dir, 'tslp_cache.py'])):
#        rat_path = os.path.sep.join([search_dir, 'tslp_cache.py']) #full path to tslp cache.py file
#        tslp_bool = True
#    if not os.path.isfile(rat_path):
#        #print "Skipping {}".format(search_dir)
#        continue
#########################
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
