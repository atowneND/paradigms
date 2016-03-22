var label = document.createElement("p");
label.setAttribute("id","thelabel");
var labelText = document.createTextNode("Who?");
label.appendChild(labelText);
document.body.appendChild(label);

var button = document.getElementById("thebutton");

function mouseup() {
    labelText.textContent="Ashley";
}
button.onclick = mouseup
