async function getOrder(id) {
    const response = await fetch(`/api/order/${id}`);
    if (response.headers.get("content-type") === 'application/json') {
        const data = await response.json();
        const order = data['response'];
        return order
    }
    return undefined
}



async function loadOrder(id) {
    const order = await getOrder(id);
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
    }
    else {
        orderContainer = document.getElementsByClassName('order-container')[0];
        notFound = createElement('p', { text: 'Order not found' })
        orderContainer.appendChild(notFound);
    }
    openModel();
}

function loadOrderItems(items) {
    const orderItems = document.getElementsByClassName('order-items')[0];
    let h2 = createElement('h2', { text: 'Items' });
    let itemdiv = createElement('div', {class:'order-items-div'})
    orderItems.appendChild(h2);
    items.forEach(item => {
        orderItem = createOrderItem(item);
        itemdiv.appendChild(orderItem);
    })
    orderItems.appendChild(itemdiv);
}

function createOrderItem(item) {
    const orderItem = createElement('div', { class: 'order-item' });
    const image = createElement('img', { class: 'order-img', src: item['imageURL'] });
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

function openModel() { // Opens a selected modal.
    const back = document.getElementById('displayblock');
    back.onclick = function() {closeModel();};
    back.style.display = "block";
    console.log(back);
    const model = document.getElementById('ordermodel');
    model.style.display = "block";
}

function closeModel() { // Closes a selected modal.
    document.getElementById('displayblock').style.display = "none";
    const model = document.getElementById('ordermodel');
    model.style.display = "none";
    cleanModel();
}

function cleanModel(){
    document.getElementsByClassName('order-id')[0].textContent = "";

    let orderitems = document.getElementById("order-items").children;
    Array.from(orderitems).forEach(element => {
        element.remove();
    });
    let ordercost = document.getElementById("order-cost").children;
    Array.from(ordercost).forEach(element => {
        element.remove();
    });
    let orderstatus = document.getElementById("order-status").children;
    Array.from(orderstatus).forEach(element => {
        element.remove();
    });
}