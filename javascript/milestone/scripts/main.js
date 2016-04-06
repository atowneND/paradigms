// Ashley Towne
// 03/30/2016
// d14
//

function upvote(args){
    var title_label = args[0]
    var rating_label = args[1]
    var user_id = args[2]
    var desired_rating = 5;
    submitVote([desired_rating, rating_label, user_id]);
    updatePage(args);
};

function downvote(args){
    var title_label = args[0]
    var rating_label = args[1]
    var user_id = args[2]
    var desired_rating = 1;
    submitVote([desired_rating, rating_label, user_id]);
    updatePage(args);
};

window.onload = function() {
    Label.prototype = new Item();
    Div.prototype = new Item();
    Button.prototype = new Item();
    Dropdown.prototype = new Item();
    Image.prototype = new Item();

    var user_id = 85;

    titleLabel = new Label();
    titleLabel.createLabel("title", "theLabel", "div1");
    titleLabel.setText("Title of movie");
    titleLabelDiv = new Div();
    titleLabelDiv.createDiv("div1");
    titleLabelDiv.addToDiv(titleLabel);

    upbutton = new Button();
    upbutton.createButton(" UP ","upButton");

    movie_img = new Image();
    movie_img.createImage();

    downbutton = new Button();
    downbutton.createButton("DOWN","downButton");

    movieImgDiv = new Div();
    movieImgDiv.createDiv("movie_img");
    movieImgDiv.addToDiv(upbutton);
    movieImgDiv.addToDiv(movie_img);
    movieImgDiv.addToDiv(downbutton);

    ratingLabel = new Label();
    ratingLabel.createLabel("rating","ratingLabel");
    ratingLabel.setText("Rating of movie");
    ratingLabelDiv = new Div();
    ratingLabelDiv.createDiv("div1");
    ratingLabelDiv.addToDiv(ratingLabel);

    args = [titleLabel, ratingLabel, user_id, movie_img]
    upbutton.addClickEventHandler(upvote, args);
    downbutton.addClickEventHandler(downvote, args);

    updatePage(args);
};

