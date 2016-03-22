var Item = {addToDocument:function(){ document.body.appendChild(this.item); },
           };

var Label = {createLabel:function(text, id){
                var this.item = document.createElement("p");
                this.item.setAttribute(id, text);
                this.addToDocument();},
             setText:function(text){
                var labelText = document.createTextNode(text);
                this.item.appendChild(labelText);
                this.addToDocument();},
            };

var Button = {createButton:function(text, id){
                var this.item = document.createElement("button");
                this.item.setAttribute(id, text);
                this.addToDocument();},
              addClickEventHandler:function(handler, args){
                 this.item.onmouseup.function(){handler(args)};},
             }
function addClickEventHandler(args){alert(args[0]):}

Label.__proto__ = Item;
Button.__proto__ = Item;

Button.createButton("hi","id");

//var Label = document.createElement("l");
//
//// from class
//var label = document.createElement("p");
//label.setAttribute("id","theLabel");
//var labelText = document.createTextNode("who?");
//label.appendChild(labelText);
//document.body.appendChild(label);
//function changeText() {label.innerHTML="Patrick Flynn";}
//var Bird = {name:"Larry",
//            fly:function(){alert("flap");}}
//var duck = {name:"donald",
//            wingspan:"20",
//            quack:function(){alert("quacking");},
//            addClickHandler:function(hndlr,args){
//                document.getElementById("theButton").onmouseup.function(){hndlr(args);}
//                }
//            };
//duck.quack();
//duck.__proto__ = Bird;
//function showMyMessage(args){alert(args[0]):}
//duck.addClickHandler(showMyMessage,["my duck click"]);
//
//duck.fly();
//alert(Bird.name); "Larry"
//alert(duck.name); "Donald"
//
//// old assignment
//var label = document.createElement("p");
//label.setAttribute("id","thelabel");
//var labelText = document.createTextNode("Who?");
//label.appendChild(labelText);
//document.body.appendChild(label);
//
//var button = document.getElementById("thebutton");
//
//function mouseup() {
//    labelText.textContent="Ashley";
//}
//button.onclick = mouseup
