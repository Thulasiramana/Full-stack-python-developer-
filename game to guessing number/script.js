let totalscore=10
function check()
{
let value=document.getElementById("value").value;
        let point=document.getElementById("score");
        let crt=document.getElementById("crt")
        let ran=Math.random()
        
        let random=(Math.floor(ran*10)+1)
        
 if (value==random)
        {
         crt.textContent="You Won"
         alert("you Won 🥳🥳😘")
         console.log("The System Guessed Number is "+random)
        }
        else{
            crt.textContent="You Wrong"
            totalscore=totalscore-1
            point.textContent= "Your Score is "+totalscore
        }
    }  
