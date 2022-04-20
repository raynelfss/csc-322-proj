let isDelivery = false;

function handleClick(e) {
    if (e.target.value == 'pickUp') {
        isDelivery = false; hideLocationForm();
    }
    else {
        isDelivery = true; displayLocationForm();
    }
    loadPrice();
}

function hideLocationForm() {
    document.getElementsByClassName('address-section')[0].style.display = 'None';
}

function displayLocationForm() {
    document.getElementsByClassName('address-section')[0].style.display = 'Flex';
}

const createSelectField = (id, quantity) => {
    const select = createElement('select', { onchange: `handleSelect('${id}')`, id: `${id}-quantity` });
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        .forEach(value => {
            const option = createElement('option', { value, text: value, selected: value == quantity });
            select.appendChild(option);
        })
    return select;
}

function createCheckoutItem(item) {
    const checkoutItem = createElement('div', { class: 'checkout-item' });
    const img = createElement('img', { src: item.img_url })
    const select = createSelectField(item.id, item.quantity);
    const infoContainer = createElement('div', { class: 'checkout-item-info' });
    const name = createElement('p', { text: item.name })
    const price = createElement('p', { text: item.price });
    appendChildren(infoContainer, [name, price]);
    appendChildren(checkoutItem, [select, infoContainer, img]);
    return checkoutItem;
}

function handleSelect(id) {
    const select = document.getElementById(`${id}-quantity`);
    updateItemQuantity(id, select.value);
}

function loadCheckoutCart() {
    let cart = getCart();
    const itemsSection = document.getElementsByClassName('items-section')[0];
    const checkoutItems = createElement('div', { class: 'checkout-items' });
    cart.items.forEach(item => {
        const checkoutItem = createCheckoutItem(item);
        checkoutItems.appendChild(checkoutItem);
    })
    itemsSection.appendChild(checkoutItems);
    loadPrice();
}

function clearCheckoutCart() {
    document.getElementsByClassName('checkout-items')[0].remove();
}

const refreshCheckoutCart = () => { clearCheckoutCart(); loadCheckoutCart(); }

// getCart, removeCartItem, updateItemQuantity, getCartTotal, clearCart imported from ./cart.js


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

function loadPrice() {
    let cart = getCart();
    let prices = calculateCartPrice(cart.items, isDelivery);
    Object.keys(prices).forEach(priceType => {
        document.getElementById(priceType).textContent = prices[priceType].toFixed(2);
    })
}

function getDishIDs() {
    let cart = getCart();
    let ids = [];
    cart.items.forEach(item => {
        for (let i = 0; i < item.quantity; i++) ids.push(item.id);
    })
    return ids;
}

function getAddress() {
    return ['address1', 'address2', 'city', 'state', 'zipcode'].map(addressField => (
        document.getElementById(addressField).value || undefined
    )).filter(field => field != undefined).join(', ');
}

async function checkout() {
    const dishIDs = getDishIDs();
    const deliveryMethod = isDelivery ? 'delivery' : 'pickup';
    const address = isDelivery ? getAddress() : null;
    const data = JSON.stringify({ dishIDs, deliveryMethod, address });
    console.log(data);
    const response = await fetch('/api/order/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: data
    });
}

// clean up unnessary functions and code later
loadCheckoutCart();
document.getElementById('checkout-button').addEventListener('click', checkout);