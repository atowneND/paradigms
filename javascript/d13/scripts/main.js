// Ashley Towne
// 03/23/2016
// d13

var Item = {addToDocument:function(){
                document.body.appendChild(this.item); },
           };

var Label = {createLabel:function(text, id){
                this.item = document.createElement("p");
                this.item.setAttribute(id, text);
                this.addToDocument();},
             setText:function(text){
                this.item.textContent = text;
                this.addToDocument();},
            };

var Button = {createButton:function(text, id){
                this.item = document.createElement("button");
                this.item.setAttribute(id, text);
                var labelText = document.createTextNode(text);
                this.item.appendChild(labelText);
                this.addToDocument();},
              addClickEventHandler:function(handler, args){
                 this.item.onmouseup = function() { handler(args); };
                 },
             }
function changeText(args){
    args[1].setText(args[0]);
}

Label.__proto__ = Item;
Button.__proto__ = Item;

Button.createButton("CLICK HERE","theButon");

Label.createLabel("guess who", "theLabel");
Label.setText("who?");
Label.addToDocument();

args = ["Ashley Towne", Label]
Button.addClickEventHandler(changeText, args);
