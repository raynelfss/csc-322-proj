// Functions for the clock
function currentTime() {
    let clock = document.getElementById("currentTime");
    var today = new Date();
    let hours = hourParse(today);
    let meridiam = ampm(today);
    let min = parseTime(today.getMinutes());
    let sec = parseTime(today.getSeconds());
    let day = parseDay(today.getUTCDay())
    var time = String(day + " " + today.getDate() + " / " + today.getMonth() + " / " + today.getFullYear() 
    + "\n" + hours + ":" + min + ":" + sec + " " + meridiam);
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

function filltable(data) {
    let table = document.getElementById("ptable");
    data.forEach(order => {

        let row = document.createElement('tr');
        ['orderID', 'dishIDs', 'customerID', 'address', 'cost', 'datetime',
            'employeeID', 'deliveryMethod', 'status'].forEach(key => {
                // itterate through those values in the order and create a column for each
                let column = null;
                switch (key) {
                    case 'employeeID':
                        // when filing in column for employeeID, check if employeeID exists and if it's a delivery
                        column = order['employeeID'] == null && order['deliveryMethod'] == 'delivery' ?
                            createElement('button', { text: 'Assign' }) : // if delivery have a button to assign deliveryBoy
                            createElement('td', { text: order[key] }); // else just display employeeID
                        break;
                    case 'orderID':
                        column = createElement('td');
                        let anchor = createElement('a', { href: `/orders/${order[key]}`, text: order[key] })
                        column.appendChild(anchor)
                        break;
                    default:
                        column = createElement('td', { text: order[key] });
                        break;
                }
                row.appendChild(column); // add the created column into the row
            })
        let button = createElement('button', { text: 'Cancel' })
        row.appendChild(button);
        table.appendChild(row); // add the row to table
    });
}



// 

getfromDB();
currentTime();

setInterval(() => { currentTime() }, 1000);

