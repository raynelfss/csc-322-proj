async function getOrder() {
    const url = window.location.href
    const urlSplitted = url.split('/');
    const id = urlSplitted[urlSplitted.length - 1];
    const response = await fetch(`/api/order/${id}`);
    if (response.headers.get("content-type") === 'application/json') {
        const data = await response.json();
        const order = data['response'];
        return order
    }
    return undefined
}

async function loadOrder() {
    const order = await getOrder();
    // console.log(order)
    if (order) {
        // set order id
        document.getElementsByClassName('order-id')[0].textContent = `Order ID: ${order['orderID']}`
        // display order items
        loadOrderItems(order['dishes'])
        // display order costs
        loadCosts(order['dishes'], order['deliveryMethod'] === 'delivery');
        // display order status
        loadStatus(order['status'])
    } else {
        orderContainer = document.getElementsByClassName('order-container')[0];
        notFound = createElement('p', { text: 'Order not found' })
        orderContainer.appendChild(notFound);
    }
}

function loadOrderItems(items) {
    const orderItems = document.getElementsByClassName('order-items')[0];
    let h2 = createElement('h2', { text: 'Items' });
    orderItems.appendChild(h2);
    items.forEach(item => {
        orderItem = createOrderItem(item);
        orderItems.appendChild(orderItem);
    })
}

function createOrderItem(item) {
    const orderItem = createElement('div', { class: 'order-item' });
    const image = createElement('img', { src: item['imageURL'] });
    const dishName = createElement('h3', { text: item['dishName'] });
    const quantity = createElement('p', { text: `Quantity: ${item['quantity']}` });
    appendChildren(orderItem, [image, dishName, quantity])
    return orderItem
}

function loadCosts(items, isDelivery) {
    const prices = calculateCartPrice(items, isDelivery);
    const orderCosts = document.getElementsByClassName('order-cost')[0]
    const h2 = createElement('h2', { text: 'Costs' });
    orderCosts.appendChild(h2);
    const priceElementArray = Object.keys(prices).map(priceType => {
        return createElement('p', { text: `${priceType}: ${prices[priceType].toFixed(2)}` });
    })
    appendChildren(orderCosts, priceElementArray);

}
// cur
function calculateCartPrice(items, isDelivery) {
    let subtotal = 0;
    let taxes = 0;
    let deliveryFee = 0;
    let total = 0;
    items.forEach(item => { subtotal = item.price * item.quantity; })
    taxes = subtotal * 0.08875;
    isDelivery && (deliveryFee = 7.99);
    total = subtotal + taxes + deliveryFee;
    return { subtotal, taxes, deliveryFee, total };
}

function loadStatus(status) {
    const orderStatus = document.getElementsByClassName('order-status')[0];
    const h2 = createElement('h2', { text: 'Status' });
    const p = createElement('p', { text: status });
    appendChildren(orderStatus, [h2, p]);
}

loadOrder()