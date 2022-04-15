function addElementtoTable() {        // Function adds an element to the item bar. Uses createElement() function.
    let data = parseIntoDict()
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
    action.classList.add("buttonv")

    let button1 =  document.createElement("button")
    button1.append(document.createTextNode("Edit"))
    button1.onclick = function(){
        editDiag(id)
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
    const response = await fetch("/api/menu/", {
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
    const response = await fetch('/api/menu/')
    const data = await response.json()
    return data['response']
}

async function getfromDBInd(id) {
    const response = await fetch('/api/menu/' + id)
    const data = await response.json()
    return data['response']
}

function openDiag(motive, buttonText, id = false) {
    let actbutton = document.getElementById("editorcreate")
    actbutton.innerHTML = buttonText

    document.getElementById("subject").innerHTML = motive

    let diag = document.getElementById('creatediv')
    if (id) {
        actbutton.onclick = function(){ editItem(id) }
    }
    else { actbutton.onclick = addElementtoTable }
    diag.style.display = 'flex'

    // let
}

function closeDiag() {
    document.getElementById("itemName").value =  '' 
    document.getElementById("description").value = '' 
    document.getElementById("imglink").value = ''  
    document.getElementById("price").value = '' 
    
    let diag = document.getElementById('creatediv')
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
    const response = await fetch("/api/menu/"+String(id), {
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

function editItem(id) {
    let item = parseIntoDict()
    sendEdittoDB(id, item)
    closeDiag()
}

async function editDiag(id) {
    openDiag("Edit item:", "Edit", id)
    console.log("Attempted edit", id)
    let item = await getfromDBInd(id)
    console.log(item)

    fillTextboxes(item[1], item[3], item[2], item[4])
}

async function sendEdittoDB(id, item) {
    const response = await fetch('/api/menu/' + String(id), {
        method: 'PUT',
        headers: {
            'Accept' : 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(item),
    })
    const data = await response.json()
    console.log("Edited the item with id", id, response)
    displayItems()
}

function parseIntoDict() {        // Function adds an element to the item bar. Uses createElement() function.
    let itemName = document.getElementById("itemName").value        // Gets itemname from input.
    let desc = document.getElementById("description").value         // Gets description from input.
    let imgsrc = document.getElementById("imglink").value       // Gets image link from input (Will be changed in future).
    let price = document.getElementById("price").value      // Gets price from input.
    
    itemName.value =  '' 
    desc.value = '' 
    imgsrc.value = ''  
    price.value = '' 
    let data = {'name': itemName, 'description' : desc, 'img_url' : imgsrc, 'price': price}     // Gathers all the data into an array.
    return data
}

function fillTextboxes(name, description, imgsrc, price) {
    document.getElementById("itemName").value = name       // Gets itemname from input.
    document.getElementById("description").value = description       // Gets description from input.
    document.getElementById("imglink").value = imgsrc       // Gets image link from input (Will be changed in future).
    document.getElementById("price").value = price      // Gets price from input.
}

function eraseElements() {
    let elements = document.getElementsByClassName("item") 
    while(elements.length > 0){ elements[0].parentNode.removeChild(elements[0]) }
}

function eraseUniqueElement(id) {
    let element = document.getElementById(id)
    console.log(element)
    element.remove()
}

displayItems()