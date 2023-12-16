
function change(){
    document.querySelector('#backs').onclick = ()=>{
        console.log('names');
        console.log("clicked");

        if (document.querySelector('body').style.backgroundColor ==='white'){
            // change color and background color of the body
            console.log("color white");
            document.querySelector('body').style.backgroundColor='black';
            document.querySelector('body').style.color='white';
            
            }else{
            console.log("color black");
            document.querySelector('body').style.backgroundColor='white'
            document.querySelector('body').style.color='black';
            document.querySelector('.nav-bar').style.color='white';
            }
            
        
    }
}
