// Get the value of each of the inputs in the HTML file when the button is clicked.
// Make sure the values are not empty
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed (but keep the values entered by the user). The user could click the button at least three times and get a new story. Display the stories randomly.

let libButton = document.getElementById("lib-button");
      let libIt = function() {
        let storyDiv = document.getElementById("story");
        let noun = document.getElementById("noun").value;
        let adjective = document.getElementById("adjective").value;
        let name = document.getElementById("person").value;
        storyDiv.innerHTML =
          "walking over the beach with " +
          noun +
          " and " +
          adjective +
          " it. " +
          name +
          " having a good time.";
      };
      libButton.addEventListener("click", libIt);