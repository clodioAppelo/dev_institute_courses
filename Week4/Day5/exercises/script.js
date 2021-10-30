// Ex 1 Change The Navbar

// In the <div> above, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.
// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (li).
// Finally, append this updated list node to the unordered list above, using the appendChild method.
// Bonus
// Use the firstElementChild and the lastElementChild properties to retrieve the first and last li elements from their parent element (ul). Display the text of each link. (Hint: use the textContent property).


// let navBar = document.getElementById("navBar");
// navBar.setAttribute("id", "socialNetworkNavigation");

//  let li  = document.createElement("li");                   // Create a <li> node
//  let logout = document.createTextNode("Logout");            // Create a text node
//   li.appendChild(logout);                                  // Append the text to <li>
//   document.getElementsByTagName("ul")[0].appendChild(li)

  

  
//----------------------------------------------------------------------------------------------------------------------

// ex 2


// In the HTML above change the name “Pete” to “Richard”.
// Change each first name of the two <ul>'s to your name.
// At the end of each <ul> add a <li> that says “Hey students”.
// Delete the name Sarah from the second <ul>.
// Bonus
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.

// let richard = document.getElementsByClassName("list") [0]. lastElementChild;
// richard.textContent = "Richard";


// let claudio = document.getElementsByTagName("ul")[0].firstElementChild;
// claudio.textContent = "Claudio";
// let claudio2 = document.getElementsByTagName("ul")[1].firstElementChild;
// claudio2.textContent = "Claudio";

//  let node = document.createElement("li");
//  let textnode = document.createTextNode("Hey students");
//  node.appendChild(textnode);
//  document.getElementsByClassName("list")[0].appendChild(node);

// let ul = document.getElementsByClassName("list");
// let li = document.createElement("li");
// li.appendChild(document.createTextNode("Hey Students"));
// ul[0, 1].appendChild(li); // it just work on one of the list instead of both

// let removeSarah = document.getElementsByTagName("li")[3];
// removeSarah.remove("li");
 






//----------------------------------------------------------------------------------------------------------------------

// ex 3

// For the following exercise use the HTML presented above:

// Add a “light blue” background color and some padding to the <div>.
// Do not display the first name (John) in the list.
// Add a border to the second name (Pete).
// Change the font size of the whole body.
// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).

let div = document.querySelector("div");
div.style.background = "lightblue";
div.style.padding = "25px";

let john = document.getElementsByTagName("li")[i];
    john.style.display = "none";
        

let pete = document.getElementsByTagName("li")[i];
pete.style.border = "blue solid 2 px";

let body = document.querySelector("body");
body.style.fontSize =   "50px"; 



//----------------------------------------------------------------------------------------------------------------------
