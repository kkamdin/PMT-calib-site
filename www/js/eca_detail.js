var eca;
var runs;
var runid;
var mode;

$( init );

function init() {
    // Decode items after the hash. For example: #run20652;flags
    var url_args = location.hash.split("#")[1].split(';')
    runid = url_args[0];
    mode = url_args[1];

    var message = false;

    $('h1').append(runid);
    $('h2').append(mode);

    // load constants  
    //$.getJSON('data/index.json', function(data) { runs = data });

    switch(mode) {
        case "stats":
            showRunStats();
            break;
        case "flags":
            var gf_url = 'data/' + runid + '/channel_data/gf_flag_index.json';
            var tw_url = 'data/' + runid + '/channel_data/tw_flag_index.json';

            $.getJSON('js/eca_constants.json', function(ecadata) {
                eca = ecadata; 
                $.getJSON(gf_url, function(gfData) {
                    showFlags(gfData, "gf"); 
                });
                $.getJSON(tw_url, function(twData) {
                    showFlags(twData, "tw");
                });
            });
            break;
        case "pmts":
	    showPMTPlots();
            break;
        default:
            message = "Unknown mode: " + mode;
    }

    if (message) {
        $("div#content").append(
            $('<p/>', {"class": "message"}).append(message));
    }

}

function showRunStats() {
    var content = $('div#content');

    var images = {
        'Hits per PMT': ['PCAhitPerPMT.png'],
        'Threshold Peak and High Half Point Histograms':
            ['HistsQHL.png', 'HistsQHS.png'],
        'Threshold Peak and High Half Point Scatterplots':
            ['peakSummaryQHL.png', 'peakSummaryQHS.png'],

        'QHL Threshold Difference (Previous - New)':
            ['PCAdiffTHRESHQHL.png', 'PCAdiffTHRESHQHL1d.png'],
        'QHS Threshold Difference (Previous - New)':
            ['PCAdiffTHRESHQHS.png', 'PCAdiffTHRESHQHS1d.png'],

        'QHL Peak Difference (Previous - New)':
            ['PCAdiffPEAKQHL.png', 'PCAdiffPEAKQHL1d.png'],
        'QHS Peak Difference (Previous - New)':
            ['PCAdiffPEAKQHS.png', 'PCAdiffPEAKQHS1d.png'],

        'QHL High Half Point Difference (Previous - New)':
            ['PCAdiffHHPQHL.png', 'PCAdiffHHPQHL1d.png'],
        'QHS High Half Point Difference (Previous - New)':
            ['PCAdiffHHPQHS.png', 'PCAdiffHHPQHS1d.png']
    };

    $.each(images, function(group_name, img_group) {
        content.append($('<h3/>').append(group_name));
        $.each(img_group, function(i, img_path) {
            content.append($('<img/>', {
                src: 'data/' + runid + '/' + img_path
            }));            
        });
    });
}

function showFlags(flagdata, flagtype) {
    var content = $('div#content');
    var table = $("<table/>");
    var thead = $("<thead><tr><td>Bit</td><td>Flag</td><td># failed channels</td></tr></thead>");
    var tbody = $("<tbody/>");
    switch(flagtype) {
        case "gf":
            content.append($('<h3/>').append("Gain Fit"));
            break;
        case "tw":
            content.append($('<h3/>').append("Time Walk"));
            break;
        default:
            content.append($('<h3/>').append("Unknown flagtype, dude!"));
    }

    $.each(flagdata, function(flag_number, matching_pmt_list) {
        var flag_name = eca["flags"][flagtype][flag_number]["name"];
        var color_class = "good";
        if (flag_name == "spare") return;
        if (matching_pmt_list.length >= 50) {
            color_class = "bad";
        } else if (matching_pmt_list.length > 10) {
            color_class = "warn";
        }         
        var row = $("<tr/>");
        var cell0 = $("<td/>").append(flag_number);
        var cell1 = $("<td/>").append(flag_name);
        var cell2 = $("<td/>", {"class": color_class}).append(matching_pmt_list.length);
        row.append(cell0);
        row.append(cell1);
        row.append(cell2);
        tbody.append(row);
    });
    table.append(thead);
    table.append(tbody);
    content.append(table);
}

function showPMTPlots() {
    
}
