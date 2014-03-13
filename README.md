# ECA Run Summary Site

## System Requirements

Access to the site requires a modern web browser with javascript enabled. On the server site, generating new content requires:

- Python 2.6+, RAT, and ROOT

## Adding New Run Data

1. Create a new directory for your run in the "data" directory. Use the name format "runXXXXXX" where the Xs represent your run number. For example, "run20262" or "run100000". If there is already a folder with the name for your run, add a revision number to the end of your new name "run20262-2" or "run100000-13".
Example complete command: `mkdir data/run20262`

2. Move ECA_log_XXXX.txt, TSLP/PDST_XXXX_n.ratdb and TSLP/PDSThists_XXXX_n.root your plots into the new directory.

4. Run the make command from the main directory (the one containing "doc", "libexec", "www", etc.) This will rebuild all run info.

## Site structure
 - readme.md : This file
 - doc : Other site documentation
 - lib
 - lib/plotCrateViewPed.cc - needs to be compiled into libexec, makes crate view plots of where cell & channel status bits are set
 - lib/plotCrateViewTSlope.cc - needs to be compiled into libexec, makes crate view plots of where cell & channel status bits are set
 - lib/exmakefile.txt - text of a Makefile to compile the plotCrateView macros. One day I will figure out how to put this into the main Makefile
 - libexec - these scripts assume that your working directory will be the base of the site
 - libexec/generate_constants_json.py
 - libexec/generate_formatted_histos.py
 - libexec/generate_index_json.py
 - libexec/generate_flag_index_json.py
 - Makefile
 - www
 - www/css
 - www/css/flag-screen-v1.css
 - www/css/menu-screen-v1.css
 - www/css/pmt-screen-v1.css
 - www/data
 - www/detail.html
 - www/index.html
 - www/js
 - www/js/flags.json
 - www/js/jquery-1.9.1.min.js
 - www/js/jquery.masonry-2.1.08.min.js
 - www/js/pca-menu.js
 - www/media
 - www/media/bg.png
 - data
 - data/attic - ?? what is this? ignored by software. you can keep old data archives in and whatever else you want in here. keeps the tree tidy.
 - data/index.json





