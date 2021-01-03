$(document).ready(function(){
    $('.slideshowContainer').slick({
      dots: true,
      prevArrow: $('.prev'),
      nextArrow: $('.next'),
      autoplay: true,
      autoplaySpeed: 5000
    });
      
    $(".slideshowContainer").on("beforeChange", function() {
  
      /*$('.slideTitle').removeClass('fadeInUp').hide();
      setTimeout(() => {    
      $('.slideTitle').addClass('fadeInUp').show();
      }, 1000);
        
      $('.slideCaption').removeClass('fadeInUp').hide();
      setTimeout(() => {    
      $('.slideCaption').addClass('fadeInUp').show();
      }, 1000);
        
      $('.learnMoreContainer').removeClass('fadeInUp').hide();
      setTimeout(() => {    
      $('.learnMoreContainer').addClass('fadeInUp').show();
      }, 1000);*/
      
      $('.slideTitle').removeClass('fadeInDown').hide();
      setTimeout(() => {    
      $('.slideTitle').addClass('fadeInDown').show();
      }, 800);
        
      $('.slideCaption').removeClass('fadeInUp').hide();
      setTimeout(() => {    
      $('.slideCaption').addClass('fadeInUp').show();
      }, 800);
        
      $('.learnMoreContainer').removeClass('fadeInUp').hide();
      setTimeout(() => {    
      $('.learnMoreContainer').addClass('fadeInUp').show();
      }, 800);
        
    })
      
  });
  
  
  