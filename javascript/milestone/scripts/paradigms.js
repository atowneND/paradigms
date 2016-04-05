// Ashley Towne
// 03/30/2016
// d14 library

function Item() {
    this.addToDocument=function(){
        console.log(this);
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

function upvote(args){
    submitVote([5, args[2]]);
    updatePage(args);
};

function downvote(args){
    submitVote([1, args[2]]);
    updatePage(args);
};

function updatePage(args){
    var user_id = args[2];

    get_mid(
        user_id,
        function (movie_id) {
            var xhttp_title = new XMLHttpRequest();
            xhttp_title.open("GET","http://student02.cse.nd.edu:40092/movies/"+movie_id.toString());
            xhttp_title.send();

            var xhttp_rating = new XMLHttpRequest();
            xhttp_rating.open("GET","http://student02.cse.nd.edu:40092/ratings/"+movie_id.toString());
            xhttp_rating.send();

            xhttp_title.onload = function(){
                changeText([args[0], xhttp_title, "title"]);
            };
            xhttp_rating.onload = function(){
                changeText([args[1], xhttp_rating, "rating"]);
            };
        }
    );

};

function changeText(args){
    args[0].setText(JSON.parse(args[1].responseText)[args[2]]);
};

function submitVote(args){
    var rat = args[0];
    var user_id = args[1];
    get_mid(
        user_id,
        function (movie_id) { 
            var url = "http://student02.cse.nd.edu:40092/recommendations/"+user_id.toString();
            var http = new XMLHttpRequest();

            http.open("PUT", url, true);
            http.send(JSON.stringify({"rating":rat, "movie_id": movie_id, "apikey": "DERP"}));
        }
    );

};

function get_mid(args,fn){
    var user_id = args;

    var xhttp_rec = new XMLHttpRequest();
    xhttp_rec.open("GET","http://student02.cse.nd.edu:40092/recommendations/"+user_id);
    xhttp_rec.send();

    xhttp_rec.onload = function(){
        var mid = JSON.parse(xhttp_rec.responseText)["movie_id"];
        fn(mid);
    };
};
