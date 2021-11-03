
// Exercise 1
// Analyse the code below without running it, what will be the output ?

// var num = 8;
// var num = 10;
// console.log(num);     // guess result: num = 10 because var num is reassigned with a new value

// -------------------------------------------------------------------------------------

// Exercise 2
// function numbers() {
//   for (var i = 0; i < 5; i += 1) {
//     console.log(i);
//   }
//     console.log(i);
// }
// numbers();
   // guess result: error will be displayed after console.log (i) outside the loop.
   //After run the code: result was displaying loop and throwing error (i) was not defined.

//  ------------------------------------------------------------------------------------------------

// Exercise 3
// You have to decide which type of variables you have to use

// Create a global variable that save the amount of money you have in your account
// Create a variable that saves the amount of VAT
// Create a variable that saves the amount of all the expenses and revenues you did /received for the past last month
// Create a JS code that multiplies of the expenses by the VAT
// Create a JS code that changes the amount of the money you have in your account depending on your expenses/revenu.
// Display it

let savings = 200000;
let vat = 0;
let expenses = 0;
let grossRevenues = 0;
let netRevenues = 0;

function incomeExpensesManager(grossRevenues, expenses){
     netRevenues = grossRevenues - expenses;
     console.log("Your Gross Income is:" + grossRevenues);
     console.log("Your Cost expenses are: " + expenses);
     console.log(" Your Net revenues before VAT is: " + netRevenues);
     vat = netRevenues * 17 / 100;
     console.log(" Your VAT (17 %) is: " + vat);
     console.log("Your former savings balance is: " + savings);
     let income = netRevenues - vat;
     console.log(" your current income is: " + income);
     savings = savings + income;
     console.log(" your current savings are: " + savings);
}

incomeExpensesManager(35000, 9550);



