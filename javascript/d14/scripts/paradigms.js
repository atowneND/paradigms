// Ashley Towne
// 03/30/2016
// d14 library

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
    //args[0].setText(JSON.parse(xhttp.responseText)["title"]);
    args[0].setText(xhttp.responseText);
};
