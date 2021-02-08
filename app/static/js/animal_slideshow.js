$(document).ready(function(){
    $('.animal1').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        adaptiveHeight: true,
        asNavFor: '.animal1For'
        
    }); 
    $('.animal1For').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.animal1',
        dots: true,
        centerMode: true,
        focusOnSelect: true,
        adaptiveHeight: true,
        prevArrow: $('.1Prev'),
        nextArrow: $('.1Next'),
        responsive: [{
            breakpoint: 600,
            settings: {
                slidesToShow: 1            
            }
        }]   
    }); 
    
    $('.animal2').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        adaptiveHeight: true,
        asNavFor: '.animal2For'
        
    }); 
    $('.animal2For').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.animal2',
        dots: true,
        centerMode: true,
        focusOnSelect: true,
        adaptiveHeight: true,
        prevArrow: $('.2Prev'),
        nextArrow: $('.2Next'),
        responsive: [{
            breakpoint: 600,
            settings: {
                slidesToShow: 1            
            }
        }]   
    });
   
    
});


  
  
  