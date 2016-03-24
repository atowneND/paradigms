// "this"
// - refers to the class if you are defining one using NEW
// - refers to the global ("window") context if not
// code from "var bird....new Bird();" is a library
// librar.js
var bird = {this.fly=function(){alert("flapflap");}}
var duck = {this.quack=function(){alert("quack v1");}}

Duck.prototype = new Bird(); // for chrome

//Duck. prototype = Bird; // only for firefox
// use new only for label and button
// import statement:  in HTML
// main.js
var fts = new duck();
fts.quack();
fts.fly();

// ajax.js
var label = document.createElement("p");
label.setAttribute("id","theP");
label.innerHTML="humbug"
document.body.appendChild(label)

var xhr = new XMLHttpRequest();
xhr.open("GET","http://uinames.com/api/?amount=1",true);
xhr.onload=function(e){
    label.innerHTML=xhr.responseText; // + error handling
}
xhr.onerror=function(e){console.log(xhr.statusText);}
xhr.send()
// xml=extensible market language

// xmlHttpRequest()

// associated html
// <html>
//      <head>
//          Title
//      </head>
//      <body>
//          <script type="text/javascript" src="scripts/library.js"></script>
//          <script type="text/javascript" src="scripts/main.js"></script>
//      </body>
// </html>
