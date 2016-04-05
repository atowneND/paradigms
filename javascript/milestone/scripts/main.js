// Ashley Towne
// 03/30/2016
// d14

Label.prototype = new Item();
Button.prototype = new Item();
Dropdown.prototype = new Item();
Image.prototype = new Item();

var hostname = "student02.cse.nd.edu"

var xhttp = new XMLHttpRequest();
movie = xhttp.open("GET","http://student02.cse.nd.edu:40092/movies/32");

var xhr = new XMLHttpRequest();
rating = xhr.open("GET","http://student02.cse.nd.edu:40092/ratings/32");

label = new Label();
label.createLabel("title", "theLabel");
label.setText("Title of movie");

upbutton = new Button();
upbutton.createButton("UP","upButton");

movie_img = new Image();
movie_img.createImage(xhttp);

downbutton = new Button();
downbutton.createButton("DOWN","downButton");

rating_label = new Label();
rating_label.createLabel("rating","ratingLabel");
rating_label.setText("Rating of movie");

args = [label, rating_label]
upbutton.addClickEventHandler(changeText, args);
downbutton.addClickEventHandler(changeText, args);

xhttp.send()
xhr.send()


