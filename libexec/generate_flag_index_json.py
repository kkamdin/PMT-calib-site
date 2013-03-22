#!/usr/bin/python

import argparse
import os
import sys
import imp
import json

pca = imp.load_source('*', 'lib/pca_constants.py')

if __name__ == '__main__':
    argp = argparse.ArgumentParser(
        description='Generate a flag index json file')
    argp.add_argument('-d', '--directory',
                      help='the directory in which to create the output files')
    mode_group = argp.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('-w', '--timewalk',
                            help='use the time walk channel data')
    mode_group.add_argument('-f', '--gainfit',
                            help='use the gain fit channel data')


    args = argp.parse_args()

    if args.timewalk:
        rat = imp.load_source('*', args.timewalk)
        statuses = rat.data['PCATW_status']
        mode = 'tw'
    elif args.gainfit:
        rat = imp.load_source('*', args.gainfit)
        statuses = rat.data['PCAGF_status']
        mode = 'gf'
    else:
        raise ValueError("Unknown mode of operation")

    if args.directory:
        # This causes the output files to be written in the right place
        os.chdir(args.directory)

    # fixme: so tired right now
    flag_channel_index = []
    for bit, flag in enumerate(pca.flags[mode]):
        lcns = [lcn for lcn, status in enumerate(statuses) if status & 2**bit]
        flag_channel_index.append(lcns)
    print json.dumps(flag_channel_index)
