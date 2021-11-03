// function insertRow(){
//     let tr = document.createElement("tr");
//     let rowNumber = document.getElementsByTagName("tr").length;
//     let currentRownumber = rowNumber + 1;
//     for(let index = 0; index < 3; index ++){
//         let currenttd = document.createElement("td");
//         let currenNode = document.createTextNode(`row ${currentRownumber} all ${ index}`);
//         currenttd.appendChild(currenttextNode);
//         tr.appendChild(td);
//     }
// }
// let currenttable = document.querySelector("table");
// currenttable.appendChild(tr);

function insertRow() {
    var table = document.getElementById("sampleTable");
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    cell1.innerHTML = "NEW CELL1";
    cell2.innerHTML = "NEW CELL2";
  }