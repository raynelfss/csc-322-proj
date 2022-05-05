// import { addCartItem } from './cart';
// createElement and appendChildren imported from helpers.js
function eraseElements() {
    let elements = document.getElementsByClassName("items")
    while (elements.length > 0) { elements[0].parentNode.removeChild(elements[0]) }
}

async function getfromDB() {
    const response = await fetch('/api/menu/')
    const data = await response.json()
    return data['response']
}

async function displayItems() {
    eraseElements()
    let items = await getfromDB() || []
    let itembar = document.getElementById("item-list")     // Uses item-list by calling its id.

    items.forEach(item => {
        let card = createCard(item);
        itembar.appendChild(card);
    })
    // items.forEach(element => {
    //     console.log(element[0])
    //     let frame = createElement(element[0], element[1], element[2], element[3], element[4])
    //     itembar.appendChild(frame)
    // })
}

function createCard(item) {
    let card = createElement('div', { class: 'items div' });
    let innerdiv = createElement('div', { class: 'div' });
    let img = createElement('img', { class: 'menu-img', width: '200px', height: '200px', src: item.imageURL });
    let name = createElement('h1', { text: item.dishName, class: 'header1' });
    let desc = createElement('p', { text: item.dishDescription, class: 'p2' });
    let pric = createElement('p', { text: `Price: ${item.price}`, class: 'p3' });
    let div3 = createElement('div', { class: 'div' });
    let viewDetails = createElement('button', {
        text: 'Reviews',
        class: 'addtocart',
        onclick: `openModel(${item.dishID})`
    })
    let addButton = createElement('button', {
        text: 'Add to cart',
        class: 'addtocart',
        // onclick: `addCartItem(${JSON.stringify(item)})`
    })
    addButton.onclick = function() {
        addCartItem(JSON.stringify(item));
        displayCart();
    }
    div3.appendChild(viewDetails);
    div3.appendChild(addButton);
    appendChildren(innerdiv, [img, name, desc, pric, div3]);
    card.appendChild(innerdiv);
    return card;
}

// function createElement(id, itemName = "Item-name", description = "No description", price = undefined, imageSrc = undefined) {
//     let element = document.createElement("div")  // Creates a div element with class items.
//     element.classList.add("items", "div")        // div is now part of class items.

//     let innerdiv = document.createElement("div") // Creates inner diviser for the many object inside item.
//     innerdiv.classList = "div"

//     if (imageSrc != undefined) { // If imagesrc is not undefined.
//         let image = document.createElement("img") // An image object is created.
//         image.src = imageSrc    // Set source of image as url from imagesrc
//         image.setAttribute("width", "200px")  // Set width to 200px.
//         image.setAttribute("height", "200px") // Set height to 200px.
//         image.classList.add("menu-img")
//         innerdiv.appendChild(image)          // Appends image to the inner div.
//     }

//     let name = document.createElement("h1")  // Name will have format h1.
//     name.appendChild(document.createTextNode(itemName)) // Appends the text as child.
//     name.classList = "header1"   // Sets class of h1 as header1.
//     innerdiv.appendChild(name)   // Adds name to inner div.

//     let desc = document.createElement("p")  // Creates description paragraph using p.
//     desc.appendChild(document.createTextNode(description)) // Appends paragraph text from description arg.
//     desc.classList = "p2"   // Adds object to p2 class.
//     innerdiv.appendChild(desc) // Appends object to innerdiv.

//     let pric = document.createElement("p") // Creates price text using p
//     pric.appendChild(document.createTextNode(price)) // Appends paragraph text from price arg.
//     pric.classList = "p3"  // Adds paragraph to class p3.
//     innerdiv.appendChild(pric)  // Appends price to inner div.

//     let div3 = document.createElement("div")
//     div3.classList = "div"

//     let add = document.createElement("button")
//     add.classList.add("addtocart")
//     add.appendChild(document.createTextNode("Add to cart"))
//     add.setAttribute('onclick', `addCartItem(${id}, '${itemName}', ${price}, '${imageSrc}', 1)`)
//     div3.appendChild(add)

//     innerdiv.appendChild(div3)

//     element.appendChild(innerdiv)  // Appends the inner div to the item object.
//     console.log("Tried to create item.") // Prints log message, signaling creation of item.
//     element.id = id

//     return element  // Return item.
// }

displayItems() 
