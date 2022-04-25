async function getOrders() {
    const response = await fetch('/api/order');
    const data = await response.json();

    if (response.headers.get("content-type") === 'application/json') {
        return data['response'] || [];
    }
    return [];
}

async function postBid(bid) {
    const response = await fetch('/api/orders', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: bid
    });
    // handle error with status 400
    if (response.status === 400) {
        const message = await response.text();
        alert(message);
    }
}

function createOrder(order) {
    const orderDiv = createElement('div', { class: 'order' });
    ['address', 'datetime'].forEach(field => {
        const element = createElement('p', { text: order[field] });
        orderDiv.appendChild(element);
    });
    // const button = createElement('button', {onclick: )}
    return orderDiv;
}

async function loadOrders() {
    const orders = await getOrders();
    const ordersDiv = document.getElementsByClassName('orders')[0];
    orders.forEach(order => {
        const orderDiv = createOrder(order);
        ordersDiv.appendChild(orderDiv);
    })
}

// bid modal


function openBidModal(orderID) {

}

function closeBidModal() { }

loadOrders()