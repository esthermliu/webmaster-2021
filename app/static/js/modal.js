function modal(id, btn_id) {
    console.log("Modal Opened")

    var modal = document.getElementById(id);
    var btn = document.getElementById(btn_id);
    //var span = document.getElementById(span_id);

    modal.style.display = "flex";
    //span.onclick = close => modal.style.display = "none";

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

}
