// Ex 1

// Using a DOM property, retrieve the h1 and console.log it.

// Using DOM methods, remove the last paragraph in the <article> tag.

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)

// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)

// let h1 = document.getElementsByTagName("h1")[0];
// console.log(h1);

// let pNumber = document.getElementsByTagName("p").length;
// let deleting= document.getElementsByTagName("p")[pNumber - 1];
// console.log(deleting);

// let deleting = document.querySelector("p:last-child");
// console.log(deleting);
// deleting.remove();

// let h2 = document.querySelector("h2");
// h2.addEventListener("click", function (e){
//     e.target.style.backgroundColor = "red";
//     console.log(e);
// });


// let h3 = document.querySelector("h3");
// h3.addEventListener("click", function(e){
//     e.target.style.display = "none";     
// });

// let btn = document.getElementById("toggleBold");


// btn.addEventListener("click", function(){
//     let bold = document.querySelectorAll("p");
//     for(i = 0; i < bold.length; i ++){
//         bold[i].style.fontWeight = "bold";
//     }
// });
// let newP = document.createElement("p");
// newP.innerHTML = "this is the new p";
// document.querySelector("article").appendChild(newP);



//------------------------------------------------------------------------------------------------------------

// Ex 2
// Retrieve the form and console.log it.

// Retrieve the inputs by their id and console.log them.

// Retrieve the inputs by their name attribute and console.log them.

// When the user submits the form (ie. submit event listener)
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.

// let form = document.getElementsByTagName("form")[0];
// console.log(form);
// let inputA = document.getElementById("fname");
// let inputB = document.getElementById("lname");
// let inputC = document.getElementById("submit");
// console.log(inputA, inputB, inputC);

// let firstIndex = form.elements.fname
// for (let a = 0; a<form.elements.length;a++){
//     let c = form.elements[a]      
//     console.log(c)
// }
// for (let a = 0; a<form.length;a++){
//     let f = form.elements[a].name      
//     console.log(f)
// }
// form.addEventListener("submit",function101)
// function function101(e){
//     e.preventDefault()
//     let inputValue1 = form.elements[0].value
//     let inputValue2 = form.elements[1].value
//     if (inputValue1&&inputValue2){
//         
//         for (let a = 0;a<e.target.elements.length-1;a++){
//             let currentInput = e.target.elements[a];
//             let li = document.createElement("li")
//             let textNode = document.createTextNode(currentInput.value)
//             li.append(textNode)
//             let ul = document.querySelector("ul")
//             ul.append(li)
//         }
//     }}




//-------------------------------------------------------------------------------------------------------

// Ex 3  Transform The Sentence
// Create a global variable named allBoldItems.

// Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.

// Create a function called highlight() that changes the color of all the bold text to blue.

// Create a function called return_normal() that changes the color of all the bold text back to black.

// Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example

//  let allBoldItems;
//  window.onload = getBold_items();

//  // Collect all <strong> tags
// function getBold_items(){
//   allBoldItems = document.getElementsByTagName('strong');
// }

// // iterate all bold tags and change color  
// function highlight() 
// {
//    for (var i=0; i < allBoldItems.length; i++)
//    {                                                    
//     allBoldItems[i].style.color = "blue";
//     }
// }

// function return_normal()
// {
//   for (var i=0; i < allBoldItems.length; i++) 
//   {
//        allBoldItems[i].style.color = "black";
//   }
// }



//-------------------------------------------------------------------------------------------

//Exercise 3 Exercice 3 : Volume Of A Sphere


// function volume_sphere()
//  {
//   var volume;
//   var radius = document.getElementById('radius').value;
//   radius = Math.abs(radius);
//   volume = (4/3) * Math.PI * Math.pow(radius, 3);
//   volume = volume.toFixed(4);
//   document.getElementById('volume').value = volume;
//   return false;
//  } 
// window.onload = document.getElementById('MyForm').onsubmit = volume_sphere;


