function getH1() {
    let header = document.getElementsByTagName("h1")[0];
    let headerContent = header.innerText;
    alert(headerContent);
}

function addElementtoItemBar() {
    let itembar = document.getElementById("item-list");
    let itemName = document.getElementById("itemName").value;
    let desc = document.getElementById("description").value;
    let imgsrc = document.getElementById("imglink").value;
    let price = document.getElementById("price").value;
    let item = createElement(itemName, desc, price, imgsrc);

    itembar.appendChild(item);
}

function createElement(itemName = "Item-name", description = "No description", price = undefined, imageSrc = undefined ) {
    let element = document.createElement("div");
    element.classList = "items";

    let innerdiv = document.createElement("div");
    
    if (imageSrc != undefined) {
        let image =  document.createElement("img");
        image.src = imageSrc;
        image.setAttribute("width","200px");
        image.setAttribute("height","200px");
        innerdiv.appendChild(image);
    }

    let name =  document.createElement("h1");
    name.appendChild(document.createTextNode(itemName));
    name.classList = "header1";
    innerdiv.appendChild(name);

    let div1 =  document.createElement("hr");
    div1.classList = "line";
    innerdiv.appendChild(div1);

    let desc = document.createElement("p");
    desc.appendChild(document.createTextNode(description));
    desc.classList = "p2";
    innerdiv.appendChild(desc);

    let div2 =  document.createElement("hr");
    div2.classList = "line";
    innerdiv.appendChild(div2);

    let pric =  document.createElement("p");
    pric.appendChild(document.createTextNode(price));
    pric.classList = "p3";
    innerdiv.appendChild(pric);

    element.appendChild(innerdiv);
    console.log("Tried to create child.")

    return element;
}