# PCA Run Summary Site

## System Requirements

Access to the site requires a modern web browser with javascript enabled. On the server site, generating new content requires:

- Python 2.6+, with these modules:
    - PIL (the python imaging library)
    - PyYaml (a YAML parser)

## Adding New Run Data

1. Create a new directory for your run in the "data" directory. Use the name format "runXXXXXX" where the Xs represent your run number. For example, "run20262" or "run100000". If there is already a folder with the name for your run, add a revision number to the end of your new name "run20262-2" or "run100000-13".
Example complete command: `mkdir data/run20262`

2. Move your plots into the new directory.

3. Put your .ratdb files in the new directory. They *must* be named PCA_log_XXXXXX.ratdb, PCATW_XXXXXX.ratdb, and PCAGF_XXXXXX.ratdb, where the Xs represent your run number. Note: The actual numbers contained in these Xs is ignored by the software, but you should still try to make it match the run number to make future maintenence easier. If you had to add a revision number to your directory name, don't add it here. **The ratdb files must match this glob: `PCA*.ratdb`**

4. Run the make command from the main directory (the one containing "doc", "libexec", "www", etc.) This will rebuild all run info.

## Site structure
 - readme.md : This file
 - doc : Other site documentation
 - lib
 - lib/pca_constants.py : A python file which contains a master list of PCA constants, including flags
 - lib/pca_constants.json : A json file generated from the python file
 - libexec - these scripts assume that your working directory will be the base of the site
 - libexec/generate_images.py
 - libexec/parse_ratdb.py
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
 - data/attic - ignored by software. you can keep old data archives in and whatever else you want in here. keeps the tree tidy.
 - data/index.json
 - data/run100000-2
 - data/run100000-2/HistsQHL.png
 - data/run100000-2/HistsQHS.png
 - data/run100000-2/PCA_log_100000.ratdb
 - data/run100000-2/PCAdiffHHPQHL.png
 - data/run100000-2/PCAdiffHHPQHL1d.png
 - data/run100000-2/PCAdiffHHPQHS.png
 - data/run100000-2/PCAdiffHHPQHS1d.png
 - data/run100000-2/PCAdiffPEAKQHL.png
 - data/run100000-2/PCAdiffPEAKQHL1d.png
 - data/run100000-2/PCAdiffPEAKQHS.png
 - data/run100000-2/PCAdiffPEAKQHS1d.png
 - data/run100000-2/PCAdiffTHRESHQHL.png
 - data/run100000-2/PCAdiffTHRESHQHL1d.png
 - data/run100000-2/PCAdiffTHRESHQHS.png
 - data/run100000-2/PCAdiffTHRESHQHS1d.png
 - data/run100000-2/PCAGF_100000.ratdb
 - data/run100000-2/PCAhitPerPMT.png
 - data/run100000-2/PCATW_100000.ratdb
 - data/run100000-2/peakSummaryQHL.png
 - data/run100000-2/peakSummaryQHS.png
 - data/run100000-2/PMT-1009-QHL.png
 - data/run100000-2/PMT-1009-QHS.png
 - data/run100000-2/PMT-1009-Tec.png
 - data/run100000-2/PMT-1009-TW.png
 - data/run100000-2/PMT-1039-QHL.png
 - data/run100000-2/PMT-1039-QHS.png
 - data/run100000-2/PMT-1039-Tec.png
 - data/run100000-2/PMT-1039-TW.png
 - data/run100000-2/PMT-1073-QHL.png
 - data/run100000-2/PMT-1073-QHS.png
 - data/run100000-2/PMT-1073-Tec.png
 - data/run100000-2/PMT-1073-TW.png
 - data/run100000-2/PMT-1107-QHL.png
 - data/run100000-2/PMT-1107-QHS.png
 - data/run100000-2/PMT-1107-Tec.png
 - data/run100000-2/PMT-1107-TW.png
 - data/run100000-2/PMT-1131-QHL.png
 - data/run100000-2/PMT-1131-QHS.png
 - data/run100000-2/PMT-1131-Tec.png
 - data/run100000-2/PMT-1131-TW.png
 - data/run100000-2/PMT-1145-QHL.png
 - data/run100000-2/PMT-1145-QHS.png
 - data/run100000-2/PMT-1145-Tec.png
 - data/run100000-2/PMT-1145-TW.png
 - data/run100000-2/PMT-1156-QHL.png
 - data/run100000-2/PMT-1156-QHS.png
 - data/run100000-2/PMT-1156-Tec.png
 - data/run100000-2/PMT-1156-TW.png
 - data/run100000-2/PMT-1170-QHL.png
 - data/run100000-2/PMT-1170-QHS.png
 - data/run100000-2/PMT-1170-Tec.png
 - data/run100000-2/PMT-1170-TW.png
 - data/run100000-2/PMT-1297-QHL.png
 - data/run100000-2/PMT-1297-QHS.png
 - data/run100000-2/PMT-1297-Tec.png
 - data/run100000-2/PMT-1297-TW.png
 - data/run100000-2/PMT-139-QHL.png
 - data/run100000-2/PMT-139-QHS.png
 - data/run100000-2/PMT-139-Tec.png
 - data/run100000-2/PMT-139-TW.png
 - data/run100000-2/PMT-1484-QHL.png
 - data/run100000-2/PMT-1484-QHS.png
 - data/run100000-2/PMT-1484-Tec.png
 - data/run100000-2/PMT-1484-TW.png
 - data/run100000-2/PMT-1544-QHL.png
 - data/run100000-2/PMT-1544-QHS.png
 - data/run100000-2/PMT-1544-Tec.png
 - data/run100000-2/PMT-1544-TW.png
 - data/run100000-2/PMT-1553-QHL.png
 - data/run100000-2/PMT-1553-QHS.png
 - data/run100000-2/PMT-1553-Tec.png
 - data/run100000-2/PMT-1553-TW.png
 - data/run100000-2/PMT-1555-QHL.png
 - data/run100000-2/PMT-1555-QHS.png
 - data/run100000-2/PMT-1555-Tec.png
 - data/run100000-2/PMT-1555-TW.png
 - data/run100000-2/PMT-1585-QHL.png
 - data/run100000-2/PMT-1585-QHS.png
 - data/run100000-2/PMT-1585-Tec.png
 - data/run100000-2/PMT-1585-TW.png
 - data/run100000-2/PMT-189-QHL.png
 - data/run100000-2/PMT-189-QHS.png
 - data/run100000-2/PMT-189-Tec.png
 - data/run100000-2/PMT-189-TW.png
 - data/run100000-2/PMT-2-QHL.png
 - data/run100000-2/PMT-2-QHS.png
 - data/run100000-2/PMT-2-Tec.png
 - data/run100000-2/PMT-2-TW.png
 - data/run100000-2/PMT-201-QHL.png
 - data/run100000-2/PMT-201-QHS.png
 - data/run100000-2/PMT-201-Tec.png
 - data/run100000-2/PMT-201-TW.png
 - data/run100000-2/PMT-205-QHL.png
 - data/run100000-2/PMT-205-QHS.png
 - data/run100000-2/PMT-205-Tec.png
 - data/run100000-2/PMT-205-TW.png
 - data/run100000-2/PMT-208-QHL.png
 - data/run100000-2/PMT-208-QHS.png
 - data/run100000-2/PMT-208-Tec.png
 - data/run100000-2/PMT-208-TW.png
 - data/run100000-2/PMT-2082-QHL.png
 - data/run100000-2/PMT-2082-QHS.png
 - data/run100000-2/PMT-2082-Tec.png
 - data/run100000-2/PMT-2082-TW.png
 - data/run100000-2/PMT-2083-QHL.png
 - data/run100000-2/PMT-2083-QHS.png
 - data/run100000-2/PMT-2083-Tec.png
 - data/run100000-2/PMT-2083-TW.png
 - data/run100000-2/PMT-2087-QHL.png
 - data/run100000-2/PMT-2087-QHS.png
 - data/run100000-2/PMT-2087-Tec.png
 - data/run100000-2/PMT-2087-TW.png
 - data/run100000-2/PMT-2088-QHL.png
 - data/run100000-2/PMT-2088-QHS.png
 - data/run100000-2/PMT-2088-Tec.png
 - data/run100000-2/PMT-2088-TW.png
 - data/run100000-2/PMT-2089-QHL.png
 - data/run100000-2/PMT-2089-QHS.png
 - data/run100000-2/PMT-2089-Tec.png
 - data/run100000-2/PMT-2089-TW.png
 - data/run100000-2/PMT-2100-QHL.png
 - data/run100000-2/PMT-2100-QHS.png
 - data/run100000-2/PMT-2100-Tec.png
 - data/run100000-2/PMT-2100-TW.png
 - data/run100000-2/PMT-2101-QHL.png
 - data/run100000-2/PMT-2101-QHS.png
 - data/run100000-2/PMT-2101-Tec.png
 - data/run100000-2/PMT-2101-TW.png
 - data/run100000-2/PMT-2103-QHL.png
 - data/run100000-2/PMT-2103-QHS.png
 - data/run100000-2/PMT-2103-Tec.png
 - data/run100000-2/PMT-2103-TW.png
 - data/run100000-2/PMT-2104-QHL.png
 - data/run100000-2/PMT-2104-QHS.png
 - data/run100000-2/PMT-2104-Tec.png
 - data/run100000-2/PMT-2104-TW.png
 - data/run100000-2/PMT-2105-QHL.png
 - data/run100000-2/PMT-2105-QHS.png
 - data/run100000-2/PMT-2105-Tec.png
 - data/run100000-2/PMT-2105-TW.png
 - data/run100000-2/PMT-2107-QHL.png
 - data/run100000-2/PMT-2107-QHS.png
 - data/run100000-2/PMT-2107-Tec.png
 - data/run100000-2/PMT-2107-TW.png
 - data/run100000-2/PMT-2108-QHL.png
 - data/run100000-2/PMT-2108-QHS.png
 - data/run100000-2/PMT-2108-Tec.png
 - data/run100000-2/PMT-2108-TW.png
 - data/run100000-2/PMT-2109-QHL.png
 - data/run100000-2/PMT-2109-QHS.png
 - data/run100000-2/PMT-2109-Tec.png
 - data/run100000-2/PMT-2109-TW.png
 - data/run100000-2/PMT-2110-QHL.png
 - data/run100000-2/PMT-2110-QHS.png
 - data/run100000-2/PMT-2110-Tec.png
 - data/run100000-2/PMT-2110-TW.png
 - data/run100000-2/PMT-2118-QHL.png
 - data/run100000-2/PMT-2118-QHS.png
 - data/run100000-2/PMT-2118-Tec.png
 - data/run100000-2/PMT-2118-TW.png
 - data/run100000-2/PMT-2123-QHL.png
 - data/run100000-2/PMT-2123-QHS.png
 - data/run100000-2/PMT-2123-Tec.png
 - data/run100000-2/PMT-2123-TW.png
 - data/run100000-2/PMT-2129-QHL.png
 - data/run100000-2/PMT-2129-QHS.png
 - data/run100000-2/PMT-2129-Tec.png
 - data/run100000-2/PMT-2129-TW.png
 - data/run100000-2/PMT-2130-QHL.png
 - data/run100000-2/PMT-2130-QHS.png
 - data/run100000-2/PMT-2130-Tec.png
 - data/run100000-2/PMT-2130-TW.png
 - data/run100000-2/PMT-2135-QHL.png
 - data/run100000-2/PMT-2135-QHS.png
 - data/run100000-2/PMT-2135-Tec.png
 - data/run100000-2/PMT-2135-TW.png
 - data/run100000-2/PMT-2139-QHL.png
 - data/run100000-2/PMT-2139-QHS.png
 - data/run100000-2/PMT-2139-Tec.png
 - data/run100000-2/PMT-2139-TW.png
 - data/run100000-2/PMT-2172-QHL.png
 - data/run100000-2/PMT-2172-QHS.png
 - data/run100000-2/PMT-2172-Tec.png
 - data/run100000-2/PMT-2172-TW.png
 - data/run100000-2/PMT-2187-QHL.png
 - data/run100000-2/PMT-2187-QHS.png
 - data/run100000-2/PMT-2187-Tec.png
 - data/run100000-2/PMT-2187-TW.png
 - data/run100000-2/PMT-2201-QHL.png
 - data/run100000-2/PMT-2201-QHS.png
 - data/run100000-2/PMT-2201-Tec.png
 - data/run100000-2/PMT-2201-TW.png
 - data/run100000-2/PMT-2204-QHL.png
 - data/run100000-2/PMT-2204-QHS.png
 - data/run100000-2/PMT-2204-Tec.png
 - data/run100000-2/PMT-2204-TW.png
 - data/run100000-2/PMT-2215-QHL.png
 - data/run100000-2/PMT-2215-QHS.png
 - data/run100000-2/PMT-2215-Tec.png
 - data/run100000-2/PMT-2215-TW.png
 - data/run100000-2/PMT-2547-QHL.png
 - data/run100000-2/PMT-2547-QHS.png
 - data/run100000-2/PMT-2547-Tec.png
 - data/run100000-2/PMT-2547-TW.png
 - data/run100000-2/PMT-2548-QHL.png
 - data/run100000-2/PMT-2548-QHS.png
 - data/run100000-2/PMT-2548-Tec.png
 - data/run100000-2/PMT-2548-TW.png
 - data/run100000-2/PMT-2589-QHL.png
 - data/run100000-2/PMT-2589-QHS.png
 - data/run100000-2/PMT-2589-Tec.png
 - data/run100000-2/PMT-2589-TW.png
 - data/run100000-2/PMT-2595-QHL.png
 - data/run100000-2/PMT-2595-QHS.png
 - data/run100000-2/PMT-2595-Tec.png
 - data/run100000-2/PMT-2595-TW.png
 - data/run100000-2/PMT-2600-QHL.png
 - data/run100000-2/PMT-2600-QHS.png
 - data/run100000-2/PMT-2600-Tec.png
 - data/run100000-2/PMT-2600-TW.png
 - data/run100000-2/PMT-2705-QHL.png
 - data/run100000-2/PMT-2705-QHS.png
 - data/run100000-2/PMT-2705-Tec.png
 - data/run100000-2/PMT-2705-TW.png
 - data/run100000-2/PMT-2914-QHL.png
 - data/run100000-2/PMT-2914-QHS.png
 - data/run100000-2/PMT-2914-Tec.png
 - data/run100000-2/PMT-2914-TW.png
 - data/run100000-2/PMT-296-QHL.png
 - data/run100000-2/PMT-296-QHS.png
 - data/run100000-2/PMT-296-Tec.png
 - data/run100000-2/PMT-296-TW.png
 - data/run100000-2/PMT-2961-QHL.png
 - data/run100000-2/PMT-2961-QHS.png
 - data/run100000-2/PMT-2961-Tec.png
 - data/run100000-2/PMT-2961-TW.png
 - data/run100000-2/PMT-2972-QHL.png
 - data/run100000-2/PMT-2972-QHS.png
 - data/run100000-2/PMT-2972-Tec.png
 - data/run100000-2/PMT-2972-TW.png
 - data/run100000-2/PMT-305-QHL.png
 - data/run100000-2/PMT-305-QHS.png
 - data/run100000-2/PMT-305-Tec.png
 - data/run100000-2/PMT-305-TW.png
 - data/run100000-2/PMT-3185-QHL.png
 - data/run100000-2/PMT-3185-QHS.png
 - data/run100000-2/PMT-3185-Tec.png
 - data/run100000-2/PMT-3185-TW.png
 - data/run100000-2/PMT-3473-QHL.png
 - data/run100000-2/PMT-3473-QHS.png
 - data/run100000-2/PMT-3473-Tec.png
 - data/run100000-2/PMT-3473-TW.png
 - data/run100000-2/PMT-35-QHL.png
 - data/run100000-2/PMT-35-QHS.png
 - data/run100000-2/PMT-35-Tec.png
 - data/run100000-2/PMT-35-TW.png
 - data/run100000-2/PMT-3607-QHL.png
 - data/run100000-2/PMT-3607-QHS.png
 - data/run100000-2/PMT-3607-Tec.png
 - data/run100000-2/PMT-3607-TW.png
 - data/run100000-2/PMT-376-QHL.png
 - data/run100000-2/PMT-376-QHS.png
 - data/run100000-2/PMT-376-Tec.png
 - data/run100000-2/PMT-376-TW.png
 - data/run100000-2/PMT-4136-QHL.png
 - data/run100000-2/PMT-4136-QHS.png
 - data/run100000-2/PMT-4136-Tec.png
 - data/run100000-2/PMT-4136-TW.png
 - data/run100000-2/PMT-4141-QHL.png
 - data/run100000-2/PMT-4141-QHS.png
 - data/run100000-2/PMT-4141-Tec.png
 - data/run100000-2/PMT-4141-TW.png
 - data/run100000-2/PMT-4145-QHL.png
 - data/run100000-2/PMT-4145-QHS.png
 - data/run100000-2/PMT-4145-Tec.png
 - data/run100000-2/PMT-4145-TW.png
 - data/run100000-2/PMT-4148-QHL.png
 - data/run100000-2/PMT-4148-QHS.png
 - data/run100000-2/PMT-4148-Tec.png
 - data/run100000-2/PMT-4148-TW.png
 - data/run100000-2/PMT-4241-QHL.png
 - data/run100000-2/PMT-4241-QHS.png
 - data/run100000-2/PMT-4241-Tec.png
 - data/run100000-2/PMT-4241-TW.png
 - data/run100000-2/PMT-4279-QHL.png
 - data/run100000-2/PMT-4279-QHS.png
 - data/run100000-2/PMT-4279-Tec.png
 - data/run100000-2/PMT-4279-TW.png
 - data/run100000-2/PMT-4292-QHL.png
 - data/run100000-2/PMT-4292-QHS.png
 - data/run100000-2/PMT-4292-Tec.png
 - data/run100000-2/PMT-4292-TW.png
 - data/run100000-2/PMT-4529-QHL.png
 - data/run100000-2/PMT-4529-QHS.png
 - data/run100000-2/PMT-4529-Tec.png
 - data/run100000-2/PMT-4529-TW.png
 - data/run100000-2/PMT-4625-QHL.png
 - data/run100000-2/PMT-4625-QHS.png
 - data/run100000-2/PMT-4625-Tec.png
 - data/run100000-2/PMT-4625-TW.png
 - data/run100000-2/PMT-4678-QHL.png
 - data/run100000-2/PMT-4678-QHS.png
 - data/run100000-2/PMT-4678-Tec.png
 - data/run100000-2/PMT-4678-TW.png
 - data/run100000-2/PMT-4680-QHL.png
 - data/run100000-2/PMT-4680-QHS.png
 - data/run100000-2/PMT-4680-Tec.png
 - data/run100000-2/PMT-4680-TW.png
 - data/run100000-2/PMT-4688-QHL.png
 - data/run100000-2/PMT-4688-QHS.png
 - data/run100000-2/PMT-4688-Tec.png
 - data/run100000-2/PMT-4688-TW.png
 - data/run100000-2/PMT-4692-QHL.png
 - data/run100000-2/PMT-4692-QHS.png
 - data/run100000-2/PMT-4692-Tec.png
 - data/run100000-2/PMT-4692-TW.png
 - data/run100000-2/PMT-4694-QHL.png
 - data/run100000-2/PMT-4694-QHS.png
 - data/run100000-2/PMT-4694-Tec.png
 - data/run100000-2/PMT-4694-TW.png
 - data/run100000-2/PMT-4696-QHL.png
 - data/run100000-2/PMT-4696-QHS.png
 - data/run100000-2/PMT-4696-Tec.png
 - data/run100000-2/PMT-4696-TW.png
 - data/run100000-2/PMT-4699-QHL.png
 - data/run100000-2/PMT-4699-QHS.png
 - data/run100000-2/PMT-4699-Tec.png
 - data/run100000-2/PMT-4699-TW.png
 - data/run100000-2/PMT-4702-QHL.png
 - data/run100000-2/PMT-4702-QHS.png
 - data/run100000-2/PMT-4702-Tec.png
 - data/run100000-2/PMT-4702-TW.png
 - data/run100000-2/PMT-4785-QHL.png
 - data/run100000-2/PMT-4785-QHS.png
 - data/run100000-2/PMT-4785-Tec.png
 - data/run100000-2/PMT-4785-TW.png
 - data/run100000-2/PMT-5127-QHL.png
 - data/run100000-2/PMT-5127-QHS.png
 - data/run100000-2/PMT-5127-Tec.png
 - data/run100000-2/PMT-5127-TW.png
 - data/run100000-2/PMT-5171-QHL.png
 - data/run100000-2/PMT-5171-QHS.png
 - data/run100000-2/PMT-5171-Tec.png
 - data/run100000-2/PMT-5171-TW.png
 - data/run100000-2/PMT-5201-QHL.png
 - data/run100000-2/PMT-5201-QHS.png
 - data/run100000-2/PMT-5201-Tec.png
 - data/run100000-2/PMT-5201-TW.png
 - data/run100000-2/PMT-5243-QHL.png
 - data/run100000-2/PMT-5243-QHS.png
 - data/run100000-2/PMT-5243-Tec.png
 - data/run100000-2/PMT-5243-TW.png
 - data/run100000-2/PMT-5254-QHL.png
 - data/run100000-2/PMT-5254-QHS.png
 - data/run100000-2/PMT-5254-Tec.png
 - data/run100000-2/PMT-5254-TW.png
 - data/run100000-2/PMT-529-QHL.png
 - data/run100000-2/PMT-529-QHS.png
 - data/run100000-2/PMT-529-Tec.png
 - data/run100000-2/PMT-529-TW.png
 - data/run100000-2/PMT-5358-QHL.png
 - data/run100000-2/PMT-5358-QHS.png
 - data/run100000-2/PMT-5358-Tec.png
 - data/run100000-2/PMT-5358-TW.png
 - data/run100000-2/PMT-538-QHL.png
 - data/run100000-2/PMT-538-QHS.png
 - data/run100000-2/PMT-538-Tec.png
 - data/run100000-2/PMT-538-TW.png
 - data/run100000-2/PMT-561-QHL.png
 - data/run100000-2/PMT-561-QHS.png
 - data/run100000-2/PMT-561-Tec.png
 - data/run100000-2/PMT-561-TW.png
 - data/run100000-2/PMT-5674-QHL.png
 - data/run100000-2/PMT-5674-QHS.png
 - data/run100000-2/PMT-5674-Tec.png
 - data/run100000-2/PMT-5674-TW.png
 - data/run100000-2/PMT-5675-QHL.png
 - data/run100000-2/PMT-5675-QHS.png
 - data/run100000-2/PMT-5675-Tec.png
 - data/run100000-2/PMT-5675-TW.png
 - data/run100000-2/PMT-5679-QHL.png
 - data/run100000-2/PMT-5679-QHS.png
 - data/run100000-2/PMT-5679-Tec.png
 - data/run100000-2/PMT-5679-TW.png
 - data/run100000-2/PMT-5687-QHL.png
 - data/run100000-2/PMT-5687-QHS.png
 - data/run100000-2/PMT-5687-Tec.png
 - data/run100000-2/PMT-5687-TW.png
 - data/run100000-2/PMT-5695-QHL.png
 - data/run100000-2/PMT-5695-QHS.png
 - data/run100000-2/PMT-5695-Tec.png
 - data/run100000-2/PMT-5695-TW.png
 - data/run100000-2/PMT-5729-QHL.png
 - data/run100000-2/PMT-5729-QHS.png
 - data/run100000-2/PMT-5729-Tec.png
 - data/run100000-2/PMT-5729-TW.png
 - data/run100000-2/PMT-5779-QHL.png
 - data/run100000-2/PMT-5779-QHS.png
 - data/run100000-2/PMT-5779-Tec.png
 - data/run100000-2/PMT-5779-TW.png
 - data/run100000-2/PMT-5810-QHL.png
 - data/run100000-2/PMT-5810-QHS.png
 - data/run100000-2/PMT-5810-Tec.png
 - data/run100000-2/PMT-5810-TW.png
 - data/run100000-2/PMT-5811-QHL.png
 - data/run100000-2/PMT-5811-QHS.png
 - data/run100000-2/PMT-5811-Tec.png
 - data/run100000-2/PMT-5811-TW.png
 - data/run100000-2/PMT-5813-QHL.png
 - data/run100000-2/PMT-5813-QHS.png
 - data/run100000-2/PMT-5813-Tec.png
 - data/run100000-2/PMT-5813-TW.png
 - data/run100000-2/PMT-6059-QHL.png
 - data/run100000-2/PMT-6059-QHS.png
 - data/run100000-2/PMT-6059-Tec.png
 - data/run100000-2/PMT-6059-TW.png
 - data/run100000-2/PMT-6092-QHL.png
 - data/run100000-2/PMT-6092-QHS.png
 - data/run100000-2/PMT-6092-Tec.png
 - data/run100000-2/PMT-6092-TW.png
 - data/run100000-2/PMT-611-QHL.png
 - data/run100000-2/PMT-611-QHS.png
 - data/run100000-2/PMT-611-Tec.png
 - data/run100000-2/PMT-611-TW.png
 - data/run100000-2/PMT-6153-QHL.png
 - data/run100000-2/PMT-6153-QHS.png
 - data/run100000-2/PMT-6153-Tec.png
 - data/run100000-2/PMT-6153-TW.png
 - data/run100000-2/PMT-6211-QHL.png
 - data/run100000-2/PMT-6211-QHS.png
 - data/run100000-2/PMT-6211-Tec.png
 - data/run100000-2/PMT-6211-TW.png
 - data/run100000-2/PMT-625-QHL.png
 - data/run100000-2/PMT-625-QHS.png
 - data/run100000-2/PMT-625-Tec.png
 - data/run100000-2/PMT-625-TW.png
 - data/run100000-2/PMT-6253-QHL.png
 - data/run100000-2/PMT-6253-QHS.png
 - data/run100000-2/PMT-6253-Tec.png
 - data/run100000-2/PMT-6253-TW.png
 - data/run100000-2/PMT-6283-QHL.png
 - data/run100000-2/PMT-6283-QHS.png
 - data/run100000-2/PMT-6283-Tec.png
 - data/run100000-2/PMT-6283-TW.png
 - data/run100000-2/PMT-6294-QHL.png
 - data/run100000-2/PMT-6294-QHS.png
 - data/run100000-2/PMT-6294-Tec.png
 - data/run100000-2/PMT-6294-TW.png
 - data/run100000-2/PMT-675-QHL.png
 - data/run100000-2/PMT-675-QHS.png
 - data/run100000-2/PMT-675-Tec.png
 - data/run100000-2/PMT-675-TW.png
 - data/run100000-2/PMT-6756-QHL.png
 - data/run100000-2/PMT-6756-QHS.png
 - data/run100000-2/PMT-6756-Tec.png
 - data/run100000-2/PMT-6756-TW.png
 - data/run100000-2/PMT-7179-QHL.png
 - data/run100000-2/PMT-7179-QHS.png
 - data/run100000-2/PMT-7179-Tec.png
 - data/run100000-2/PMT-7179-TW.png
 - data/run100000-2/PMT-7241-QHL.png
 - data/run100000-2/PMT-7241-QHS.png
 - data/run100000-2/PMT-7241-Tec.png
 - data/run100000-2/PMT-7241-TW.png
 - data/run100000-2/PMT-7258-QHL.png
 - data/run100000-2/PMT-7258-QHS.png
 - data/run100000-2/PMT-7258-Tec.png
 - data/run100000-2/PMT-7258-TW.png
 - data/run100000-2/PMT-7285-QHL.png
 - data/run100000-2/PMT-7285-QHS.png
 - data/run100000-2/PMT-7285-Tec.png
 - data/run100000-2/PMT-7285-TW.png
 - data/run100000-2/PMT-7336-QHL.png
 - data/run100000-2/PMT-7336-QHS.png
 - data/run100000-2/PMT-7336-Tec.png
 - data/run100000-2/PMT-7336-TW.png
 - data/run100000-2/PMT-7569-QHL.png
 - data/run100000-2/PMT-7569-QHS.png
 - data/run100000-2/PMT-7569-Tec.png
 - data/run100000-2/PMT-7569-TW.png
 - data/run100000-2/PMT-7572-QHL.png
 - data/run100000-2/PMT-7572-QHS.png
 - data/run100000-2/PMT-7572-Tec.png
 - data/run100000-2/PMT-7572-TW.png
 - data/run100000-2/PMT-7611-QHL.png
 - data/run100000-2/PMT-7611-QHS.png
 - data/run100000-2/PMT-7611-Tec.png
 - data/run100000-2/PMT-7611-TW.png
 - data/run100000-2/PMT-7728-QHL.png
 - data/run100000-2/PMT-7728-QHS.png
 - data/run100000-2/PMT-7728-Tec.png
 - data/run100000-2/PMT-7728-TW.png
 - data/run100000-2/PMT-7729-QHL.png
 - data/run100000-2/PMT-7729-QHS.png
 - data/run100000-2/PMT-7729-Tec.png
 - data/run100000-2/PMT-7729-TW.png
 - data/run100000-2/PMT-7732-QHL.png
 - data/run100000-2/PMT-7732-QHS.png
 - data/run100000-2/PMT-7732-Tec.png
 - data/run100000-2/PMT-7732-TW.png
 - data/run100000-2/PMT-7737-QHL.png
 - data/run100000-2/PMT-7737-QHS.png
 - data/run100000-2/PMT-7737-Tec.png
 - data/run100000-2/PMT-7737-TW.png
 - data/run100000-2/PMT-7752-QHL.png
 - data/run100000-2/PMT-7752-QHS.png
 - data/run100000-2/PMT-7752-Tec.png
 - data/run100000-2/PMT-7752-TW.png
 - data/run100000-2/PMT-7762-QHL.png
 - data/run100000-2/PMT-7762-QHS.png
 - data/run100000-2/PMT-7762-Tec.png
 - data/run100000-2/PMT-7762-TW.png
 - data/run100000-2/PMT-7804-QHL.png
 - data/run100000-2/PMT-7804-QHS.png
 - data/run100000-2/PMT-7804-Tec.png
 - data/run100000-2/PMT-7804-TW.png
 - data/run100000-2/PMT-7972-QHL.png
 - data/run100000-2/PMT-7972-QHS.png
 - data/run100000-2/PMT-7972-Tec.png
 - data/run100000-2/PMT-7972-TW.png
 - data/run100000-2/PMT-8240-QHL.png
 - data/run100000-2/PMT-8240-QHS.png
 - data/run100000-2/PMT-8240-Tec.png
 - data/run100000-2/PMT-8240-TW.png
 - data/run100000-2/PMT-8273-QHL.png
 - data/run100000-2/PMT-8273-QHS.png
 - data/run100000-2/PMT-8273-Tec.png
 - data/run100000-2/PMT-8273-TW.png
 - data/run100000-2/PMT-8305-QHL.png
 - data/run100000-2/PMT-8305-QHS.png
 - data/run100000-2/PMT-8305-Tec.png
 - data/run100000-2/PMT-8305-TW.png
 - data/run100000-2/PMT-8355-QHL.png
 - data/run100000-2/PMT-8355-QHS.png
 - data/run100000-2/PMT-8355-Tec.png
 - data/run100000-2/PMT-8355-TW.png
 - data/run100000-2/PMT-8358-QHL.png
 - data/run100000-2/PMT-8358-QHS.png
 - data/run100000-2/PMT-8358-Tec.png
 - data/run100000-2/PMT-8358-TW.png
 - data/run100000-2/PMT-8368-QHL.png
 - data/run100000-2/PMT-8368-QHS.png
 - data/run100000-2/PMT-8368-Tec.png
 - data/run100000-2/PMT-8368-TW.png
 - data/run100000-2/PMT-8528-QHL.png
 - data/run100000-2/PMT-8528-QHS.png
 - data/run100000-2/PMT-8528-Tec.png
 - data/run100000-2/PMT-8528-TW.png
 - data/run100000-2/PMT-8683-QHL.png
 - data/run100000-2/PMT-8683-QHS.png
 - data/run100000-2/PMT-8683-Tec.png
 - data/run100000-2/PMT-8683-TW.png
 - data/run100000-2/PMT-8732-QHL.png
 - data/run100000-2/PMT-8732-QHS.png
 - data/run100000-2/PMT-8732-Tec.png
 - data/run100000-2/PMT-8732-TW.png
 - data/run100000-2/PMT-8794-QHL.png
 - data/run100000-2/PMT-8794-QHS.png
 - data/run100000-2/PMT-8794-Tec.png
 - data/run100000-2/PMT-8794-TW.png
 - data/run100000-2/PMT-8798-QHL.png
 - data/run100000-2/PMT-8798-QHS.png
 - data/run100000-2/PMT-8798-Tec.png
 - data/run100000-2/PMT-8798-TW.png
 - data/run100000-2/PMT-8849-QHL.png
 - data/run100000-2/PMT-8849-QHS.png
 - data/run100000-2/PMT-8849-Tec.png
 - data/run100000-2/PMT-8849-TW.png
 - data/run100000-2/PMT-8886-QHL.png
 - data/run100000-2/PMT-8886-QHS.png
 - data/run100000-2/PMT-8886-Tec.png
 - data/run100000-2/PMT-8886-TW.png
 - data/run100000-2/PMT-8920-QHL.png
 - data/run100000-2/PMT-8920-QHS.png
 - data/run100000-2/PMT-8920-Tec.png
 - data/run100000-2/PMT-8920-TW.png
 - data/run100000-2/PMT-8992-QHL.png
 - data/run100000-2/PMT-8992-QHS.png
 - data/run100000-2/PMT-8992-Tec.png
 - data/run100000-2/PMT-8992-TW.png
 - data/run100000-2/PMT-9003-QHL.png
 - data/run100000-2/PMT-9003-QHS.png
 - data/run100000-2/PMT-9003-Tec.png
 - data/run100000-2/PMT-9003-TW.png
 - data/run100000-2/PMT-9009-QHL.png
 - data/run100000-2/PMT-9009-QHS.png
 - data/run100000-2/PMT-9009-Tec.png
 - data/run100000-2/PMT-9009-TW.png
 - data/run100000-2/PMT-9013-QHL.png
 - data/run100000-2/PMT-9013-QHS.png
 - data/run100000-2/PMT-9013-Tec.png
 - data/run100000-2/PMT-9013-TW.png
 - data/run100000-2/PMT-9019-QHL.png
 - data/run100000-2/PMT-9019-QHS.png
 - data/run100000-2/PMT-9019-Tec.png
 - data/run100000-2/PMT-9019-TW.png
 - data/run100000-2/PMT-9062-QHL.png
 - data/run100000-2/PMT-9062-QHS.png
 - data/run100000-2/PMT-9062-Tec.png
 - data/run100000-2/PMT-9062-TW.png
 - data/run100000-2/PMT-9084-QHL.png
 - data/run100000-2/PMT-9084-QHS.png
 - data/run100000-2/PMT-9084-Tec.png
 - data/run100000-2/PMT-9084-TW.png
 - data/run100000-2/PMT-9239-QHL.png
 - data/run100000-2/PMT-9239-QHS.png
 - data/run100000-2/PMT-9239-Tec.png
 - data/run100000-2/PMT-9239-TW.png
 - data/run100000-2/PMT-9285-QHL.png
 - data/run100000-2/PMT-9285-QHS.png
 - data/run100000-2/PMT-9285-Tec.png
 - data/run100000-2/PMT-9285-TW.png
 - data/run100000-2/PMT-9286-QHL.png
 - data/run100000-2/PMT-9286-QHS.png
 - data/run100000-2/PMT-9286-Tec.png
 - data/run100000-2/PMT-9286-TW.png
 - data/run100000-2/PMT-9347-QHL.png
 - data/run100000-2/PMT-9347-QHS.png
 - data/run100000-2/PMT-9347-Tec.png
 - data/run100000-2/PMT-9347-TW.png
 - data/run100000-2/PMT-9355-QHL.png
 - data/run100000-2/PMT-9355-QHS.png
 - data/run100000-2/PMT-9355-Tec.png
 - data/run100000-2/PMT-9355-TW.png
 - data/run100000-2/PMT-9375-QHL.png
 - data/run100000-2/PMT-9375-QHS.png
 - data/run100000-2/PMT-9375-Tec.png
 - data/run100000-2/PMT-9375-TW.png
 - data/run100000-2/PMT-9426-QHL.png
 - data/run100000-2/PMT-9426-QHS.png
 - data/run100000-2/PMT-9426-Tec.png
 - data/run100000-2/PMT-9426-TW.png
 - data/run100000-2/PMT-9428-QHL.png
 - data/run100000-2/PMT-9428-QHS.png
 - data/run100000-2/PMT-9428-Tec.png
 - data/run100000-2/PMT-9428-TW.png
 - data/run100000-2/PMT-9449-QHL.png
 - data/run100000-2/PMT-9449-QHS.png
 - data/run100000-2/PMT-9449-Tec.png
 - data/run100000-2/PMT-9449-TW.png
 - data/run100000-2/PMT-9461-QHL.png
 - data/run100000-2/PMT-9461-QHS.png
 - data/run100000-2/PMT-9461-Tec.png
 - data/run100000-2/PMT-9461-TW.png
 - data/run100000-2/PMT-9473-QHL.png
 - data/run100000-2/PMT-9473-QHS.png
 - data/run100000-2/PMT-9473-Tec.png
 - data/run100000-2/PMT-9473-TW.png
 - data/run100000-2/PMT-9492-QHL.png
 - data/run100000-2/PMT-9492-QHS.png
 - data/run100000-2/PMT-9492-Tec.png
 - data/run100000-2/PMT-9492-TW.png
 - data/run100000-2/PMT-9559-QHL.png
 - data/run100000-2/PMT-9559-QHS.png
 - data/run100000-2/PMT-9559-Tec.png
 - data/run100000-2/PMT-9559-TW.png
 - data/run100000-2/PMT-9569-QHL.png
 - data/run100000-2/PMT-9569-QHS.png
 - data/run100000-2/PMT-9569-Tec.png
 - data/run100000-2/PMT-9569-TW.png
 - data/run100000-2/PMT-9586-QHL.png
 - data/run100000-2/PMT-9586-QHS.png
 - data/run100000-2/PMT-9586-Tec.png
 - data/run100000-2/PMT-9586-TW.png
 - data/run100000-2/PMT-9643-QHL.png
 - data/run100000-2/PMT-9643-QHS.png
 - data/run100000-2/PMT-9643-Tec.png
 - data/run100000-2/PMT-9643-TW.png
 - data/run100000-2/PMT-9679-QHL.png
 - data/run100000-2/PMT-9679-QHS.png
 - data/run100000-2/PMT-9679-Tec.png
 - data/run100000-2/PMT-9679-TW.png
 
