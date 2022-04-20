// Functions for the clock
function currentTime() {
    let clock = document.getElementById("currentTime");
    var today = new Date();
    let hours = hourParse(today);
    let meridiam = ampm(today);
    let min = parseTime(today.getMinutes());
    let sec = parseTime(today.getSeconds());
    var time = String(hours + ":" + min + ":" + sec + " " + meridiam);
    clock.innerText = time;
}

function hourParse(today) {
    let hour = today.getHours();
    if (hour % 12 == 0) { return 12; }
    else { return hour % 12; }
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
                let column = null;
                switch (key) {
                    case 'employeeID':
                        column = order['employeeID'] == null && order['deliveryMethod'] == 'delivery' ?
                            createElement('button', { text: 'Assign' }) :
                            createElement('td', { text: order[key] });
                        break;
                    default:
                        column = createElement('td', { text: order[key] });
                        break;
                }
                row.appendChild(column);
            })
        let button = createElement('button', { text: 'Cancel' })
        row.appendChild(button);
        table.appendChild(row);
    });
}



// 

getfromDB();
currentTime();

setInterval(() => { currentTime() }, 1000);

