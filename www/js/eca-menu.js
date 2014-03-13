var eca;
var detailPanels;

$( init );

function init() {
    $('h1').fadeOut('slow');
    $('h1').fadeIn('slow');

    // load flag configuration
    $.getJSON('js/eca_constants.json', function(data) { eca = data });

    // load run summary
    $.getJSON('data/index.json', function(data) {
        populateRunTable(data);
    });

    detailPanels = {};
}


function populateRunTable(eca_runs) {
    $.each(eca_runs, function(idx, thisRun) {
        var row = $('<tr/>', {
            "id": "row-run-" + thisRun['run_name'],
            "class": "run " + ((idx & 1) ? "even" : "odd")
        });

        var nameCell = $('<td/>', {"class": "run_name"});
        nameCell.append(thisRun['run_name']);

        var dateCell = $('<td/>');
        dateCell.append(thisRun['date']);

        var gainFitCell = $('<td/>', {
            "class": thisRun['pdst_pass'] ? "pass" : "fail"
        });
        gainFitCell.append("<em>" +
                          (thisRun['pdst_pass'] ? 'Yes' : 'No') +
                          "</em>");

        var timeWalkCell = $('<td/>', {
            "class": thisRun['tslp_pass'] ? "pass" : "fail"
        });
        timeWalkCell.append("<em>" +
                            (thisRun['tslp_pass'] ? 'Yes' : 'No') +
                            "</em>");

        var ratAvailableCell = $('<td/>', {
            "class": thisRun['rat_available'] ? "yes" : "no"
        });
        ratAvailableCell.append("<em>" +
                                (thisRun['rat_available'] ? 'Yes' : 'No') +
                                "</em>");

        var detailControlCell = $('<td/>', {
            "class": "expander"
        });
        detailControlCell.append('<a href="#more">Show</a>').click([thisRun['run_name']], toggleDetailsPanel);

        row.append(nameCell);
        row.append(dateCell);
        row.append(gainFitCell);
        row.append(timeWalkCell);
        row.append(ratAvailableCell);
        row.append(detailControlCell);
        $('table#run-list tbody').append(row);
    });
}


function toggleDetailsPanel(clickInfo) {
    var targetRun = clickInfo.data[0];
    if (!(targetRun in detailPanels)) {
        detailPanels[targetRun] = createDetailsPanel(targetRun);
    }
    showHideDetailsPanel(detailPanels[targetRun]);
    clickInfo.preventDefault();
    window.console.log(clickInfo);
}


function createDetailsPanel(targetRun) {
    var row = $("<tr />", {"class": "details", "id": "details-" + targetRun});
    var cell = $("<td />", {colspan: 6});
    var div = $("<div />", {});
    var filters = $("<div />", {"class": "filters"});

    var filtercategory = $("<div />", {"class": "filtercategory"});
    $.each(eca.flags, function(mode, flags) {
        var category = $("<a/>", {
            href: "#",
            "class": (mode == "general") ? "selected" : "unselected",
            click: function (event) {
                $(event.target).attr({"class": "selected"});
                $(event.target).siblings().attr({"class": "unselected"})
                drawFilterOptions("tr#details-" + targetRun);
                event.preventDefault();
            }
        }).append(mode);
        filtercategory.append(category);
    })

    var categoryoptions = $("<div />", {"class": "categoryoptions"});
    
    var filterimage_wrapper = $("<div />", {
        "class": "filterimage-wrapper"
    }).append("Loading...");

    filters.append(filtercategory);
    filters.append(categoryoptions);
    div.append(filters);
    div.append(filterimage_wrapper);
    cell.append(div);
    row.append(cell);
    row.hide();
    $('tr#row-run-' + targetRun).after(row);

    return "details-" + targetRun;
}


function drawFilterOptions(rowSelector) {
    var categoryOptions = $(rowSelector + " .categoryoptions");
    var runName = $(rowSelector).attr('id').split('-')[1];
    var runMode = $(rowSelector + ' .filtercategory .selected').text().toLowerCase();

    var reset = false;

    // Clear out any existing content
    if (categoryOptions.children().length > 0) {
        reset = true;
        categoryOptions.empty();
    }

    $.each(eca.flags[runMode], function(idx, flag) {
        if (flag['name'] == "spare"
            || flag['name'] == "TW spare"
            || flag['name'] == "GF spare") return;

        var option = $("<a/>", {
            "class": (idx == 0) ? "selected" : "unselected",
            click: function (event) {
                if ($(event.target).getattr('class') !== 'selected') {
                    $(event.target).attr({"class": "selected"});
                } else {
                    $(event.target).attr({"class": "unselected"});
                }
                $(event.target).siblings().attr({"class": "unselected"});
                event.preventDefault();
            },            
            hover: function (event) {
//                var flagNumberString = (String(idx).length == 1) ? idx : idx;
                var flagNumberString = (String(idx).length == 1) ? "0" + idx : idx;

                //if (flagNumberString == "00") {
                  //  flagImageFilename = runMode + "-allflags.png";
                //} else {
                  //  flagImageFilename = runMode + "-flag-" + flagNumberString + ".png";
                //}
                    flagImageFilename = runMode + "-flag-" + flagNumberString + ".png";

                var filterimage = $("<img />", {
                    "class": "filterimage",
                    src: "data/" + runName + '/crate_view/' + flagImageFilename
//                    src: "data/run6665/crate_view/pdst-flag-00.png"
                });

                $(rowSelector + ' .filterimage-wrapper').empty().append(filterimage);

                event.preventDefault();
            },
        }).append(flag['name']);
        categoryOptions.append(option);
    });

    if (reset) {
        categoryOptions.masonry('reload');
    } else {
        categoryOptions.masonry({itemSelector : 'a'});        
    }

}


function showHideDetailsPanel(targetRowId) {
    var rowSelector = "tr#" + targetRowId;
    var parentRow = $(rowSelector).prev();

    if ($(rowSelector).is(":visible")) {
        // Hide it
        $(rowSelector + "> td> div").slideUp(250, function() { $(rowSelector).hide() });
        parentRow.find("td.expander a").text("Show");
    } else {
        // Show it
        $(rowSelector).show(0, function() { $(rowSelector + "> td> div").slideDown(250) });
        parentRow.find("td.expander a").text("Hide");
        drawFilterOptions(rowSelector);
    }
}

