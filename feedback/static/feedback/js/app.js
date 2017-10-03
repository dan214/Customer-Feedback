$(document).ready(function () {

    $(".lorem").hide();
    $(".lorem").fadeIn(6000);

    $('.reviews').bxSlider({
        speed: 10000,
        auto: true,
        controls: true,
        captions: true,
        pager: false,
        ticker: true,
        mode: 'vertical',
    });
    $('.companies').bxSlider({
        speed: 2000,
        auto: true,
        pager:false,
        controls: true,
        pause:2000,
        mode: 'horizontal',
    });


});

// Get the CSV and create the chart
$.getJSON('https://www.highcharts.com/samples/data/jsonp.php?filename=analytics.csv&callback=?', function (csv) {

    Highcharts.chart('graph', {

        data: {
            csv: csv
        },

        title: {
            text: 'Daily visits at www.highcharts.com'
        },

        subtitle: {
            text: 'Source: Google Analytics'
        },

        xAxis: {
            tickInterval: 7 * 24 * 3600 * 1000, // one week
            tickWidth: 0,
            gridLineWidth: 1,
            labels: {
                align: 'left',
                x: 3,
                y: -3
            }
        },

        yAxis: [{ // left y axis
            title: {
                text: null
            },
            labels: {
                align: 'left',
                x: 3,
                y: 16,
                format: '{value:.,0f}'
            },
            showFirstLabel: false
        }, { // right y axis
            linkedTo: 0,
            gridLineWidth: 0,
            opposite: true,
            title: {
                text: null
            },
            labels: {
                align: 'right',
                x: -3,
                y: 16,
                format: '{value:.,0f}'
            },
            showFirstLabel: false
        }],

        legend: {
            align: 'left',
            verticalAlign: 'top',
            y: 20,
            floating: true,
            borderWidth: 0
        },

        tooltip: {
            shared: true,
            crosshairs: true
        },

        plotOptions: {
            series: {
                cursor: 'pointer',
                point: {
                    events: {
                        click: function (e) {
                            hs.htmlExpand(null, {
                                pageOrigin: {
                                    x: e.pageX || e.clientX,
                                    y: e.pageY || e.clientY
                                },
                                headingText: this.series.name,
                                maincontentText: Highcharts.dateFormat('%A, %b %e, %Y', this.x) + ':<br/> ' +
                                    this.y + ' visits',
                                width: 200
                            });
                        }
                    }
                },
                marker: {
                    lineWidth: 1
                }
            }
        },

        series: [{
            name: 'All visits',
            lineWidth: 4,
            marker: {
                radius: 4
            }
        }, {
            name: 'New visitors'
        }]
    });
});
$(document).delegate("#CustomerReviewButton", "click", function (event) {
    var url = $(this).attr('href');
    event.preventDefault();
    var url = $(this).attr('href');
    var _width = "560px",
        _height = "540px";
    $.colorbox({
        iframe: true, fixed: true, width: _width, height: _height, scrolling: true, href: url
    });
});

$(document).delegate("#SubmitReviewButton",
    "click",
    function (event) {
        var id = $(this).attr('data-id');

        event.preventDefault();

        $.ajax({
            type: 'POST',
            url: '/reviews/create_review/' + id + '/',
            dataType: 'json',
            data: $('form#SubmitReviewForm').serializeObject(), // serialize all your
            success: function (data, textStatus) {
                parent.$.fn.colorbox.close();
                window.parent.location.href = "/";
            },
            error: function (xhr, status, e) {
                alert(status, e);
            }
        });


    });


function up() {
    animateContent("up")
}

function down() {
    animateContent("down")
}

function start() {
    setTimeout(function () {
        down();
    }, 1000);
    setTimeout(function () {
        up();
    }, 1000);
    setTimeout(function () {
        console.log("wait...");
    }, 5000);
}

function bindCustomerReviewButton() {
    if ($("#CustomerReviewButton").length) {
        $(document)
            .delegate("#CustomerReviewButton",
                "click",
                function (event) {
                    $.post("/create_review")
                        .done(function (data) {
                            var url = "/create_review?company_id=" + webinarId;
                            var _width = "600",
                                _height = "450";

                            $.colorbox({
                                iframe: true, fixed: true, width: _width, height: _height, scrolling: false, href: url
                            });

                        });


                });

    }
}

$.fn.serializeObject = function () {
    var o = {};
    var a = this.serializeArray();

    $.each(a, function () {
        var itemName = this.name;


        if (o[itemName]) {
            if (!o[itemName].push) {
                o[itemName] = [o[itemName]];
            }
            o[itemName].push(this.value || '');
        } else {
            o[itemName] = this.value || '';
        }
    });
    return o;
};
