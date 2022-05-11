var isModalOpen = false;

async function getOrders() {    // Retreive orders pending orders from database.
    const response = await fetch('/api/order/inprogress');
    const data = await response.json();

    if (response.headers.get("content-type") === 'application/json') {
        return data['response'] || [];
    }
    return [];
}

function getBid() {
    return document.getElementById('bid').value;
}

async function postBid(orderID) {
    const amount = getBid();
    const data = JSON.stringify({ amount, orderID });
    const response = await fetch('/api/bids/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: data
    });
    // handle error with status 400
    if (response.status === 400) {
        const message = await response.text();
        alert(message);
    }
    closeBidModal();

}

function createOrder(order) {
    const orderDiv = createElement('div', { class: 'order' });
    ['address', 'datetime'].forEach(field => {
        const element = createElement('p', { text: order[field] });
        orderDiv.appendChild(element);
    });
    const button = createElement('button', { text: 'Bid', onclick: `openBidModal(${order.orderID})` });
    orderDiv.appendChild(button);
    return orderDiv;
}

async function loadOrders() {
    const orders = await getOrders() || [];
    const ordersDiv = document.getElementsByClassName('orders')[0];
    if (orders.length > 0) {
        orders.forEach(order => {
            const orderDiv = createOrder(order);
            ordersDiv.appendChild(orderDiv);
        })
    }
    else {
        ordersDiv.appendChild(createElement("h1", {"text" : "There are no active orders at the moment."}))
    }
}

function clearOrders() {
    let children = document.getElementsByClassName('order') || [];
    Array.from(children).forEach(element => {
        element.remove();
    });
}

function reload() {
    clearOrders();
    loadOrders();
}

// bid modal


function openBidModal(orderID) {
    isModalOpen = true;
    const modalContainer = document.getElementsByClassName('modalContainer')[0];
    document.getElementsByClassName('modalCancel')[0].setAttribute('onclick', 'closeBidModal()');
    document.getElementsByClassName('place')[0].setAttribute('onclick', `postBid(${orderID})`);
    modalContainer.style.display = 'block';

}

function closeBidModal() {
    const modalContainer = document.getElementsByClassName('modalContainer')[0];
    modalContainer.style.display = 'none';
    isModalOpen = false;
}

reload();
setInterval(() => {
    if(!isModalOpen) {
        reload();
    }
}, 10000);