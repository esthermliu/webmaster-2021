$(window).on('load', function(){
    $('.featuredContainer').slick({
        centerMode: true,
        centerPadding: '20px',
        autoplay: true,
        dots: true,
        autoplaySpeed: 3000,
        prevArrow: $('.featurePrev'),
        nextArrow: $('.featureNext'),
        slidesToShow: 3
    });
      
  });


  
  
  