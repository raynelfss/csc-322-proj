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

function eraseElements() {
    let elements = document.getElementsByClassName("items") 
    while(elements.length > 0){ elements[0].parentNode.removeChild(elements[0]) }
}

function eraseUniqueElement(id) {
    let element = document.getElementById(id)
    console.log(element)
    element.remove()
}

async function getfromDB() {
    const response = await fetch('http://127.0.0.1:5000/api/menu/')
    const data = await response.json()
    return data['response']
}

async function displayItems()  {
    eraseElements()
    let items = await getfromDB() || [] 
    let itembar = document.getElementById("item-list")      // Uses item-list by calling its id.

    items.forEach(element => {
        console.log(element[0]) 
        let frame = createElement(element[0], element[1], element[3], element[4], element[2]) 
        itembar.appendChild(frame) 
    }) 
}

function createElement(id, itemName = "Item-name", description = "No description", price = undefined, imageSrc = undefined ) {
    let element = document.createElement("div")         // Creates a div element with class items.
    element.classList.add("items", "div")                         // div is now part of class items.

    let innerdiv = document.createElement("div")        // Creates inner diviser for the many object inside item.
    innerdiv.classList = "div"

    if (imageSrc != undefined) {                // If imagesrc is not undefined.
        let image =  document.createElement("img")      // An image object is created.
        image.src = imageSrc                // Set source of image as url from imagesrc
        image.setAttribute("width","200px")         // Set width to 200px.
        image.setAttribute("height","200px")        // Set height to 200px.
        innerdiv.appendChild(image)                 // Appends image to the inner div.
    }

    let name =  document.createElement("h1")        // Name will have format h1.
    name.appendChild(document.createTextNode(itemName))         // Appends the text as child.
    name.classList = "header1"          // Sets class of h1 as header1.
    innerdiv.appendChild(name)          // Adds name to inner div.

    let div1 =  document.createElement("hr")        // Creates a divider line using "hr"
    div1.classList.add("line")                 // Adds hr to line class.
    innerdiv.appendChild(div1)              // Appends div1 line to innerdiv.

    let desc = document.createElement("p")          // Creates description paragraph using p.
    desc.appendChild(document.createTextNode(description))      // Appends paragraph text from description arg.
    desc.classList = "p2"                   // Adds object to p2 class.
    innerdiv.appendChild(desc)              // Appends object to innerdiv.

    let div2 =  document.createElement("hr")        // Creates a divider line using "hr"
    div2.classList.add("line")                  // Adds hr to line class.
    innerdiv.appendChild(div2)              // Appends div1 line to innerdiv.

    let pric =  document.createElement("p")         // Creates price text using p
    pric.appendChild(document.createTextNode(price))        // Appends paragraph text from price arg.
    pric.classList = "p3"               // Adds paragraph to class p3.
    innerdiv.appendChild(pric)          // Appends price to inner div.

    let div3 = document.createElement("div")
    div3.classList = "div"
    
    let button1 =  document.createElement("button")
    button1.append(document.createTextNode("Edit"))
    button1.onclick = function(){
        editItem(id)
    }
    div3.appendChild(button1)

    let button2 =  document.createElement("button")
    button2.append(document.createTextNode("Delete"))
    button2.onclick = function(){
        deleteItem(id)
    }
    div3.appendChild(button2)
    innerdiv.appendChild(div3)

    element.appendChild(innerdiv)       // Appends the inner div to the item object.
    console.log("Tried to create item.")       // Prints log message, signaling creation of item.
    element.id = id

    return element              // Return item.
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
    console.log("Attempted edit", id)
    let item = await getfromDB()
    console.log(item, item[id])
    //TODO:
    // - Create edit frame (function)
    // - Modify attributes from database (if not, erase and replace)
    // - Update Items list.
    displayItems()
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

displayItems() 
