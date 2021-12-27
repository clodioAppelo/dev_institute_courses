// Have you heard the infamous song “99 Bottles of Beer?”
// In ths exercise you need to console.log the lyrics to the song 99 Bottles of Beer as an output.

// Prompt the user for a number to begin counting down bottles.
// In the song everytime a bottle falls we subtract the bottles by 1.
// What your code should do is:
// instead of subtracting by 1, everytime a bottle drops the subtracted number should go up by 1
// For example the first time a bottle drops we subtract by 1, the second time we subtract by 2 and so on.
// Take a look below for more help.

// ==============================


// let word = "bottles";
// let count = parseInt(prompt(" Please enter the number of beers on the wall to start our song: "))


// let countPass = 0
// while (count > 0) { 
//   if (count == 1);{ 
//     word = "bottle"
    
         
//   }
//     console.log(count + " " + word + " of beer on the wall");
//     console.log(count + " " + word + " of beer,");
    
    
//     count = count - 1;
//     countPass ++
    
    
//     if (count > 0) { 
//       if (count == 1){
//          word = "bottle"
         
         
//          console.log("Take "+ countPass+ " down," + passIt + " around,")
//         console.log(count + " " + word + " of beer on the wall.");
         
//         } else {
//         passIt = " pass them"
//         console.log("Take "+ countPass+ " down," + passIt + " around,")
//         console.log(count + " " + word + " of beer on the wall.");
    
//         }
        
//     } else {
//       if (count < 1){
//          word = "bottles"
       
//       }
//         console.log("Take "+ countPass+ " down, "+ passIt+ " around,")
//         console.log("No more " + word + " of beer on the wall.");
        
//     }
// }

let startBottles = prompt("Choose a number to begin counting down the bottles");
let count = 1;

console.log(startBottles + " bottles of beer on the wall\n"+startBottles+" bottles of beer\n" + "Take " +count+" down, pass it around");
startBottles = +startBottles - count;
count++;

do {
    console.log(startBottles + " bottles of beer on the wall\n"+startBottles+" bottles of beer\n" + "Take " +count+" down, pass them around");
    startBottles = +startBottles - count;
    count++;

} while (startBottles >0);