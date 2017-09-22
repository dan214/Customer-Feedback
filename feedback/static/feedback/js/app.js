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