function addTask(){
    let item  = document.getElementById("todoinput").value;
    let text = document.createTextNode(item);
    let checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.name = "name";
    checkbox.value = "value";

    let newitem = document.createElement("div");
    
    newitem.appendChild(checkbox);
    newitem.appendChild(text);
    document.getElementsByClassName("listTask")[0].appendChild(newitem);

}