jQuery(window).scroll(function(){
  winScroll();
})

function winScroll() {
  var wScroll = jQuery(this).scrollTop();
  if (wScroll > 2 ) {
    jQuery(".controls-list").addClass("reveal")
  } else {
    jQuery(".controls-list").removeClass("reveal")
  }
};
