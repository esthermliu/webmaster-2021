jQuery(document).ready(function($){
	$('.navbar').css("background-color", "transparent");
	if ($(this).scrollTop() < 190) {
		$('.navbar').css("background-color", "transparent");
        $('.navbar').css("height", "110px");
        $('.navbar').css("box-shadow", "0 0px 0px 0px rgba(0,0,0,.6)");
        $('.dropDownContentAbout').css("transform", "translate(0px, 0px)");
        $('.dropDownContentOverview').css("transform", "translate(0px, 0px)");
        $('.dropDownContentMedia').css("transform", "translate(0px, 0px)");
        
		$('.dropDownContentAbout').css("background-color", "rgb(23, 37, 42)");
		$('.dropDownContentOverview').css("background-color", "rgb(23, 37, 42)");
		$('.dropDownContentMedia').css("background-color", "rgb(23, 37, 42)");
        
        $('.dropButtonAbout a').css("color", "white");
		$('.dropButtonOverview a').css("color", "white");
		$('.dropButtonMedia a').css("color", "white");
		
		$('.dropDownContentAbout').css("box-shadow", "none");
		$('.dropDownContentOverview').css("box-shadow", "none");
        $('.dropDownContentMedia').css("box-shadow", "none");
        
        $('.logoWhite').css("display", "flex");
        $('.logoDark').css("display", "none");
	} else {
		$('.navbar').css("background-color", "rgba(255, 255, 255, 1)");
        $('.dropDownContentAbout').css("transform", "translate(0px, -13px)");
        $('.dropDownContentOverview').css("transform", "translate(0px, -13px)");
        $('.dropDownContentMedia').css("transform", "translate(0px, -13px)");
		$('.dropButtonAbout a').css("color", "rgba(23, 37, 42, 1)");
		$('.dropButtonOverview a').css("color", "rgba(23, 37, 42, 1)");
		$('.dropButtonMedia a').css("color", "rgba(23, 37, 42, 1)");
		$('.homepageLogo').css("color", "rgba(23, 37, 42, 1)");
        $('.homepageLogo p').css("color", "rgba(23, 37, 42, 1)");
        $('.homepageLogo i').css("color", "rgba(23, 37, 42, 1)");
        $('.navbar').css("height", "85px");
        
        $('.navbar').css("box-shadow", "0 4px 10px -10px rgba(0,0,0,.6)");

        $('.logoWhite').css("display", "none");
        $('.logoDark').css("display", "flex");
        
        $('.dropDownContentAbout').css("box-shadow", "0 35px 80px -40px rgba(0,0,0,.45)");
		$('.dropDownContentOverview').css("box-shadow", "0 35px 80px -40px rgba(0,0,0,.45)");
		$('.dropDownContentMedia').css("box-shadow", "0 35px 80px -40px rgba(0,0,0,.45)");
	}
	$(window).scroll(function(){
		if ($(this).scrollTop() < 190) {
			$('.navbar').css("background-color", "transparent");
            $('.navbar').css("height", "110px");
            $('.navbar').css("box-shadow", "0 0px 0px 0px rgba(0,0,0,.6)");
            $('.dropDownContentAbout').css("transform", "translate(0px, 0px)");
            $('.dropDownContentOverview').css("transform", "translate(0px, 0px)");
            $('.dropDownContentMedia').css("transform", "translate(0px, 0px)");
            
			$('.dropDownContentAbout').css("background-color", "rgb(23, 37, 42)");
			$('.dropDownContentOverview').css("background-color", "rgb(23, 37, 42)");
			$('.dropDownContentMedia').css("background-color", "rgb(23, 37, 42)");
            
            $('.dropButtonAbout a').css("color", "white");
		    $('.dropButtonOverview a').css("color", "white");
		    $('.dropButtonMedia a').css("color", "white");
            $('.homepageLogo').css("color", "white");
            $('.homepageLogo p').css("color", "white");
            $('.homepageLogo i').css("color", "white");
			
			$('.dropDownContentAbout').css("box-shadow", "none");
			$('.dropDownContentOverview').css("box-shadow", "none");
            $('.dropDownContentMedia').css("box-shadow", "none");
            
            $('.logoWhite').css("display", "flex");
            $('.logoDark').css("display", "none");
		} else {
			$('.navbar').css("background-color", "rgba(255, 255, 255, 1)");
            $('.navbar').css("height", "85px");
            $('.dropDownContentAbout').css("transform", "translate(0px, -13px)");
            $('.dropDownContentOverview').css("transform", "translate(0px, -13px)");
            $('.dropDownContentMedia').css("transform", "translate(0px, -13px)");
            
            $('.dropButtonAbout a').css("color", "rgba(23, 37, 42, 1)");
		    $('.dropButtonOverview a').css("color", "rgba(23, 37, 42, 1)");
		    $('.dropButtonMedia a').css("color", "rgba(23, 37, 42, 1)");
            $('.homepageLogo').css("color", "rgba(23, 37, 42, 1)");
            $('.homepageLogo p').css("color", "rgba(23, 37, 42, 1)");
            $('.homepageLogo i').css("color", "rgba(23, 37, 42, 1)");
            
            $('.navbar').css("box-shadow", "0 4px 10px -10px rgba(0,0,0,.6)");
            
            $('.dropDownContentAbout').css("box-shadow", "0 35px 80px -40px rgba(0,0,0,.45)");
		    $('.dropDownContentOverview').css("box-shadow", "0 35px 80px -40px rgba(0,0,0,.45)");
            $('.dropDownContentMedia').css("box-shadow", "0 35px 80px -40px rgba(0,0,0,.45)");
            
            $('.logoWhite').css("display", "none");
            $('.logoDark').css("display", "flex");
		    
			/*$('.dropDownContentAbout').css("background-color", "rgba(225, 225, 225, 1)");
			$('.dropDownContentOverview').css("background-color", "rgba(225, 225, 225, 1)");
			$('.dropDownContentMedia').css("background-color", "rgba(225, 225, 225, 1)");*/
		}
		
		if ($(this).scrollTop() > 190) {
			$('.navbar').css("background-color", "rgba(255, 255, 255, 1)");
            $('.navbar').css("height", "85px");
            $('.dropDownContentAbout').css("transform", "translate(0px, -13px)");
            $('.dropDownContentOverview').css("transform", "translate(0px, -13px)");
            $('.dropDownContentMedia').css("transform", "translate(0px, -13px)");
            
            $('.dropButtonAbout a').css("color", "rgba(23, 37, 42, 1)");
		    $('.dropButtonOverview a').css("color", "rgba(23, 37, 42, 1)");
		    $('.dropButtonMedia a').css("color", "rgba(23, 37, 42, 1)");
            $('.homepageLogo').css("color", "rgba(23, 37, 42, 1)");
            $('.homepageLogo p').css("color", "rgba(23, 37, 42, 1)");
            $('.homepageLogo i').css("color", "rgba(23, 37, 42, 1)");
            
            $('.navbar').css("box-shadow", "0 4px 10px -10px rgba(0,0,0,.6)");
            
            $('.dropDownContentAbout').css("box-shadow", "0 35px 80px -40px rgba(0,0,0,.45)");
		    $('.dropDownContentOverview').css("box-shadow", "0 35px 80px -40px rgba(0,0,0,.45)");
            $('.dropDownContentMedia').css("box-shadow", "0 35px 80px -40px rgba(0,0,0,.45)");
            
            $('.logoWhite').css("display", "none");
            $('.logoDark').css("display", "flex");
		} else {
			$('.navbar').css("background-color", "transparent");
            $('.navbar').css("height", "110px");
            $('.navbar').css("box-shadow", "0 0px 0px 0px rgba(0,0,0,.6)");
            $('.dropDownContentAbout').css("transform", "translate(0px, 0px)");
            $('.dropDownContentOverview').css("transform", "translate(0px, 0px)");
            $('.dropDownContentMedia').css("transform", "translate(0px, 0px)");
            
			$('.dropDownContentAbout').css("background-color", "rgb(23, 37, 42)");
			$('.dropDownContentOverview').css("background-color", "rgb(23, 37, 42)");
			$('.dropDownContentMedia').css("background-color", "rgb(23, 37, 42)");
            
            $('.dropButtonAbout a').css("color", "white");
		    $('.dropButtonOverview a').css("color", "white");
		    $('.dropButtonMedia a').css("color", "white");
            $('.homepageLogo').css("color", "white");
            $('.homepageLogo p').css("color", "white");
            $('.homepageLogo i').css("color", "white");
			
			$('.dropDownContentAbout').css("box-shadow", "none");
			$('.dropDownContentOverview').css("box-shadow", "none");
            $('.dropDownContentMedia').css("box-shadow", "none");
            
            $('.logoWhite').css("display", "flex");
            $('.logoDark').css("display", "none");
		}
		

	});
});
