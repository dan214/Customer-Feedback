$(document).ready(function() {

     $('.reviews').bxSlider({
        speed: 500,
        auto: true,
        controls: true,
        captions: false,
        pager: true,
        nextText: '',
        prevText: '',
        mode: 'vertical'


    });

    $('.reviews').bxSlider({
        speed: 'fast',
        auto: true,
        controls: true,
        captions: false,
        pager: true,
        nextText: '',
        prevText: '',
        mode: 'vertical',
        onSliderLoad: function () {

            $(".holder").css({ display: "block" });

        }
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