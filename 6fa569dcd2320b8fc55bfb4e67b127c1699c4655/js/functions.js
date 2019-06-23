(function ($) {

var $window = $(window),
		$this = $(this);

$window.scroll(function(){

		var wScroll = $this.scrollTop(),
		$onroll = $(".onroll");
		$onroll2 = $(".onroll.two");
		$onroll3 = $(".onroll.three");

		//about scroll
if(wScroll > $onroll.offset().top - ($window.height() / 1.2)){

		var opacity = (-wScroll * -1) - 359 ;

		$onroll.css({'opacity': opacity});

		}
		//end of about scroll

		//about scroll
if(wScroll > $onroll2.offset().top - ($window.height() / 0.6)){

		var opacity = (-wScroll * -1) - 559 ;

		$onroll2.css({'opacity': opacity});

		}
		//end of about scroll


});
}) (jQuery);
