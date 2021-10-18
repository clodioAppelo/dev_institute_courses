/*Remove Banana from the array.
Sort the array in alphabetical order.
Add “Kiwi” to the end of the array.
Remove “Apples” from the array. Don’t use the same method as in part 1.
Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
At the end you should see this outcome:
["Kiwi", "Oranges", "Blueberries"]*/

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

fruits.shift(); //[ "Apples", "Blueberries", "Oranges" ]

fruits.sort(); // [ "Apples". "Blueberries","Oranges" ]
console.log(fruits);

fruits.push("Kiwi");// ["Apples","Oranges", "Blueberries", "Kiwi"]

console.log(fruits.splice(0,1)); // ["Oranges", "Blueberries", "Kiwi"]

fruits.reverse(); 
console.log(fruits); //[ "Kiwi", "Oranges", "Blueberries" ]


//Exercise 2: Access and then console.log “Oranges”.

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

console.log(moreFruits [1] [1] [0]);