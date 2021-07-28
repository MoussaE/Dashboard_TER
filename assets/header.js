

setTimeout(function() {

    var ul = document.querySelector("ul.header.menu.nav-ul");
    var chemin = window.location.pathname;
    accueil = document.getElementById("Accueil");
    jupyter = document.getElementById("Jupyter-Notebook");
    compare = document.getElementById("Compare");
    github = document.getElementById("Github");

    if(chemin == "/" || chemin == "") {
        accueil.classList.add("actual-content");
    }
    else if(chemin == "/jupyter") {
        jupyter.classList.add("actual-content");
    }
    else if(chemin == "/compare") {
        compare.classList.add("actual-content");
    }
    // Sur plot donc affiche globe
    else if(chemin == "/plot") {
        globe = document.getElementById("Globe");
        rgraphique = document.getElementById("remove-graphique");
        rgraphique.classList.add("actual-content");
        /*ul.removeChild(rgraphique);

        globe.addEventListener("mouseover", function(event) {
            //console.log(event);
            globe.children[0].src = "/assets/icon/globe_white.svg";
        })
    
        globe.addEventListener("mouseout", function(event) {
            //console.log(event);
            globe.children[0].src = "/assets/icon/globe.svg";
        })*/


    }
    // Sur globe donc affiche plote
    else if (chemin == "/map") {
        graphique = document.getElementById("Graphique");
        rglobe = document.getElementById("remove-globe");
        rglobe.classList.add("actual-content");
        /*ul.removeChild(rglobe);

        graphique.addEventListener("mouseover", function(event) {
            //console.log(event);
            graphique.children[0].src = "/assets/icon/chart_white.svg";
        })
    
        graphique.addEventListener("mouseout", function(event) {
            //console.log(event);
            graphique.children[0].src = "/assets/icon/chart.svg";
        }) */

        
    }   
    // Ailleur que sur map ou plot
    //else {
        graphique = document.getElementById("Graphique");
        globe = document.getElementById("Globe");

        graphique.addEventListener("mouseover", function(event) {
            //console.log(event);
            graphique.children[0].src = "/assets/icon/chart_white.svg";
        })
    
        graphique.addEventListener("mouseout", function(event) {
            //console.log(event);
            graphique.children[0].src = "/assets/icon/chart.svg";
        }) 

        globe.addEventListener("mouseover", function(event) {
            ////console.log(event);
            globe.children[0].src = "/assets/icon/globe_white.svg";
        })
    
        globe.addEventListener("mouseout", function(event) {
            ////console.log(event);
            globe.children[0].src = "/assets/icon/globe.svg";
        })
    //}
    ////console.log(accueil, graphique, jupyter, globe, compare, github); 

    // Acceuil ---------------

    accueil.addEventListener("mouseover", function(event) {
        //console.log(event);
        accueil.children[0].src = "/assets/icon/house_white.svg";
    })

    accueil.addEventListener("mouseout", function(event) {
        //console.log(event);
        accueil.children[0].src = "/assets/icon/house_purple.svg";
    })


    // Jupyter-Notebook ----------    

    jupyter.addEventListener("mouseover", function(event) {
        //console.log(event);
        jupyter.children[0].src = "/assets/icon/python_fill_white.svg";
    })

    jupyter.addEventListener("mouseout", function(event) {
        //console.log(event);
        jupyter.children[0].src = "/assets/icon/python_fill_purple.svg";
    })

    // Compare -----------

    compare.addEventListener("mouseover", function(event) {
        //console.log(event);
        compare.children[0].src = "/assets/icon/compare_white.svg";
    })

    compare.addEventListener("mouseout", function(event) {
        //console.log(event);
        compare.children[0].src = "/assets/icon/compare.svg";
    })

    // GITHUB -----------

    github.addEventListener("mouseover", function(event) {
        //console.log(event);
        github.children[0].src = "/assets/icon/github_purple.svg";
    })

    github.addEventListener("mouseout", function(event) {
        //console.log(event);
        github.children[0].src = "/assets/icon/github_white.svg";
    })

    current = document.querySelector(".actual-content");
    //console.log(current);
    current.href = "javascript:void(0)";
    current.style.cursor = "default";
}, 2000)
