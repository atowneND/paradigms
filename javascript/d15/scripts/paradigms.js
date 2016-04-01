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

function changeText(args){
    args[0].setText(xhttp.responseText);
    args[1].setText(JSON.parse(xhr.responseText)["rating"]);
};

function submitVote(args){
    var rating = args[0].getSelected();
    if (rating=="Just Plain Bad"){
        rat = 1;
    }else if (rating=="Not So Good"){
        rat = 2;
    }else if (rating=="OK I guess"){
        rat = 3;
    }else if (rating=="Pretty Good"){
        rat = 4;
    }else if (rating=="Awesome!"){
        rat = 5;
    }
    var url = "http://student02.cse.nd.edu:40001/recommendations/95";
    http = new XMLHttpRequest();
    var params = "rating="+rating;
    http.open("PUT", url, true);
    http.send(JSON.stringify({"rating":rat, "movie_id": 32, "apikey": "DERP"}));
};
