(function ($) {

var $window = $(window),
		$this = $(this);

$window.scroll(function(){

		var wScroll = $this.scrollTop(),
		$featureListPod = $(".featureList .pod"),
		$about = $(".about"),
		$description = $(".about .description"),
		$display = $(".about .display"),
		$headerInfo = $(".headerInfo");

		
		//about scroll
		if(wScroll > $headerInfo.offset().top - $window.height()){

		var opacity = (-wScroll/10) + 10 ;

		$headerInfo.css({'opacity': opacity});

		}
		//end of about scroll

		//about scroll
		if(wScroll > $about.offset().top - $window.height()){

		var offset = (Math.min(0, wScroll - $about.offset().top +$(window).height() - 550)).toFixed();

		$display.css({'transform': 'translate('+ offset +'px, '+ Math.abs(offset * 0.2) +'px)'});

		$description.css({'transform': 'translate('+ Math.abs(offset) +'px, '+ Math.abs(offset * 0.2) +'px)'});

		}
		//end of about scroll
		
		//feature scroll	
		if(wScroll > $(".featureList").offset().top - ($window.height() / 1.95)){

			$featureListPod.each(function(i){

				setTimeout(function(){
				$featureListPod.eq(i).addClass("show");
				}, (700 * (Math.exp(i * 0.14))) - 700);
			});
		}
		//end of feature scroll


});


}) (jQuery);
