function change() {
    document.querySelector("#backs").onclick = () => {
      console.log("names");
      console.log("clicked");
  
      if (document.querySelector("body").style.backgroundColor === "white") {
        // change color and background color of the body
        console.log("color white");
        document.querySelector("body").style.backgroundColor = "black";
        document.querySelector("body").style.color = "white";
      } else {
        console.log("color black");
        document.querySelector("body").style.backgroundColor = "white";
        document.querySelector("body").style.color = "black";
        document.querySelector(".nav-bar").style.color = "white";
      }
    };
  }
  
  function toggles() {
    console.log("clicked with funge");
    document.querySelector("#show").onclick = () => {
      let state = document.querySelector(".nav-bar");
      let positioning = document.querySelector(".menu");
      if (state.style.display === "none") {
        state.style.display = "block";
        positioning.style.position = "relative";
        positioning.style.bottom = "70px";
  
        state.style.display.scrollBehavior = "smooth";
      } else {
        state.style.display = "none";
      }
    };
  }
  