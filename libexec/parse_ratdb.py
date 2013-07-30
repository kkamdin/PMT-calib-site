#!/usr/bin/python
import yaml
import argparse
import sys
import os
import imp

eca = imp.load_source('*', 'lib/eca_constants.py')

# Handle the command line arguments
ap = argparse.ArgumentParser(description='Parse a ratdb file')
ap.add_argument('-p', '--pythonsrc',
                help="write a python source file to the path PYTHONSRC")
#ap.add_argument('-w', '--timewalkpath',
#                help="write a time walk channel status file to TIMEWALKPATH")
#ap.add_argument('-f', '--gainfitpath',
#               help="write a gain fit channel status file to GAINFITPATH")
#ap.add_argument('-g', '--generalpath',
#                help="write a general run status file to GENERALPATH")
ap.add_argument('file', help='the ratdb file to parse')
args = ap.parse_args()

if not (args.pythonsrc):
    ap.error("No output specified for ratdb to py file transformation")

# Conveniently, ratdb files *seem* to be yaml-compatible (except the comments)
raw_data = [line.split('//', 1)[0] for line in file(args.file).readlines()]
data = yaml.safe_load("".join(raw_data))

# Write the output files, first the python file
if args.pythonsrc:
    with file(args.pythonsrc, 'w') as out:
        out.write("#!/usr/bin/python\n\ndata = ")
        out.write(str(data))
        out.write("\n\n")


# The channel status files are all similarly generated
#this is the human-readable part that is just for fun
#def report_status_flags(status_list, list_type, output_file):
#    with file(output_file, 'w') as out:
#        if type(status_list) is not list:
#            # This happens when there is only one status word
#            status_list = [status_list]
#
#        for channel_number, status in enumerate(status_list):
#            if status is 0:
#                out.write("{}: OK\n".format(channel_number))
#            else:
#                channel_flags = [pca.flags[list_type][flag_bit]['name']
#                                 for flag_bit in xrange(1, 31)
#                                 if status & 2**flag_bit]
#                out.write("{}: {}\n".format(channel_number,
#                                            ",".join(channel_flags)))
#
#
#types = [(args.gainfitpath, 'PCAGF_status', 'gf'),
#         (args.timewalkpath, 'PCATW_status', 'tw'),
#         (args.generalpath, 'PCA_gen_status', 'general')]
#
#for output_name, status_key, mode in types:
#    if output_name:
#        if status_key in data:
#            report_status_flags(data[status_key], mode, output_name)
#        else:
#            sys.stderr.write("WARNING: No {} data found".format(status_key))
