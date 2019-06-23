$(function () {
  slideAnime();
  $(".slide").first().addClass("active");

})


function slideAnime() {
  $(".next, .prev").on('click', function() {
    var $this = $(this),
      slide = $(".slide"),
      curActive = $(".viewport").find(".active"),
      position = $(".viewport").children().index(curActive)
      slideNum = $(".slide").length;

      if ($this.hasClass("next")) {
        if (position < slideNum - 1) {
          curActive.removeClass("active").next().addClass("active");
        } else {
          curActive.removeClass("active");
          slide.first().addClass("active");
        }
      } else {

          if (position != 0) {
            curActive.removeClass("active").prev().addClass("active");
          } else {
            curActive.removeClass("active");
            slide.last().addClass("active")
          }

      }


  })

}
