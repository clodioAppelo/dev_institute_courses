// Exercise 1
// Part 1
// function infoAboutMe() {
//     console.log("My name is Claudio, I love River Plate");
// }

// infoAboutMe()

// //Part 2

// function infoAboutPerson(personName, personAge, personFavorColor){
//     console.log("your name is: " + personName + " Your age is: " + personAge + 
//     " Your favorite Color is: " + personFavorColor);
// }

// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")

//Part3

// function infoAboutPerson(personName, personAge, personFavorColor, personHobbies){
//     console.log("your name is: " + personName + " Your age is: " + personAge + 
//     " Your favorite Color is: " + personFavorColor + " Your hobbies are: ");
    
//  for (let i = 0; i < personHobbies.length; i++) {
//       console.log(personHobbies[i])
//  }
// }

// infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
// infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])

//-----------------------------------------------------------------------------------------------------------

//Exercises 2

//if the user is too young, alert “Sorry, you are too young to drive this car. Powering off”
// if the user is old enough, alert “You are old enough to drive, Powering On. Enjoy the ride!”
// if the user just turned 18, alert “Congratulations on your first year of driving. Enjoy the ride!”

// function checkDriverAge(age){
    // if (!age){
    //    age = parseInt(prompt ("How old are you?") , 10)
    // }
    // if ( isNaN(age) ){
    //    return checkDriverAge ( parseInt (prompt ( "that was not a number, Please enter a number")),10);
    //}
//     if (age < 18) {
//         console.log("Sorry, you are too young to drive this car. Powering off")
//     } else if ( age > 18){
//         console.log("You are old enough to drive, Powering On. Enjoy the ride!")
//     } else { age = 18;
//         console.log("Congratulations on your first year of driving. Enjoy the ride!")

//     }

// }

// checkDriverAge(18)

//---------------------------------------------------------------------------------------------------------------

//Exercise 3 

// Create a function called checkNumber() that takes no parameter.
// In the function, loop through numbers 0 to 100.
// Add an if/else block
// If the number is even, console.log "the number <number> is even"
// Else, console.log "the number <number> is even"
// Call the function

// function checkNumber(){
//     for (let i = 0; i < 100; i++)
//         if (i % 2 === 0){
//             console.log("the number " + i + " is even")
//         }else {
//             console.log( "the number " + i + " is odd")
//         }
    
// }

// checkNumber()

//------------------------------------------------------------------------------------------------------------------

// exercise 4  incomplete !!!!!!!incomplete !!!!!!!

// John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.

// The calculator has the following rules:
// 1. Tip 20% when the bill is less than $50,
// 2. Tip 15% when the bill is between $50 and $200,
// 3. Tip 10% if the bill is more than $200.



// Ask John for the amount of the bill.
// Create the program explained above.
// In the end, John would like to know:
// Tip amount.
// Final bill (bill + tip).
// (NOTE: To calculate 20% of a value, simply multiply it with 20/100 = 0.2)


   



//-----------------------------------------------------------------------------------------------------

// Exercise 5

// Instructions
// Create a function call isDivisible() that takes no parameter.
// In the function, loop through numbers 0 to 500.
// Console.log all the numbers divisible by 23.
// At the end, console.log the sum of all numbers that are divisible by 23.

// function isDivisible(){
// let sum = 0;
//     for (let i = 0; i < 500; i++){
//         if( i % 23 === 0){
//             console.log(i);
//              sum += i;
//         } 
//     } console.log(sum);
// }

// isDivisible()

//Bonus
// isDivisible(divisor)

// Example:
// isDivisible(3) : Console.log all the numbers divisible by 3, and their sum
// isDivisible(45) : Console.log all the numbers divisible by 45, and their sum

// function isDivisible(divisor){
//     let sum = 0;
//         for (let i = 0; i < 500; i++){
//             if( i % divisor === 0){
//                 console.log(i);
//                  sum += i;
//             } 
//         } console.log(sum);
//     }

    
// isDivisible(3)
//------------------------------------------------------------------------------------------------------

//Exercise 6   Incomplete!!!!!

// Create a function called checkBasket().
// It should:
// prompt the user for an item
// let the user know if the item is in the basket
// Hint: Use the in keyword inside the conditional

// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }

// function checkBasket(basket, lookingFor) {
//     if (basket.hasOwnProperty(lookingFor)) {
//       console.log("This item is in the basket")
//     } else {
//       console.log("This item is not in the basket")
//     }
//   }
  
//   checkBasket(amazonBasket, "glasses");
//   checkBasket(amazonBasket, "soda");
  
  
// checkBasket(prompt("Please, enter the item: " , ));

//--------------------------------------------------------------------------------------------------------


// Exercises 7
// Add the stock and prices objects to your js file.

// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.

// Create a function called myBill() that takes no parameters.

// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock.
// If the item is in stock find out the price in the prices object.
// Call the myBill() function.
// Bonus: If the item is in stock, decrease the item’s stock by 1

// let shoppingList = ["banana", "orange", "apple"];

// let stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// let prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// function myBill(){

// }



//-----------------------------------------------------------------------------------------------------------

// Exercise 8

// Instructions
// Create a function named changeEnough that receives two arguments : an item price and an array representing the amount of change in your pocket.

// In the function, determine whether or not you can afford the item.
// If the sum of the change is bigger or equal than the item’s price, it means that you can afford the item, therefore the function should return true
// If the sum of the change is smaller than the item’s price, it means that you cannot afford the item, therefore the function should return false

// Change will always be represented in the following order: quarters, dimes, nickels, pennies.


// function changeEnough(price, array){
//      let quarter = array[0] * 0.25;
//      let dime = array[1] * 0.1;
//      let nickel = array[2] * 0.05;
//      let penny = array[3] * 0.01;
//      if (price <= quarter + dime + nickel + penny) {
//          return true;

//      }else return false
// }

// console.log(changeEnough(4.25, [25, 20, 5, 0] ));
// console.log(changeEnough(14.11, [2, 100, 0, 0] ));
// console.log(changeEnough(0.75, [0, 0, 20, 5] ));




//--------------------------------------------------------------------------------------------------

// Exercise 9

// Instructions
// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.
// Define a function called planeRideCost().
// It should ask the user for their destination.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$
// If the user doesn’t answer or if the answer is not a string, ask again.
// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.
// Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost.
// Call the function totalVacationCost()
// Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function.