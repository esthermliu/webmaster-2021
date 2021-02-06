$('.topicLink').on('click', function(){
    $(".serviceLink").removeClass("firstLink");

    var target = $(this).attr('rel');
    console.log(target);
    var target_class = $(this).attr('class');
    var target_id = $(this).attr('id');
    console.log(target_class);
    $("#"+ target).show().siblings("div").hide();
    var secondClass = $('#' + target_id).attr('class').split(' ')[1]
    console.log(secondClass);
    $("." + secondClass).addClass("currentTopic").siblings("a").removeClass("currentTopic");
});

