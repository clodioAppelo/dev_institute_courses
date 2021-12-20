// Exercise 1 : Your Favorite Colors
// Instructions
// Create an array called colors where the value is a list of your favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus

// let arrColors = ["red", "blue", "green", "yellow", "black"]

// for (let i = 0; i < arrColors.length; i++) {
//     console.log("My #1 choice is " + arrColors[0] );
//     console.log("My #2 choice is " + arrColors[1] );
//     console.log("The following colors aren't my favorites " + arrColors[2] +" " + 
//     arrColors[3] + " "+ arrColors[4]);
//     break
// }

//-----------------------------------------------------------------------------------------------------


// Exercise 2 : List Of People
// Instructions
// let people = ["Greg", "Mary", "Devon", "James"]
// Write code to remove “Greg” from the people array.

// Write code to replace “James” to “Jason”.

// Write code to add your name to the end of the people array.

// Using a loop, iterate through the people array and console.log each person.

// Using a loop, iterate through the people array and after you console.log “Jason” exit the loop. Hint: take a look at the break statement in the lesson.

// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name. Hint: remember that now the people array should look like this let people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method

// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

// Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1 ?

// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?


// let people = ["Greg", "Mary", "Devon", "James"];
// people.shift(); // "Greg" eliminated
// people.splice(2, 1, 'jason'); // "James" is being replaced for "Jason"
// people.push("Claudio"); // My name is being added to the end of the array

// for(let i = 0; i < people.length; i++){
// console.log(people[i])
// } // iterating elements of the array and displaying them in console breaking after "Jason".

// console.log("----------------------------------------------------------------------------")

// for(let i = 0; i < people.length; i++){
//     console.log(people[i]);
//     if( i == 2){
//         break;
//     }
// }                      //iterarion of the array breaking up at element "jason"

// newPeople = people.slice(1,3)
// console.log(newPeople);
// console.log(people);

// console.log("Mary's index in people is  " + people. indexOf("Mary"));

// console.log("Foo's index in people is  " + people.indexOf("Foo")); // returns -1 because the element wasn't found

// last = people.indexOf("Claudio");
// console.log(last); // last value = 3 which is the position of "Claudio, the last element of the people's array"

//------------------------------------------------------------------------------------------------

// Exercise 3 : Repeat The Question
// Instructions
// Prompt the user for a number.
// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method

// let i = prompt(" Please enter a number: ");
// do{ numb = prompt("give me another number! ");
//  }
// while(num <10)
// console/log(numb)    
//     

//-------------------------------------------------------------------------------------------------

// Console.log the number of floors in the building.

// Console.log how many apartments are on the floors 1 and 3.

// Console.log the name of the second tenant and the number of rooms he has in his apartment.

// Check if the sum of Sarah and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.


// let building = {
//     numberOfFloors : 4,
//     numberOfAptByFloor : {
//         firstFloor : 3,
//         secondFloor : 4,
//         thirdFloor : 9,
//         fourthFloor : 2,
//     },
//     nameOfTenants : ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan :  [4, 1000],
//         david : [1, 500],
//     },
// }
//     console.log(building.numberOfFloors); // 4
//     console.log(building.numberOfAptByFloor.firstFloor + ", " + building.numberOfAptByFloor.thirdFloor); // 3, 9

//     console.log(building.nameOfTenants[1] + " " + building.numberOfRoomsAndRent.dan [0]); // Dan 4

//      if ( building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1] > building.numberOfRoomsAndRent.dan [1]){
//         building.numberOfRoomsAndRent.dan[1] = 1200;
//      }
    
//     console.log(building.numberOfRoomsAndRent.dan [1]);

    //------------------------------------------------------------------------------------------------------------------------------

    
//     Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Console.log the keys. (using a for loop).
// Console.log the values. (using a for loop).

// let family = {
//     dad: "David",
//     mom: "Esther",
//     child1: "Rut",
//     child2: "Yona",
// }

// for (let x in family) {
//     console.log(x) // key's from object
//     console.log(family[x]) // value's from object
//   }

  //-------------------------------------------------------------------------------------------------------

//   Exercise 6
//   Instructions
//   let details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'raindeer',
//   };

// for( let [key, value] of Object.entries(details)){
//     console.log(key, value);
// }

//-----------------------------------------------------------------------------------------------------------

// Exercise 7 : Secret Group
// Instructions
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”

// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// names.sort();

// for(let index = 0; index < names.length; index++){
//     let element = names[index];
//     if (element = element.slice(0,1)){
//     }
//   console.log(element);
// }

