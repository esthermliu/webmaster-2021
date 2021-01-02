window.onscroll = function() { // When the user scrolls
    scrollFunction(); // The scroll function will be called
};

// Scroll function
function scrollFunction() {
if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) { // If the body is greater than 100 from the top
	document.getElementById("mybtn").style.display = "block"; // Display the button
  } else {
	document.getElementById("mybtn").style.display = "none"; // Otherwise do not display the button
  }
}

$("a[href='#']").click(function() { // When you click the button with an href of #
  $("html, body").animate({ scrollTop: 0 }, "slow"); // Scroll to the top
  return false;
});
