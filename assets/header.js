document.addEventListener("DOMContentLoaded", Object(setTimeout(function () {
    

    var accueil = document.getElementById("Accueil");
    var graphique = document.getElementById("Graphique");
    var jupyter = document.getElementById("Jupyter-Notebook");
    var github = document.getElementById("Github");


    console.log(accueil, graphique, jupyter); 

    accueil.addEventListener("mouseover", function(event) {
        console.log(event);
        accueil.children[0].src = "/assets/icon/house_white.svg";
    })

    accueil.addEventListener("mouseout", function(event) {
        console.log(event);
        accueil.children[0].src = "/assets/icon/house_purple.svg";
    })


    graphique.addEventListener("mouseover", function(event) {
        console.log(event);
        graphique.children[0].src = "/assets/icon/chart_white.svg";
    })

    graphique.addEventListener("mouseout", function(event) {
        console.log(event);
        graphique.children[0].src = "/assets/icon/chart.svg";
    })

    jupyter.addEventListener("mouseover", function(event) {
        console.log(event);
        jupyter.children[0].src = "/assets/icon/python_fill_white.svg";
    })

    jupyter.addEventListener("mouseout", function(event) {
        console.log(event);
        jupyter.children[0].src = "/assets/icon/python_fill_purple.svg";
    })

    github.addEventListener("mouseover", function(event) {
        console.log(event);
        github.children[0].src = "/assets/icon/github_white.svg";
    })

    github.addEventListener("mouseout", function(event) {
        console.log(event);
        github.children[0].src = "/assets/icon/github_purple.svg";
    })

}, 1000)))


