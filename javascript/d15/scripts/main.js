// Ashley Towne
// 03/30/2016
// d14

Label.prototype = new Item();
Button.prototype = new Item();
Dropdown.prototype = new Item();

button = new Button();
button.createButton("CLICK HERE","theButton");

label = new Label();
label.createLabel("guess who", "theLabel");
label.setText("Which movie?");

rating_label = new Label();
rating_label.createLabel("foo","ratingLabel");
rating_label.setText("");

drop = new Dropdown();
var vote_dict = {1:"Just Plain Bad", 2:"Not So Good", 3: "OK I guess", 4:"Pretty Good", 5:"Awesome!"};
drop.createDropdown(vote_dict,"yo","Awesome!");

vote_button = new Button();
vote_button.createButton("Vote","voteButton");

args = [label, rating_label]
button.addClickEventHandler(changeText, args);
args = [drop]
vote_button.addClickEventHandler(submitVote, args);

var xhttp = new XMLHttpRequest();
movie = xhttp.open("GET","http://student02.cse.nd.edu:40001/movies/32");

var xhr = new XMLHttpRequest();
rating = xhr.open("GET","http://student02.cse.nd.edu:40001/ratings/32");

//xhttp.onload = function(handler,args){
//    return handler(args);
//}
//xhr.onload = function(handler,args){
//    return handler(args);
//}

xhttp.send()
xhr.send()


