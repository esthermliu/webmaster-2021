$("a[href='#treatments']").click(function() {
    $([document.documentElement, document.body]).animate({
        scrollTop: $("#treatmentSection").offset().top - $("#secondBox").height()
    }, 800);
})