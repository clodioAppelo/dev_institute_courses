//ex 1

// let incrementPosition = 0;
// const redSquare = document.querySelector("#animate");
// let incrementInterval = () => {
//   let currentInterval = setInterval(() => {
//     redSquare.style.top = `${incrementPosition}px`;
//     redSquare.style.left = `${incrementPosition}px`;
//     incrementPosition += 50;
//     if (incrementPosition == 400) {
//       clearInterval(currentInterval);
//       incrementPosition = 0;
//     }
//   }, 400);
// };

// function myMove() {
//   let clickMe = document.querySelector("button");
//   clickMe.addEventListener("click", incrementInterval);
// }


//---------------------------------------------------------------------------

// ex 2

const fill = document.querySelector(".fill");
const empties = document.querySelectorAll(".empty");

fill.addEventListener("dragstart", dragStart);
fill.addEventListener("dragend", dragEnd);

for (const empty of empties) {
  empty.addEventListener("dragover", dragOver);
  empty.addEventListener("dragenter", dragEnter);
  empty.addEventListener("dragleave", dragLeave);
  empty.addEventListener("drop", dragDrop);
}

function dragStart() {
  this.className += " hold";
  setTimeout(() => (this.className = "invisible"), 0);
}

function dragEnd() {
  this.className = "fill";
}

function dragOver(e) {
  e.preventDefault();
}

function dragEnter(e) {
  e.preventDefault();
  this.className += " hovered";
}

function dragLeave() {
  this.className = "empty";
}

function dragDrop() {
  this.className = "empty";
  this.append(fill);
}


