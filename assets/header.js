

setTimeout(function() {

    var ul = document.querySelector("ul.header.menu.nav-ul");
    var chemin = window.location.pathname;
    accueil = document.getElementById("Accueil");
    jupyter = document.getElementById("Jupyter-Notebook");
    compare = document.getElementById("Compare");
    github = document.getElementById("Github");


    if(chemin == "/plot") {
        globe = document.getElementById("Globe");
        rgraphique = document.getElementById("remove-graphique");
        ul.removeChild(rgraphique);

        globe.addEventListener("mouseover", function(event) {
            console.log(event);
            globe.children[0].src = "/assets/icon/globe_white.svg";
        })
    
        globe.addEventListener("mouseout", function(event) {
            console.log(event);
            globe.children[0].src = "/assets/icon/globe.svg";
        })

    }

    else if (chemin == "/map") {
        graphique = document.getElementById("Graphique");
        rglobe = document.getElementById("remove-globe");
        ul.removeChild(rglobe);

        graphique.addEventListener("mouseover", function(event) {
            console.log(event);
            graphique.children[0].src = "/assets/icon/chart_white.svg";
        })
    
        graphique.addEventListener("mouseout", function(event) {
            console.log(event);
            graphique.children[0].src = "/assets/icon/chart.svg";
        }) 
    }    
    else {
        graphique = document.getElementById("Graphique");
        globe = document.getElementById("Globe");

        graphique.addEventListener("mouseover", function(event) {
            console.log(event);
            graphique.children[0].src = "/assets/icon/chart_white.svg";
        })
    
        graphique.addEventListener("mouseout", function(event) {
            console.log(event);
            graphique.children[0].src = "/assets/icon/chart.svg";
        }) 

        globe.addEventListener("mouseover", function(event) {
            console.log(event);
            globe.children[0].src = "/assets/icon/globe_white.svg";
        })
    
        globe.addEventListener("mouseout", function(event) {
            console.log(event);
            globe.children[0].src = "/assets/icon/globe.svg";
        })
    }
    //console.log(accueil, graphique, jupyter, globe, compare, github); 

    // Acceuil ---------------

    accueil.addEventListener("mouseover", function(event) {
        console.log(event);
        accueil.children[0].src = "/assets/icon/house_white.svg";
    })

    accueil.addEventListener("mouseout", function(event) {
        console.log(event);
        accueil.children[0].src = "/assets/icon/house_purple.svg";
    })

    // Jupyter-Notebook ----------    

    jupyter.addEventListener("mouseover", function(event) {
        console.log(event);
        jupyter.children[0].src = "/assets/icon/python_fill_white.svg";
    })

    jupyter.addEventListener("mouseout", function(event) {
        console.log(event);
        jupyter.children[0].src = "/assets/icon/python_fill_purple.svg";
    })

    // Compare -----------

    compare.addEventListener("mouseover", function(event) {
        console.log(event);
        compare.children[0].src = "/assets/icon/compare_white.svg";
    })

    compare.addEventListener("mouseout", function(event) {
        console.log(event);
        compare.children[0].src = "/assets/icon/compare.svg";
    })

    // GITHUB -----------

    github.addEventListener("mouseover", function(event) {
        console.log(event);
        github.children[0].src = "/assets/icon/github_white.svg";
    })

    github.addEventListener("mouseout", function(event) {
        console.log(event);
        github.children[0].src = "/assets/icon/github_purple.svg";
    })
}, 1000)
