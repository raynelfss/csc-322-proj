function addElementtoTable() {        // Function adds an element to the item bar. Uses createElement() function.
    let itemName = document.getElementById("itemName").value        // Gets itemname from input.
    let desc = document.getElementById("description").value         // Gets description from input.
    let imgsrc = document.getElementById("imglink").value       // Gets image link from input (Will be changed in future).
    let price = document.getElementById("price").value      // Gets price from input.
    
    
    itemName.value =  '' 
    desc.value = '' 
    imgsrc.value = ''  
    price.value = '' 
    let data = {'name': itemName, 'description' : desc, 'img_url' : imgsrc, 'price': price}     // Gathers all the data into an array.
    addtoDB(data)
    closeDiag("creatediv")
}

function createElement(id, itemName = "Item-name", description = "No description", price = undefined, imageSrc = undefined ) {
    let element = document.createElement("tr")         // Creates a div element with class items.
    element.classList = "item"

    let ident = document.createElement("td")
    ident.appendChild(document.createTextNode(id))
    element.appendChild(ident)
    
    

    let name =  document.createElement("td")        // Name will have format h1.
    name.appendChild(document.createTextNode(itemName))         // Appends the text as child.
    element.appendChild(name)          // Adds name to inner div.

    let desc = document.createElement("td")          // Creates description paragraph using p.
    desc.appendChild(document.createTextNode(description))      // Appends paragraph text from description arg.
    element.appendChild(desc)              // Appends object to element.

    let image =  document.createElement("td")      // An image object is created.
    image.appendChild(document.createTextNode(imageSrc))                 // Appends image to the inner div.
    element.appendChild(image)

    let pric =  document.createElement("td")         // Creates price text using p
    pric.appendChild(document.createTextNode(price))        // Appends paragraph text from price arg.
    element.appendChild(pric)          // Appends price to inner div.
    
    let action = document.createElement("td")

    let button1 =  document.createElement("button")
    button1.append(document.createTextNode("Edit"))
    button1.onclick = function(){
        editItem(id)
    }
    action.appendChild(button1)

    let button2 =  document.createElement("button")
    button2.append(document.createTextNode("Delete"))
    button2.onclick = function(){
        deleteItem(id)
    }

    action.appendChild(button2)
    element.appendChild(action)

    console.log("Tried to create item.")       // Prints log message, signaling creation of item.
    element.id = id

    return element              // Return item.
}

async function addtoDB(itemArray) {
    const response = await fetch("http://127.0.0.1:5000/api/menu/", {
        method: 'POST',
        headers: {
            'Accept' : 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(itemArray),
    })
    const content = await response.json()
    console.log(content)
    displayItems()
}

async function getfromDB() {
    const response = await fetch('http://127.0.0.1:5000/api/menu/')
    const data = await response.json()
    return data['response']
}

function openDiag(id) {
    let diag = document.getElementById(id)
    diag.style.display = 'flex'
}

function closeDiag(id) {
    document.getElementById("itemName").value =  '' 
    document.getElementById("description").value = '' 
    document.getElementById("imglink").value = ''  
    document.getElementById("price").value = '' 
    let diag = document.getElementById(id)
    diag.style.display = 'none'
}

async function displayItems()  {
    eraseElements()
    let items = await getfromDB() || [] 
    let table = document.getElementById("ptable")      // Uses item-list by calling its id.

    items.forEach(element => {
        console.log(element[0]) 
        let frame = createElement(element[0], element[1], element[3], element[4], element[2]) 
        table.appendChild(frame) 
    }) 
}

async function deleteItem(id) {
    console.log("Attempted delete", id)
    const response = await fetch("http://127.0.0.1:5000/api/menu/", {
        method: 'DELETE',
        headers: {
            'Accept' : 'application/json',
            'Content-Type': 'application/json',
        },
        body: id,
    })
    const content = await response.json()
    console.log(content)
    eraseUniqueElement(id)
    //displayItems()
}

async function editItem(id) {
    let diag = document.getElementById("creatediv")
    diag.style.display = "flex"

    var item

    console.log("Attempted edit", id)
    let items = await getfromDB()
    items.forEach(element => {
        if (element[0] == id) {
            item = element
        }
    })
    console.log(item)
    //TODO:
    // - Create edit frame (function)
    // - Modify attributes from database (if not, erase and replace)
    // - Update Items list.
}

function eraseElements() {
    let elements = document.getElementsByClassName("item") 
    while(elements.length > 0){
        elements[0].parentNode.removeChild(elements[0]) 
    }
}

function eraseUniqueElement(id) {
    let element = document.getElementById(id)
    console.log(element)
    element.remove()
}

displayItems()