function addElementtoItemBar() {        // Function adds an element to the item bar. Uses createElement() function.
    let itemName = document.getElementById("itemName").value;       // Gets itemname from input.
    let desc = document.getElementById("description").value;        // Gets description from input.
    let imgsrc = document.getElementById("imglink").value;      // Gets image link from input (Will be changed in future).
    let price = document.getElementById("price").value;     // Gets price from input.
    
    
    document.getElementById("itemName").value =  '';
    document.getElementById("description").value = '';
    document.getElementById("imglink").value = ''; 
    document.getElementById("price").value = '';

    let current = JSON.parse(localStorage.getItem("Items")) || [];
    localStorage.removeItem("Items");
    let data = [itemName, desc, imgsrc, price];    // Gathers all the data into an array.
    current.push(data);
    localStorage.setItem("Items", JSON.stringify(current));
    displayItems();
}

function displayItems()  {
    let elements = document.getElementsByClassName("items");
    while(elements.length > 0){
        elements[0].parentNode.removeChild(elements[0]);
    }

    let items = JSON.parse(localStorage.getItem("Items")) || [];
    let itembar = document.getElementById("item-list");     // Uses item-list by calling its id.
    //console.log(itembar);

    items.forEach(element => {
        console.log(element[0]);
        let frame = createElement(element[0], element[1], element[3], element[2]);
        itembar.appendChild(frame);
    });
}

function createElement(itemName = "Item-name", description = "No description", price = undefined, imageSrc = undefined ) {
    let element = document.createElement("div");        // Creates a div element with class items.
    element.classList = "items";                        // div is now part of class items.

    let innerdiv = document.createElement("div");       // Creates inner diviser for the many object inside item.
    
    if (imageSrc != undefined) {                // If imagesrc is not undefined.
        let image =  document.createElement("img");     // An image object is created.
        image.src = imageSrc;               // Set source of image as url from imagesrc
        image.setAttribute("width","200px");        // Set width to 200px.
        image.setAttribute("height","200px");       // Set height to 200px.
        innerdiv.appendChild(image);                // Appends image to the inner div.
    }

    let name =  document.createElement("h1");       // Name will have format h1.
    name.appendChild(document.createTextNode(itemName));        // Appends the text as child.
    name.classList = "header1";         // Sets class of h1 as header1.
    innerdiv.appendChild(name);         // Adds name to inner div.

    let div1 =  document.createElement("hr");       // Creates a divider line using "hr"
    div1.classList = "line";                // Adds hr to line class.
    innerdiv.appendChild(div1);             // Appends div1 line to innerdiv.

    let desc = document.createElement("p");         // Creates description paragraph using p.
    desc.appendChild(document.createTextNode(description));     // Appends paragraph text from description arg.
    desc.classList = "p2";                  // Adds object to p2 class.
    innerdiv.appendChild(desc);             // Appends object to innerdiv.

    let div2 =  document.createElement("hr");       // Creates a divider line using "hr"
    div2.classList = "line";                // Adds hr to line class.
    innerdiv.appendChild(div2);             // Appends div1 line to innerdiv.

    let pric =  document.createElement("p");        // Creates price text using p
    pric.appendChild(document.createTextNode(price));       // Appends paragraph text from price arg.
    pric.classList = "p3";              // Adds paragraph to class p3.
    innerdiv.appendChild(pric);         // Appends price to inner div.

    element.appendChild(innerdiv);      // Appends the inner div to the item object.
    console.log("Tried to create item.")       // Prints log message, signaling creation of item.

    return element;             // Return item.
}

displayItems();
