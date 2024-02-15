
function change(){

  let nodelist = document.querySelectorAll('*');
    document.querySelector("#backs").onclick = () => {

      if (document.querySelector("body").style.backgroundColor === "white") {
        // change color and background color of the body
        // document.querySelector("body").style.backgroundColor = "black";
        // document.querySelector(".about-me").style.backgroundColor = "black";
        // document.querySelector(".contact-bar").style.backgroundColor = "blue";

        for(let i = 0;i < nodelist.length;i ++){
          nodelist[i].style.backgroundColor = 'black';
          nodelist[i].style.color = 'white';

        }

      } else {
        // document.querySelector("body").style.backgroundColor = "white";
        document.querySelector(".nav-bar").style.backgroundColor = "white";
        for(let i = 0;i < nodelist.length;i ++){
          nodelist[i].style.backgroundColor = 'white';
          nodelist[i].style.color = 'black';

        }

      }
    }
  }

// function toggles() {
//     let state = document.querySelector(".nav-bar");
//     let positioning = document.querySelector(".menue");
//     document.querySelector("#show").onclick = () => {
//         positioning.style.display = "block";

//       if (state.style.display === "none") {
//         state.style.display = "block";



//       } else {
//         state.style.display = "none";
//         positioning.style.display = "block";

//       }
//     }
//   }

