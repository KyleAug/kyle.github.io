$("label").click(function(){
  var imgId = $(this).attr("data-id");
 $(".display").removeClass("sidebar-active");
 $(".display"+"#"+imgId).addClass("sidebar-active");
});
