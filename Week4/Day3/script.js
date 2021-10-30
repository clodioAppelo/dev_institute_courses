let gameRound = 0
function playTheGame(){
        if (confirm("Do you want to play now?")){
            let num = parseInt(prompt(" Enter a number from 0 to 10"));
            if (isNaN (num)){
                alert("Sorry Not a number, Goodbye")
            } else if(num > 10 ){
                alert(" Your number must be between 0 and 10")  
            }else { 
                computerNumber = Math.floor(Math.random()* 11);
                test(num,computerNumber)
            } 
        }else {
        alert("No Problem, Have a Great Day!");
        }    
}

   function test(num,computerNumber){
       
       gameRound ++
       
       if (gameRound > 3){
           return alert("Sorry, Game Over")
       }

       if(num === computerNumber){
           alert("WINNER")
       } else if (num > computerNumber){
        alert(" your number is bigger than Mine Enter a new number");
        return test(parseInt(prompt("New guess!")),computerNumber)
       } else if (num < computerNumber){
        alert(" your number is lower than Mine Enter a new number");
        return test(parseInt(prompt("New guess!")),computerNumber)
       }
    }
  

