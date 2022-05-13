async function getCurrentOrders() {
    const response = await fetch('/api/order/inprogress');
    const data = await response.json();
    console.log(data['response']);

    return data['response'];
}

async function showOrders() {
    let container = document.getElementById('orderlist');

    let orders = await getCurrentOrders();

    if (orders.length > 0) {
        orders.forEach(order => {
            if ((order.status != "cancelled" && order.status != "completed")  && ((order.deliveryMethod == "delivery" && order.employeeID != null) || (order.deliveryMethod == "pickup"))) {
                let orderdiv = createElement("a", {class: "orderdiv", href: `/dashboard/chefprogress/${order.orderID}`});
                Array.from(["orderID", "datetime", "deliveryMethod", "status", "cost"]).forEach(attrib => {
                    let element = createElement("p", {text: `${attrib.charAt(0).toUpperCase() + attrib.slice(1)} : ${order[attrib]}`, class: attrib});
                    orderdiv.appendChild(element);
                });
                container.appendChild(orderdiv);
            }
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

function reload() {
    eraseOrders();
    showOrders();
}

reload();

setInterval(() => {
    reload();
}, 10000);