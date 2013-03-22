#!/usr/bin/python

from __future__ import division
from PIL import Image
import argparse
import os
import sys
import math
import imp

pca = imp.load_source('*', 'lib/pca_constants.py')

def color_add(c1, c2):
    #return tuple([min(c1[x] + c2[x], 255) for x in range(0, len(c1))])
    return (min(c1[0] + c2[0], 255),
            min(c1[1] + c2[1], 255),
            min(c1[2] + c2[2], 255))


def chunks(input, chunksize):
    """ Yield successive n-sized chunks from input.
    From http://stackoverflow.com/questions/312443
    """
    for i in xrange(0, len(input), chunksize):
        yield input[i:i+chunksize]


def scaled_bitmap(pixels, original_width, scale):
    scaled_px = []
    for row in chunks(pixels, original_width):
        scaled_row = []
        for p in row:
            scaled_row.extend([p] * scale)
        scaled_px.extend(scaled_row * scale)
    return scaled_px


def process_statuses(statuses, flags, colors, target_flag=None):
    pixels = []
    if target_flag is None:
        for idx, status in enumerate(statuses):
            if status is 0:
                pixels.append((255, 255, 255))
            else:
                pixel_components = [colors[flags[bit]['type']]
                                    for bit in xrange(1, 31)
                                    if status & 2**bit]
                pixels.append(reduce(color_add, pixel_components))
    else:
        bit = target_flag['bit']
        for idx, status in enumerate(statuses):
            if status is 0 or not status & 2**bit:
                pixels.append((255, 255, 255))
            else:
                pixels.append(colors[target_flag['type']])
    return pixels


def generate_image(pixel_data, filename, scale=1):
    channel_width = 1
    channel_height = 1
    card_width = channel_width * 32
    card_height = channel_height
    crate_width = card_width * scale
    crate_height = card_height * 16 * scale
    crate_count = 19
    columns = 5
    rows = int(math.ceil(crate_count/columns))
    margin = 1
    bg_color = (0, 0, 0)
    image_width = (crate_width * columns) + ((columns + 1) * margin)
    image_height = (crate_height * rows) + ((rows + 1) * margin)
    main_image = Image.new("RGB", (image_width, image_height), bg_color)
    pixel_chunks = chunks(pixel_data, 512)  # 512 chan/crate
    for crate_num in range(crate_count):
        crate_image = Image.new("RGB", (crate_width, crate_height), bg_color)
        if scale == 1:
            crate_image.putdata(pixel_chunks.next())
        else:
            crate_image.putdata(scaled_bitmap(pixel_chunks.next(), card_width,
                                              scale))
        ypos, xpos = divmod(crate_num, columns)
        x = margin + (margin * xpos) + (crate_width * xpos)
        y = margin + (margin * ypos) + (crate_height * ypos)
        main_image.paste(crate_image, (x, y))
    main_image.save(filename)


if __name__ == '__main__':
    argp = argparse.ArgumentParser(
        description='Generate channel flag status images')
    argp.add_argument('-d', '--directory',
                      help='the directory in which to create the output files')
    argp.add_argument('-s', '--scale', type=int, default=1,
                      help='the factor by which to scale up the output image')
    # argp.add_argument('-j', '--json', action='store_true',
    #     help='generate json files in addition to images')
    mode_group = argp.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('-w', '--timewalk',
                            help='use the time walk channel data')
    mode_group.add_argument('-f', '--gainfit',
                            help='use the gain fit channel data')


    args = argp.parse_args()

    if args.timewalk:
        rat = imp.load_source('__main__', args.timewalk)
        statuses = rat.data['PCATW_status']
        mode = 'tw'
    elif args.gainfit:
        rat = imp.load_source('__main__', args.gainfit)
        statuses = rat.data['PCAGF_status']
        mode = 'gf'
    else:
        raise ValueError("Unknown mode of operation")

    if args.directory:
        # This causes the output files to be written in the right place
        os.chdir(args.directory)

    # Summary Image
    generate_image(process_statuses(statuses, pca.flags[mode], pca.colors),
                   filename="{}-allflags.bmp".format(mode),
                   scale=args.scale)

    # Flag-specific images
    for bit, flag in enumerate(pca.flags[mode]):
        pixels = process_statuses(statuses, pca.flags[mode], pca.colors,
                                  target_flag=flag)
        generate_image(pixels,
                       filename="{}-flag-{:02d}.bmp".format(mode, bit),
                       scale=args.scale)
