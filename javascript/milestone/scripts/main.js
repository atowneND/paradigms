// Ashley Towne
// 03/30/2016
// d14

Label.prototype = new Item();
Button.prototype = new Item();
Dropdown.prototype = new Item();
Image.prototype = new Item();

var user_id = 95;

label = new Label();
label.createLabel("title", "theLabel");
label.setText("Title of movie");

upbutton = new Button();
upbutton.createButton("UP","upButton");

movie_img = new Image();
movie_img.createImage();

downbutton = new Button();
downbutton.createButton("DOWN","downButton");

rating_label = new Label();
rating_label.createLabel("rating","ratingLabel");
rating_label.setText("Rating of movie");

args = [label, rating_label, user_id]
upbutton.addClickEventHandler(upvote, args);
downbutton.addClickEventHandler(downvote, args);

updatePage(args);

