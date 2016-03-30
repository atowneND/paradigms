// Ashley Towne
// 03/30/2016
// d14

Label.prototype = new Item();
Button.prototype = new Item();

button = new Button();
label = new Label();

button.createButton("CLICK HERE","theButton");

label.createLabel("guess who", "theLabel");
label.setText("who?");

args = [label]
button.addClickEventHandler(changeText, args);

var xhttp = new XMLHttpRequest();
movie = xhttp.open("GET","http://student02.cse.nd.edu:40001/movies/32");
xhttp.onload = (function(handler,args){
    return function() { handler(args); };
})(changeText,args);

xhttp.send()
