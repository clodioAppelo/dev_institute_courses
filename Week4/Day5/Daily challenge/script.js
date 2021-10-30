let planets = [
    ["Mercury", "123 120 121"],
    ["Venus", " 196 164 118" ],
    ["Earth", "0 165 252"],
    ["Mars", "255 133 95"],
    ["Jupiter", "208 186 157"],
    ["Saturn", "162 146 125"],
    ["Uranus", " 152 218 244"],
    ["Neptune", "120 127 255"] 
];

for (let i = 0; i <planets.length; i++){
    let planetNode = document.createElement("div");
    planetNode.style.backgroundColor = "rgb(" + planets[i][1] + ")";
    planetNode.classList.add("planet");

    let nameNode = document.createTextNode(planets[i][0]);
    planetNode.appendChild(nameNode);
   

    let body = document.querySelector("body");
    body.appendChild(planetNode);

}