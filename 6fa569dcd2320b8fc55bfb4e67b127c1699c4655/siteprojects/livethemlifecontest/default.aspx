<%
Response.Status = "301 Moved Permanently"
Response.AddHeader ("Location", "/")
response.end
%>

<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="keywords" content="mgm mirage, las vegas, hotels,  resorts, spa, entertainment, dining, players club, instagram contest">
<meta name="description" content="MGM Resorts International is a collection of resort-casinos, residential living and retail developments providing unsurpassed service and amenities to every guest.">
        <title>#LiveTheMlife Instagram Contest</title>
        <link href='http://fonts.googleapis.com/css?family=Lato:400,900italic,900,700italic,700,400italic,300italic,100italic,300,100' rel='stylesheet' type='text/css'>
        <link href="assets/css/styles.css" rel="stylesheet" type="text/css">
       
    </head>

    <body>
    
    	<!-- This is the header component -->
    	<!--#include virtual="assets/includes/header.ascx" --> 
       	<!-- End of header component --> 
        
        <!-- This is the main content component -->
        <section id="main-content">
        	<article class="title">
            	<img src="assets/images/title-main-content.png" alt="M life">
            </article>
            <figure id="product" class="animatedParent animateOnce" data-sequence="500">
            	<img class="animated fadeInUpShort" data-id="1" src="assets/images/product-blurb.png" alt="Snap a Pic">
                <img class="animated fadeInUpShort" data-id="2" src="assets/images/iphone.png" alt="Cellphone">
                
              <div class="clear"></div>
                    <figcaption id="property-disclaimer">
                        <img src="assets/images/logo-mlife-white.png" alt="M life">
                        <h3>To enter on Instagram:<br>
                        #LiveTheMlife #Contest</h3>
                        <div class="clear"></div>  
                    </figcaption>  
            </figure>
            
        </section>
        
        <!-- This is the footer component -->
        <!--#include virtual="assets/includes/footer.ascx" -->
        <!-- End of footer component -->  
        
        <!--#include virtual="/include/tracking.ascx" -->
        
        <script src="https://code.jquery.com/jquery-2.1.3.min.js" type="text/javascript"></script>
        
        <script src="assets/js/animate-it.js" type="text/javascript"></script>
        <script type="text/javascript">
			$(function() {
				$(".header-wrap [href]").each(function() {
				if (this.href == window.location.href) {
					$(this).addClass("active");
					}
				});
			});
		</script>

    </body>
</html>
