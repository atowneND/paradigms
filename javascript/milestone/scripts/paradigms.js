// Ashley Towne
// 03/30/2016
// d14 library

function Item() {
    this.addToDocument=function(){
        document.body.appendChild(this.item);
    };
};

function Div() {
    this.createDiv = function(div_id){
        this.item = document.createElement("div");
        this.item.id = div_id;
    };
    this.addToDiv = function(child_obj){
        this.item.appendChild(child_obj.item);
        this.addToDocument();
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
    };
};

function Button() {
    this.createButton = function(text, id){
        this.item = document.createElement("button");
        this.item.id = id;
        var labelText = document.createTextNode(text);
        this.item.appendChild(labelText);
        this.addToDocument();
    };
    this.addClickEventHandler = function(handler, args){
        this.item.onclick = function() { handler(args); };
    };
};

function Dropdown() {
    this.createDropdown = function(dict,id,selected){
        this.item = document.createElement("select");
        this.item.setAttribute(id,"hi");
        for (var item in dict){
            var option = document.createElement("option");
            option.text = dict[item];
            this.item.add(option);
        }
        this.item.value = selected;
        this.addToDocument();
    };
    this.getSelected = function(){
        return this.item.options[this.item.selectedIndex].value;
    };
};

function Image(){
    this.createImage = function(){
        this.item = document.createElement("img");
        this.item.src = "/~cmc/teaching/cse30332_sp16/images/dCTuPRukbDs3mOSx9SD0PCMRd2g.jpg"
        this.addToDocument();
    };
};

function updatePage(args){
    console.log("this was claled");
    var title_label = args[0];
    var rating_label = args[1];
    var user_id = args[2];
    var movie_img = args[3];

    get_mid(
        user_id,
        function (movie_id) {
            console.log("This is our movie id: " + movie_id);
            // Save rating
            rating_label.movie_id = movie_id;

            // Update title and rating
            var xhttp_title = new XMLHttpRequest();
            xhttp_title.open("GET","http://student02.cse.nd.edu:40092/movies/"+movie_id.toString());

            var xhttp_rating = new XMLHttpRequest();
            xhttp_rating.open("GET","http://student02.cse.nd.edu:40092/ratings/"+movie_id.toString());

            xhttp_title.onload = function(){
                changeText([title_label, xhttp_title, "title"]);
                movie_img.item.src = "/~cmc/teaching/cse30332_sp16/images"+JSON.parse(xhttp_title.responseText)["img"];
            };
            xhttp_rating.onload = function(){
                changeText([rating_label, xhttp_rating, "rating"]);
            };

            xhttp_title.send();
            xhttp_rating.send();
        }
    );

};

function changeText(args){
    args[0].setText(JSON.parse(args[1].responseText)[args[2]]);
};

function submitVote(args){
    var rat = args[0];
    var rating_label = args[1];
    var user_id = args[2];
    var url = "http://student02.cse.nd.edu:40092/recommendations/"+user_id.toString();
    var http = new XMLHttpRequest();

    http.open("PUT", url, true);
    http.onload = function(){
        updatePage(args[3])
    };
    http.send(JSON.stringify({"rating":rat, "movie_id": rating_label.movie_id, "apikey": "DERP"}));

};

function get_mid(user_id,fn){
    var xhttp_rec = new XMLHttpRequest();
    xhttp_rec.open("GET","http://student02.cse.nd.edu:40092/recommendations/"+user_id);

    xhttp_rec.onload = function(){
        var mid = JSON.parse(xhttp_rec.responseText)["movie_id"];
        fn(mid);
    };

    xhttp_rec.send();
};
