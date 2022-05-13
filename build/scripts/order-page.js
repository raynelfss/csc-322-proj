// Functions for the clock
function currentTime() {
    let clock = document.getElementById("currentTime");
    var today = new Date();
    let hours = hourParse(today);
    let meridiam = ampm(today);
    let min = parseTime(today.getMinutes());
    let sec = parseTime(today.getSeconds());
    let day = parseDay(today.getUTCDay())
    var time = String(day + " " + (today.getMonth() +1) + " / " + today.getDate() + " / " + today.getFullYear() 
    + ", " + hours + ":" + min + ":" + sec + " " + meridiam);
    clock.innerText = time;
}

function hourParse(today) {
    let hour = today.getHours();
    if (hour % 12 == 0) { return 12; }
    else { return hour % 12; }
}

function parseDay(num){
    let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    return days[num];
}

function ampm(today) {
    let hour = today.getHours();
    if (hour < 12) { return "AM"; }
    else { return "PM"; }
}

function parseTime(temp) {
    if (temp < 10) { return "0" + temp }
    else { return temp }
}

// Functions to display 

async function getfromDB() {
    const response = await fetch('/api/order/inprogress');
    const data = await response.json();
    console.log(data['response']);

    filltable(data['response']);

}

async function getOrderByID(id){
    const response = await fetch('/api/order/' + id);
    const data = await response.json();
    return data['response'];
}

function filltable(data) {
    let table = document.getElementById("ptable");
    data.forEach(order => {

        let row = document.createElement('tr');
        row.classList.add("rows");
        row.id = order.orderID;
        ['orderID', 'dishIDs', 'customerID', 'address', 'cost', 'datetime',
            'employeeID', 'deliveryMethod', 'status'].forEach(key => {
                // itterate through those values in the order and create a column for each
                let column = null;
                switch (key) {
                    case 'employeeID':
                        // when filing in column for employeeID, check if employeeID exists and if it's a delivery
                            if (order['employeeID'] == null && order['deliveryMethod'] == 'delivery') {
                                let button = createElement('td');
                                button.appendChild(createElement('button', { text: 'Assign', onclick: `autoAssign(${order.orderID})` }));
                                column = button;
                            } // if delivery have a button to assign deliveryBoy
                            else {
                                column = createElement('td', { text: order[key] }); // else just display employeeID
                            }
                        break;
                    case 'orderID':
                        column = createElement('td');
                        let anchor = createElement('a', { onclick:`loadOrder(${order[key]})`/*href: `/orders/${order[key]}`*/, text: order[key] })
                        column.appendChild(anchor)
                        break;
                    default:
                        column = createElement('td', { text: order[key] });
                        break;
                }
                row.appendChild(column); // add the created column into the row
            })
            let button_row = createElement('td');
            let button = createElement('button', { text: 'Cancel' , onclick: `cancelAction(${order.orderID})`})
            button_row.appendChild(button)
        row.appendChild(button_row);
        table.appendChild(row); // add the row to table
    });
}

function cancelAction(id) {
    if (confirm("Are you sure you want to cancel this order? The order value will be refunded to the user.")) {
        cancelOrder(id);

    }
}

async function cancelOrder(id) {
    const order = await getOrderByID(id);
    order.status = "cancelled";
    let dishes = order.dishIDs.split(',');
    order.dishIDs = dishes;

    console.log(order);
    updateItem(id, order)
    eraseUniqueElement(id);
}

async function updateItem(id, order) {
    const response =  await fetch('/api/order/' + id, {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(order),
    });
    const data = await response.json()
    console.log(data)
}

function eraseElements() {
    let elements = document.getElementsByClassName('rows');
    while (elements.length > 0) {elements[0].parentNode.removeChild(elements[0])};
}

function eraseUniqueElement(id) {
    let element = document.getElementById(id);
    element.remove();
}

getfromDB();
currentTime();

setInterval(() => { currentTime() }, 1000);

