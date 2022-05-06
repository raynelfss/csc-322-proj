function addElementtoTable() {        // Function adds an element to the item bar. Uses createElement() function.
    let data = parseIntoDict()
    console.log(data)
    addtoDB(data)
    closeDiag("cover")
}

function createRow(item) {
    let row = createElement('tr', { class: 'item', id: item['dishID'] });
    Object.keys(item).forEach(key => {
        if (key == 'imageURL') {
            let column = createElement('td');
            let img = createElement('img' , {src: item[key], height: '100px'});
            column.appendChild(img);
            row.appendChild(column);
        }
        else {
            let column = createElement('td', { text: item[key] })
            row.appendChild(column);
        }
    })
    let actionColumn = createElement('td', { class: 'buttonv' });
    let editButton = createElement('button', { text: 'Edit', onclick: `editDiag(${item['dishID']})` })
    let deleteButton = createElement('button', { text: 'Delete', onclick: `deleteItem(${item['dishID']})` })
    actionColumn.appendChild(editButton);
    actionColumn.appendChild(deleteButton);
    row.appendChild(actionColumn);
    return row;
}

async function addtoDB(itemArray) {
    const response = await fetch("/api/menu/", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
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

    let diag = document.getElementById('cover')
    if (id) { actbutton.onclick = function () { editItem(id) } }
    else { actbutton.onclick = addElementtoTable }
    diag.style.display = 'block'

    // let
}

function closeDiag(name) {
    ['dishName', 'dishDescription', 'price', 'imageURL'].forEach(field => {
        document.getElementById(field).value = '';
    })

    let diag = document.getElementById(name)
    diag.style.display = 'none'
}

async function displayItems() {
    eraseElements()
    let items = await getfromDB() || []
    let table = document.getElementById("ptable")      // Uses item-list by calling its id.
    console.log(items);
    items.forEach(item => {
        let row = createRow(item);
        table.appendChild(row);
    })
}

async function deleteItem(id) {
    console.log("Attempted delete", id)
    const response = await fetch("/api/menu/" + String(id), {
        method: 'DELETE',
        headers: {
            'Accept': 'application/json',
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
    let item = parseIntoDict();
    console.log(id, item);
    sendEdittoDB(id, item);
    closeDiag('cover');
}

async function editDiag(id) {
    openDiag("Edit item:", "Save", id)
    console.log("Attempted edit", id)
    let item = await getfromDBInd(id)
    console.log(item)
    fillTextboxes(item)
}

async function sendEdittoDB(id, item) {
    const response = await fetch('/api/menu/' + String(id), {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(item),
    })
    const data = await response.json()
    console.log("Edited the item with id", id, response)
    displayItems()
}

function parseIntoDict() {        // Function adds an element to the item bar. Uses createElement() function.
    let data = {};
    ['dishName', 'dishDescription', 'price', 'imageURL'].forEach(field => {
        let inputElement = document.getElementById(field);
        data[field] = inputElement.value;
        inputElement.value = '';
    })
    return data
}

function fillTextboxes(item) {
    ['dishName', 'dishDescription', 'price', 'imageURL'].forEach(field => {
        console.log(item[field])
        document.getElementById(field).value = item[field];
    })
}

function eraseElements() {
    let elements = document.getElementsByClassName("item")
    while (elements.length > 0) { elements[0].parentNode.removeChild(elements[0]) }
}

function eraseUniqueElement(id) {
    let element = document.getElementById(id)
    console.log(element)
    element.remove()
}

displayItems()