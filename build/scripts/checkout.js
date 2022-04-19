let isDelivery = false;

const cE = (tag, attributes = {}) => {
    const element = document.createElement(tag);
    Object.keys(attributes).forEach(attribute => {
        switch (attribute) {
            case 'text':
                element.textContent = attributes[attribute];
                break;
            default:
                if (attributes[attribute]) {
                    element.setAttribute(attribute, attributes[attribute]);
                    break;
                }
        }
    })
    return element
}

const appendChildren = (parent, children = []) => {
    children.forEach(child => parent.appendChild(child));
}

function handleClick(e) {
    if (e.target.value == 'pickUp') {
        isDelivery = false; hideLocationForm();
    }
    else {
        isDelivery = true; displayLocationForm();
    }
    displayPrice();
}

function hideLocationForm() {
    document.getElementsByClassName('address-section')[0].style.display = 'None';
}

function displayLocationForm() {
    document.getElementsByClassName('address-section')[0].style.display = 'Flex';
}

const createSelectField = (id, quantity) => {
    const select = cE('select', { onchange: `onSelect('${id}')`, id: `${id}-quantity` });
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        .forEach(value => {
            const option = cE('option', { value, text: value, selected: value == quantity });
            select.appendChild(option);
        })
    return select;
}

function createCheckoutItem(item) {
    const checkoutItem = cE('div', { class: 'checkout-item' });
    const img = cE('img', { src: item.img_url })
    const select = createSelectField(item.id, item.quantity);
    const infoContainer = cE('div', { class: 'checkout-item-info' });
    const name = cE('p', { text: item.name })
    const price = cE('p', { text: item.price });
    appendChildren(infoContainer, [name, price]);
    appendChildren(checkoutItem, [select, infoContainer, img]);
    return checkoutItem;
}

const onSelect = (id) => {
    const select = document.getElementById(`${id}-quantity`);
    updateItemQuantity(id, select.value);
}

function displayCart() {
    let cart = getCart();
    const itemsSection = document.getElementsByClassName('items-section')[0];
    const checkoutItems = cE('div', { class: 'checkout-items' });
    cart.items.forEach(item => {
        const checkoutItem = createCheckoutItem(item);
        checkoutItems.appendChild(checkoutItem);
    })
    itemsSection.appendChild(checkoutItems);
    displayPrice();
}

function hideCart() {
    document.getElementsByClassName('checkout-items')[0].remove();
}

// update cart
// update price
// calculate price
// place order
const refreshCart = () => { hideCart(); displayCart(); }

const getCart = () => {
    let cart = localStorage.getItem('cart');
    if (!cart) {
        cart = { items: [], total: 0 }
        localStorage.setItem('cart', JSON.stringify(cart));
    }
    else { cart = JSON.parse(cart); }
    return cart;
}

const addCartItem = (id, name, price, img_url, quantity) => {
    let cart = getCart();
    let item = cart.items.find(item => item.id == id);
    if (item) {
        updateItemQuantity(id, Number(item.quantity) + 1); return;
    }
    cart.items.push({ id, name, price, img_url, quantity });
    cart.total += quantity * price;
    localStorage.setItem('cart', JSON.stringify(cart));
}

const removeCartItem = (itemID) => {
    let cart = getCart();
    cart.items = cart.items.filter(({ id }) => id != itemID);
    cart.total = getCartTotal(cart.items);
    localStorage.setItem('cart', JSON.stringify(cart));
    refreshCart();
}

const updateItemQuantity = (itemID, newQuantity) => {
    if (newQuantity == 0) { removeCartItem(itemID); return; }
    if (newQuantity > 10) { return; }

    let cart = getCart();
    let i = cart.items.findIndex(({ id }) => id == itemID);
    if (i > -1) {
        cart.items[i].quantity = newQuantity;
        cart.total = getCartTotal(cart.items);
        localStorage.setItem('cart', JSON.stringify(cart));
        refreshCart();
    }
}

const getCartTotal = (items) => {
    let total = 0;
    items.forEach(item => { total += item.price * item.quantity; });
    return total;
}

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

function displayPrice() {
    let cart = getCart();
    let prices = calculateCartPrice(cart.items, isDelivery);
    Object.keys(prices).forEach(priceType => {
        document.getElementById(priceType).textContent = prices[priceType].toFixed(2);
    })
}

const clearCart = () => {
    localStorage.setItem('cart', JSON.stringify({ items: [], total: 0 }));
}

function getItemIds() {
    let cart = getCart();
    let ids = [];
    cart.items.forEach(item => {
        for (let i = 0; i < item.quantity; i++) ids.push(item.id);
    })
    return ids;
}

function getAddress() {
    return ['address1', 'address2', 'city', 'state', 'zipcode'].map(addressField => (
        document.getElementById(addressField).value
    )).join(', ');
}

async function checkout() {
    const dishIDs = getItemIds();
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
displayCart();
document.getElementById('checkout-button').addEventListener('click', checkout);