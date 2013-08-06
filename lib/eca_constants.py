#!/usr/bin/python

# So the creation of this file has been a manual process. I've used my text editor (sublime text 2)
# I've been using this search:
# ^.+?\[(\d+)\]\s+?\=\s+\"(.+?)\";\s*(\/\/\s*(.+)\s*)?$
# and this replace:
# {'bit': $1, 'name': "$2", 'doc': "$4", 'type': 'info'},

status_word_count = 9728

colors = {'info':  (0,0,0), # black
          'fail':  (255,0,0), # red
          'warn1': (255,128,0), # orange
          'warn2': (64,0,128), # purple
          'warn3': (0,0,255)} # blue

# order and blanks are important!
flags = {
    'pdst': [
        {'bit': 0, 'name': "cell status PDST", 'doc': "OR of bits 1-14", 'type': 'info'},
        {'bit': 1, 'name': "cell QHS status", 'doc': "QHS ped outside limits", 'type': 'info'},
        {'bit': 2, 'name': "cell QHS width", 'doc': "width > upper limit", 'type': 'info'},
        {'bit': 3, 'name': "cell QHS stable", 'doc': "differebce from previous run > upper limit", 'type': 'info'},
        {'bit': 4, 'name': "cell QHL status", 'doc': "QHL ped outside limits", 'type': 'info'},
        {'bit': 5, 'name': "cell QHL width", 'doc': "width > upper limit", 'type': 'info'},
        {'bit': 6, 'name': "cell QHL stable", 'doc': "differebce from previous run > upper limit", 'type': 'info'},
        {'bit': 7, 'name': "cell QLX status", 'doc': "QHX ped outside limits", 'type': 'info'},
        {'bit': 8, 'name': "cell QLX width", 'doc': "width > upper limit", 'type': 'info'},
        {'bit': 9, 'name': "cell QLX stable", 'doc': "differebce from previous run > upper limit", 'type': 'info'},
        {'bit': 10, 'name': "cell TAC status", 'doc': "TAC ped outside limits", 'type': 'info'},
        {'bit': 11, 'name': "cell TAC width", 'doc': "width > upper limit", 'type': 'info'},
        {'bit': 12, 'name': "cell TAC stable", 'doc': "differebce from previous run > upper limit", 'type': 'info'},
        {'bit': 13, 'name': "cell insufficent events", 'doc': "fewer than 10 events on this cell", 'type': 'info'},
        {'bit': 14, 'name': "cell no events", 'doc': "0 events on this cell", 'type': 'fail'},
        {'bit': 15, 'name': "channel status", 'doc': "OR of bits 16-27", 'type': 'info'},
        {'bit': 16, 'name': "MB ID check", 'doc': "", 'type': 'info'},
        {'bit': 17, 'name': "DB ID check", 'doc': "", 'type': 'info'},
        {'bit': 18, 'name': "channel QHS status", 'doc': "any QHS values outside tolerance", 'type': 'info'},
        {'bit': 19, 'name': "channel QHL status", 'doc': "any QHL values outside tolerance", 'type': 'info'},
        {'bit': 20, 'name': "channel QLX status", 'doc': "any QLX values outside tolerance", 'type': 'info'},
        {'bit': 21, 'name': "channel TAC status", 'doc': "any TAC values outside tolerance", 'type': 'info'},
        {'bit': 22, 'name': "channel ped status", 'doc': "any ped measures outside tolerance", 'type': 'info'},
        {'bit': 23, 'name': "channel width status", 'doc': "any width measures outside tolerance", 'type': 'info'},
        {'bit': 24, 'name': "channel stability status", 'doc': "any difference measures outside tolerance", 'type': 'info'},
        {'bit': 25, 'name': "sequencer disabled", 'doc': "", 'type': 'info'},
        {'bit': 26, 'name': "channel insifficent events", 'doc': "fewer than 10 events for at least one cell on this channel", 'type': 'info'},
        {'bit': 27, 'name': "channel no events", 'doc': "0 events on this channel", 'type': 'info'},
        {'bit': 28, 'name': "spare", 'doc': "", 'type': 'info'},
        {'bit': 29, 'name': "spare", 'doc': "", 'type': 'info'},
        {'bit': 30, 'name': "spare", 'doc': "", 'type': 'info'},
        {'bit': 31, 'name': "GF spare", 'doc': "", 'type': 'info'}],

    
    'tslp': [
        {'bit': 0, 'name': "cell status TSLP", 'doc': "OR of bits 1-12", 'type': 'info'},
        {'bit': 1, 'name': "cell no events", 'doc': "0 events on this cell", 'type': 'fail'},
        {'bit': 2, 'name': "cell bad data", 'doc': "too few good points used in cubic fit", 'type': 'info'},
        {'bit': 3, 'name': "cell weird data", 'doc': "too many suspicious points", 'type': 'info'},
        {'bit': 4, 'name': "cell x3 status", 'doc': "x^3 coeff. outside limits", 'type': 'info'},
        {'bit': 5, 'name': "cell x3 stable", 'doc': "x^3 coeff. outside range of previous run", 'type': 'info'},
        {'bit': 6, 'name': "cell x2 status", 'doc': "x^2 coeff. outside limits", 'type': 'info'},
        {'bit': 7, 'name': "cell x2 stable", 'doc': "x^2 coeff. outside range of previous run", 'type': 'info'},
        {'bit': 8, 'name': "cell x status", 'doc': "x^3 coeff. outside limits", 'type': 'info'},
        {'bit': 9, 'name': "cell x stable", 'doc': "x^3 coeff. outside range of previous run", 'type': 'info'},
        {'bit': 10, 'name': "cell width status", 'doc': "Too many points with width outside tolerance", 'type': 'info'},
        {'bit': 11, 'name': "cell insufficent events", 'doc': "too many points with too few events", 'type': 'info'},
        {'bit': 12, 'name': "spare", 'doc': "", 'type': 'info'},
        {'bit': 13, 'name': "channel status", 'doc': "OR of bits 16-27", 'type': 'info'},
        {'bit': 14, 'name': "channel no events", 'doc': "0 events on this channel", 'type': 'fail'},
        {'bit': 15, 'name': "channel bad data", 'doc': "too few good points used in cubic fit", 'type': 'info'},
        {'bit': 16, 'name': "channel weird data", 'doc': "too many suspicious points", 'type': 'info'},
        {'bit': 17, 'name': "channel x3 status", 'doc': "x^3 coeff. outside limits and/or range of previous run", 'type': 'info'},
        {'bit': 18, 'name': "channel x2 status", 'doc': "x^2 coeff. outside limits and/or range of previous run", 'type': 'info'},
        {'bit': 19, 'name': "channel x status", 'doc': "x^3 coeff. outside limits and/or range of previous run", 'type': 'info'},
        {'bit': 20, 'name': "channel fit status", 'doc': "any fit parameters outside limits", 'type': 'info'},
        {'bit': 21, 'name': "channel fit stable", 'doc': "any fit parameters outside range of previous run", 'type': 'info'},
        {'bit': 22, 'name': "channel width status", 'doc': "too many points with width outside tolderance", 'type': 'info'},
        {'bit': 23, 'name': "channel insufficient events", 'doc': "too many points with two few events", 'type': 'info'},
        {'bit': 24, 'name': "MB ID check", 'doc': "", 'type': 'info'},
        {'bit': 25, 'name': "DB ID check", 'doc': "", 'type': 'info'},
        {'bit': 26, 'name': "sequencer disabled", 'doc': "", 'type': 'info'},
        {'bit': 27, 'name': "spare", 'doc': "", 'type': 'info'},
        {'bit': 28, 'name': "spare", 'doc': "", 'type': 'info'},
        {'bit': 29, 'name': "spare", 'doc': "", 'type': 'info'},
        {'bit': 30, 'name': "spare", 'doc': "", 'type': 'info'},
        {'bit': 31, 'name': "spare", 'doc': "", 'type': 'info'}],
}

