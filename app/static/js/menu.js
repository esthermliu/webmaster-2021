function menuClicked(x) {
	x.classList.toggle("change");
	document.getElementById("navLinks").classList.toggle("openMenu");
}

function phoneNav(phone, minus, plus) {
    $(phone).toggle(500);
	$(minus).toggle(200);
	$(plus).toggle(200);
}