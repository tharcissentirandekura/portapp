<!DOCTYPE html>
<html>
<body>
<style>
    body{
        color: white;
        background-color: black;
        font-size: 24px;
        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    }
</style>
<h1 id="counts" onclick="count()">waiting to count ...</h1>
<h2 id="times">0</h2>
<p>
    burundi is the most hated country and I like so much becsue
    its people is amazing and I thinking I will male a lot of things in the future 
    after making more sense.
</p>
<button id="btn" onclick="coloring()">change background</button>



<script>

    let counter = 0;
    var count = 0;
    setInterval(()=>{
  
    count++
    // console.log(count)
    document.querySelector('#times').innerHTML = count;

        }, 1000);

    function coloring(){
        document.querySelector('#btn').onclick = ()=>{
            counter ++;
        
            console.log("counter = ",counter);
            document.querySelector('#counts').innerHTML = counter;
                
            

            // }
        // document.querySelector('#btn').onclick = ()=>{

            if (document.querySelector('body').style.backgroundColor ==='white'){
                // change color and background color of the body
                document.querySelector('body').style.backgroundColor='black';
                document.querySelector('body').style.color='white';
             }else{
                document.querySelector('body').style.backgroundColor='white'
                document.querySelector('body').style.color='black';
                

             }
             
            
        }
    }

</script>

</body>
</html>