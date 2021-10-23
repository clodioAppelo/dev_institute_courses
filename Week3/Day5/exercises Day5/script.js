// for (let i = 0; i <= 15; i++) {
//     if(i% 2 == 0) {
//     console.log(i + " is an even number");


//     }else{
//         console.log ( " is not an even number")  

        
//     }
// } 

// Write a JavaScript for loop that will go through the variable names.

// if the item is not a string, pass.
// if the item is a string, check if it's first letter is in uppercase. If not, change it to uppercase and then display the name.
// 2. Write a JavaScript for loop that will go through the variable names

// if the item is not a string, go out of the loop.
// if the item is a string, display it.

let names= ["john", "sarah", 23, "Rudolf",34]

for (let index = 0; index < names.length; index++) {
    let element = names[index];
    if (typeof element !== 'string' ){
        continue
    }
    if(element[0] != element[0].toUpperCase()){
        element = element.charAt(0).toUpperCase() + element.slice(1)
    }
    console.log(element);
}

for (let index = 0; index < names.length; index++) {
    let element = names[index];
    if (typeof element !== 'string' ){
        break
    }
}
