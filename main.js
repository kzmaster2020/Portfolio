$( document ).ready(function() {
    console.log( "ready!" );
    $('.gal-box').toggle();
    $('.zc-box').toggle();
    $('.uffc-box').toggle();
});

$('#zc-img').click(function(){
  $('.zc-box').fadeToggle("fast", "linear");

  $(window).scrollTop(0);
});

$('#x02').click(function(){
  $('.zc-box').fadeToggle("fast", "linear");
  $([document.documentElement, document.body]).animate({
        scrollTop: $("#zc-img").offset().top
    }, 500);
});

$('#arrow').click(function(){
  $('html').animate({scrollTop: "10px"});

});

$('#gal-img').click(function(){
  $('.gal-box').fadeToggle("fast", "linear");
  $(window).scrollTop(0);
});

$('#x01').click(function(){
  $('.gal-box').fadeToggle("fast", "linear");
  $([document.documentElement, document.body]).animate({
        scrollTop: $("#gal-img").offset().top
    }, 500);
});

$('#arrow').click(function(){
  $('html').animate({scrollTop: "10px"});

});

$('#uffc-img').click(function(){
  $('.uffc-box').fadeToggle("fast", "linear");
  $(window).scrollTop(0);
});

$('#x03').click(function(){
  $('.uffc-box').fadeToggle("fast", "linear");
  $([document.documentElement, document.body]).animate({
        scrollTop: $("#uffc-img").offset().top
    }, 500);
});

$('#arrow').click(function(){
  $('html').animate({scrollTop: "10px"});

});

var texts = [
  "Web Developer",
  "Game Programmer",
  "Artist",
  "Comic Creator",
  "Author",
  "Writer",
  "Dancer",
  "Instructor",
  "Voice Actor",
  "Animator",
  "Community Activist",
  "Graphic Designer",
  "Designer"
].reverse();


function textChange(){
  if (texts.length == 0){
    texts.push("Web Developer",
    "Game Programmer",
    "Artist",
    "Comic Creator",
    "Author",
    "Writer",
    "Dancer",
    "Instructor",
    "Voice Actor",
    "Animator",
    "Community Activist",
    "Graphic Designer",
    "Designer");
    textChange();
  }
  else {
    $('#text-change').html(texts.pop()).fadeIn(500).delay(1000).fadeOut(500, textChange);
  }
}


$('#text-change').ready(function(){
  textChange();
});
