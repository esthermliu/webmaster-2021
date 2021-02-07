$(window).on('load', function(){
    $('.featuredContainer2').slick({
        centerMode: true,
        centerPadding: '20px',
        autoplay: true,
        dots: true,
        autoplaySpeed: 3000,
        prevArrow: $('.featurePrev'),
        nextArrow: $('.featureNext'),
        slidesToShow: 3,
        responsive: [{
            breakpoint: 1050,
            settings: {
                slidesToShow: 1            
            }
        }]
    });

    $('.featuredContainer2').show();
    $('.featurePrev').show();
    $('.featureNext').show();
      
  });


  
  
  