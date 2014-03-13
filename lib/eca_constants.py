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
        {'bit': 0, 'name': "cell overall status", 'doc': "OR of bits 1-14", 'type': 'info'},
        {'bit': 1, 'name': "cell QHS invalid", 'doc': "QHS ped outside limits", 'type': 'info'},
        {'bit': 2, 'name': "cell QHS width invalid", 'doc': "width > upper limit", 'type': 'info'},
        {'bit': 3, 'name': "cell QHS unstable", 'doc': "differebce from previous run > upper limit", 'type': 'info'},
        {'bit': 4, 'name': "cell QHL invalid", 'doc': "QHL ped outside limits", 'type': 'info'},
        {'bit': 5, 'name': "cell QHL width invalid", 'doc': "width > upper limit", 'type': 'info'},
        {'bit': 6, 'name': "cell QHL unstable", 'doc': "differebce from previous run > upper limit", 'type': 'info'},
        {'bit': 7, 'name': "cell QLX invalid", 'doc': "QHX ped outside limits", 'type': 'info'},
        {'bit': 8, 'name': "cell QLX width invalid", 'doc': "width > upper limit", 'type': 'info'},
        {'bit': 9, 'name': "cell QLX unstable", 'doc': "differebce from previous run > upper limit", 'type': 'info'},
        {'bit': 10, 'name': "cell TAC invalid", 'doc': "TAC ped outside limits", 'type': 'info'},
        {'bit': 11, 'name': "cell TAC width invalid", 'doc': "width > upper limit", 'type': 'info'},
        {'bit': 12, 'name': "cell TAC unstable", 'doc': "differebce from previous run > upper limit", 'type': 'info'},
        {'bit': 13, 'name': "cell insufficent events", 'doc': "fewer than 10 events on this cell", 'type': 'info'},
        {'bit': 14, 'name': "cell 0 events", 'doc': "0 events on this cell", 'type': 'fail'},
        {'bit': 15, 'name': "channel overall status", 'doc': "OR of bits 16-27", 'type': 'info'},
        {'bit': 16, 'name': "MB ID check", 'doc': "", 'type': 'info'},
        {'bit': 17, 'name': "DB ID check", 'doc': "", 'type': 'info'},
        {'bit': 18, 'name': "channel QHS value/width invalid", 'doc': "any QHS values outside tolerance", 'type': 'info'},
        {'bit': 19, 'name': "channel QHL value/width invalid", 'doc': "any QHL values outside tolerance", 'type': 'info'},
        {'bit': 20, 'name': "channel QLX value/width invalid", 'doc': "any QLX values outside tolerance", 'type': 'info'},
        {'bit': 21, 'name': "channel TAC value/width invalid", 'doc': "any TAC values outside tolerance", 'type': 'info'},
        {'bit': 22, 'name': "channel any ped bad", 'doc': "any ped measures outside tolerance", 'type': 'info'},
        {'bit': 23, 'name': "channel any width bad", 'doc': "any width measures outside tolerance", 'type': 'info'},
        {'bit': 24, 'name': "channel any stability bad", 'doc': "any difference measures outside tolerance", 'type': 'info'},
        {'bit': 25, 'name': "sequencer disabled", 'doc': "", 'type': 'info'},
        {'bit': 26, 'name': "channel insifficent events", 'doc': "fewer than 10 events for at least one cell on this channel", 'type': 'info'},
        {'bit': 27, 'name': "channel 0 events", 'doc': "0 events on this channel", 'type': 'info'},
        {'bit': 28, 'name': "spare", 'doc': "", 'type': 'info'},
        {'bit': 29, 'name': "spare", 'doc': "", 'type': 'info'},
        {'bit': 30, 'name': "spare", 'doc': "", 'type': 'info'},
        {'bit': 31, 'name': "GF spare", 'doc': "", 'type': 'info'}],

    
    'tslp': [
        {'bit': 0, 'name': "cell overall status", 'doc': "OR of bits 1-12", 'type': 'info'},
        {'bit': 1, 'name': "cell 0 events", 'doc': "0 events on this cell", 'type': 'fail'},
        {'bit': 2, 'name': "cell too few points for fit", 'doc': "too few good points used in cubic fit", 'type': 'info'},
        {'bit': 3, 'name': "cell too many suspicious points", 'doc': "too many suspicious points", 'type': 'info'},
        {'bit': 4, 'name': "cell x3 param bad", 'doc': "x^3 coeff. outside limits", 'type': 'info'},
        {'bit': 5, 'name': "cell x3 param unstable", 'doc': "x^3 coeff. outside range of previous run", 'type': 'info'},
        {'bit': 6, 'name': "cell x2 param bad", 'doc': "x^2 coeff. outside limits", 'type': 'info'},
        {'bit': 7, 'name': "cell x2 param unstable", 'doc': "x^2 coeff. outside range of previous run", 'type': 'info'},
        {'bit': 8, 'name': "cell x param bad", 'doc': "x^3 coeff. outside limits", 'type': 'info'},
        {'bit': 9, 'name': "cell x param unstable", 'doc': "x^3 coeff. outside range of previous run", 'type': 'info'},
        {'bit': 10, 'name': "cell too many points bad width", 'doc': "Too many points with width outside tolerance", 'type': 'info'},
        {'bit': 11, 'name': "cell too many points w too few events", 'doc': "too many points with too few events", 'type': 'info'},
        {'bit': 12, 'name': "cell railed", 'doc': "cell has 1 or more points at 4095", 'type': 'info'},
        {'bit': 13, 'name': "channel overall status", 'doc': "OR of bits 16-27", 'type': 'info'},
        {'bit': 14, 'name': "channel 0 events", 'doc': "0 events on this channel", 'type': 'fail'},
        {'bit': 15, 'name': "channel too few points for fit", 'doc': "any cells w too few good points used in cubic fit", 'type': 'info'},
        {'bit': 16, 'name': "channel too many suspicious points", 'doc': "any cells w too many suspicious points", 'type': 'info'},
        {'bit': 17, 'name': "channel x3 param bad or unstable", 'doc': "x^3 coeff. outside limits and/or range of previous run", 'type': 'info'},
        {'bit': 18, 'name': "channel x2 param bad or unstable", 'doc': "x^2 coeff. outside limits and/or range of previous run", 'type': 'info'},
        {'bit': 19, 'name': "channel x param bad or unstable", 'doc': "x^3 coeff. outside limits and/or range of previous run", 'type': 'info'},
        {'bit': 20, 'name': "channel any fit params bad", 'doc': "any fit parameters outside limits", 'type': 'info'},
        {'bit': 21, 'name': "channel any fit unstable", 'doc': "any fit parameters outside range of previous run", 'type': 'info'},
        {'bit': 22, 'name': "channel too many bad widths", 'doc': "too many points with width outside tolderance", 'type': 'info'},
        {'bit': 23, 'name': "channel too many points w few events", 'doc': "too many points with two few events", 'type': 'info'},
        {'bit': 24, 'name': "MB ID check", 'doc': "", 'type': 'info'},
        {'bit': 25, 'name': "DB ID check", 'doc': "", 'type': 'info'},
        {'bit': 26, 'name': "sequencer disabled", 'doc': "", 'type': 'info'},
        {'bit': 27, 'name': "channel any railed", 'doc': "", 'type': 'info'},
        {'bit': 28, 'name': "spare", 'doc': "", 'type': 'info'},
        {'bit': 29, 'name': "spare", 'doc': "", 'type': 'info'},
        {'bit': 30, 'name': "spare", 'doc': "", 'type': 'info'},
        {'bit': 31, 'name': "spare", 'doc': "", 'type': 'info'}],
}

