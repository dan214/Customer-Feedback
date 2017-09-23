$(document).ready(function() {

    $(".lorem").hide();
    $(".lorem").fadeIn(6000);

    $('.reviews').bxSlider({
        speed: 10000,
        controls: true,
        captions: true,
        pager: false,
        ticker:true,
        mode: 'vertical',
    });




});

    $(document).delegate("#CustomerReviewButton", "click", function (event) {
        var url = $(this).attr('href');
        event.preventDefault();
        var url = $(this).attr('href');
        var _width = "560px",
            _height = "540px";
        $.colorbox({
            iframe: true, fixed: true, width: _width, height: _height, scrolling: false, href: url
        });
    });

function animateContent(direction) {  
    var animationOffset = $('.company').height() - $('.reviews').height()-30;
    if (direction == 'up') {
        animationOffset = 0;
    }

    console.log("animationOffset:"+animationOffset);
    $('.reviews').animate({ "marginTop": (animationOffset)+ "px" }, 5000);
}

function up(){
    animateContent("up")
}
function down(){
    animateContent("down")
}

function start(){
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

function bindCustomerReviewButton(){
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
            iframe: true, fixed: true, width: _width, height: _height, scrolling: false, href: url});

    });


                });

    }
}