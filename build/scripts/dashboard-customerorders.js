async function getCurrentOrders() {
    const response = await fetch('/api/order/fromcustomer');
    const data = await response.json();
    console.log(data['response']);

    return data['response'];
}

async function showOrders() {
    let container = document.getElementById('orderlist');

    let orders = await getCurrentOrders();

    if (orders.length > 0) {
        orders.forEach(order => {
            let orderdiv = createElement("a", {class: `orderdiv ${order['status']}`, href: "javascript:void(0)", onclick: `loadOrder(${order['orderID']})`});
            Array.from(["orderID", "datetime", "deliveryMethod", "status", "cost"]).forEach(attrib => {
                let element = createElement("p", {text: `${attrib.charAt(0).toUpperCase() + attrib.slice(1)} : ${order[attrib]}`, class: attrib});
                orderdiv.appendChild(element);
            });
            container.appendChild(orderdiv);
        });
    }
    else {
        let textdiv = createElement("div", {class : "noOrders"});
        let text = createElement("p", {text: "There are no active orders available. Please check back in a minute.", class: "noOrdersText"});
        textdiv.appendChild(text);
        container.appendChild(textdiv);
    }
}

function eraseOrders() {
    let orders = document.getElementsByClassName('orderdiv');
    if (orders.length > 0){
        Array.from(orders).forEach(element => {
            element.remove();
        });
    }
}

showOrders();
// function reload() {
//     eraseOrders();
//     showOrders();
// }

// reload();

// setInterval(() => {
//     if (!doNotReload) reload();
// }, 10000);
