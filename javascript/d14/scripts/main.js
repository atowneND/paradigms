// Ashley Towne
// 03/30/2016
// d14

function Item() {
    this.addToDocument=function(){
        document.body.appendChild(this.item);
    };
};

function Label() {
    this.createLabel = function(text, id){
        this.item = document.createElement("p");
        this.item.setAttribute(id, text);
        this.addToDocument();
    };
    this.setText = function(text){
        this.item.textContent = text;
        this.addToDocument();
    };
};

function Button() {
    this.createButton = function(text, id){
        this.item = document.createElement("button");
        this.item.setAttribute(id, text);
        var labelText = document.createTextNode(text);
        this.item.appendChild(labelText);
        this.addToDocument();
    };
    this.addClickEventHandler = function(handler, args){
        this.item.onmouseup = function() { handler(args); };
    };
};
function changeText(args){
    args[1].setText(args[0]);
};

Label.prototype = new Item();
Button.prototype = new Item();

button = new Button();
label = new Label();

button.createButton("CLICK HERE","theButton");

label.createLabel("guess who", "theLabel");
label.setText("who?");

args = ["Ashley Towne", label]
button.addClickEventHandler(changeText, args);

var xhttp = new XMLHttpRequest();
movie = xhttp.open("GET","http://student02.cse.nd.edu:40001/movies/32");
xhttp.onload = function(){
    args = [xhttp.responseText, label];
    changeText(args);
}
xhttp.send()
