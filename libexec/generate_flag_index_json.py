#!/usr/bin/python

import argparse
import os
import sys
import imp
import json

eca = imp.load_source('*', 'lib/eca_constants.py')

if __name__ == '__main__':
    argp = argparse.ArgumentParser(
        description='Generate a flag index json file')
    argp.add_argument('-d', '--directory',
                      help='the directory in which to create the output files')
    mode_group = argp.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('-w', '--tslp',
                            help='use the tslope channel data')
    mode_group.add_argument('-f', '--pdst',
                            help='use the pedestal channel data')


    args = argp.parse_args()

    if args.tslp:
        rat = imp.load_source('*', args.tslp)
        statuses = rat.data['tslp_status']
        mode = 'tw'
    elif args.pdst:
        rat = imp.load_source('*', args.pdst)
        statuses = rat.data['pdst_status']
        mode = 'gf'
    else:
        raise ValueError("Unknown mode of operation")

    if args.directory:
        # This causes the output files to be written in the right place
        os.chdir(args.directory)

    # fixme: so tired right now
    flag_channel_index = []
    for bit, flag in enumerate(eca.flags[mode]):
        lcns = [lcn for lcn, status in enumerate(statuses) if status & 2**bit]
        flag_channel_index.append(lcns)
    print json.dumps(flag_channel_index)
