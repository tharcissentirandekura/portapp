


function change(){
    document.querySelector("#backs").onclick = () => {

      if (document.querySelector("body").style.backgroundColor === "white") {
        // change color and background color of the body
        document.querySelector("body").style.backgroundColor = "black";
        document.querySelector("body").style.color = "white";
      } else {
        document.querySelector("body").style.backgroundColor = "white";
        document.querySelector("body").style.color = "black";
        document.querySelector(".nav-bar").style.color = "white";
      }
    }
  }

function toggles() {
    let state = document.querySelector(".nav-bar");
    let positioning = document.querySelector(".menue");
    document.querySelector("#show").onclick = () => {
        positioning.style.display = "block";

      if (state.style.display === "none") {
        state.style.display = "block";
        positioning.style.position = "relative";
        positioning.style.bottom = "70px";

  
      } else {
        state.style.display = "none";
        positioning.style.display = "block";
  
      }
    }
  }

