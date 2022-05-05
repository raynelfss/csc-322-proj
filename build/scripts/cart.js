function createSelectField(id, quantity) {
    const select = createElement('select', { onchange: `onSelect('${id}')`, id: `${id}-quantity` });
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        .forEach(value => {
            const option = createElement('option', { value, text: value, selected: value == quantity });
            select.appendChild(option);
        })
    return select;
}

function onSelect(id) {
    const select = document.getElementById(`${id}-quantity`);
    updateItemQuantity(id, select.value);
}

function createItemInfo(name, price) {
    const cartItemInfo = createElement('div', { class: 'cart-item-info' });
    const itemName = createElement('p', { class: 'item-name', text: name });
    const itemPrice = createElement('p', { class: 'item-price', text: price });
    appendChildren(cartItemInfo, [itemName, itemPrice]);
    return cartItemInfo;
}

function createCartItem({ dishID, dishName, imageURL, price, quantity }) {
    console.log(dishID, dishName, imageURL, price, quantity);
    const cartItem = createElement('div', { class: 'cart-item ' });
    const select = createSelectField(dishID, quantity);
    const cartItemInfo = createItemInfo(dishName, price);
    const img = createElement('img', { src: imageURL });
    appendChildren(cartItem, [select, cartItemInfo, img]);
    return cartItem
}

function createCartItems(items = []) {
    const cartItems = createElement('div', { class: 'cart-items' });
    if (items.length != 0) {
        items.forEach(item => {
            const cartItem = createCartItem(item);
            cartItems.appendChild(cartItem);
        });
    } else {
        const p = createElement('p', { text: 'No items in cart yet.' })
        cartItems.appendChild(p)
    }
    return cartItems;
}

function createCartContainer({ items, total }) {
    const cartContainer = createElement('div', { class: 'cart-container' });
    const h2 = createElement('h2', { text: 'Cart' });
    const img = createElement('img', { class: 'close', src: './imgs/close.svg', onclick: 'hideCart()' })
    const cartItems = createCartItems(items);
    const buttonAttr = items.length == 0 ?
        { text: `Checkout | $${total}`, disabled: true, onclick: 'goToCheckout()' } :
        { text: `Checkout | $${total}`, onclick: 'goToCheckout()' };
    const button = createElement('button', buttonAttr)
    appendChildren(cartContainer, [h2, img, cartItems, button]);
    return cartContainer;
}

function displayCart() {
    const cart = getCart();
    const body = document.body;
    const overlay = createElement('div', { class: 'overlay', onclick: 'hideCart()' });
    const cartContainer = createCartContainer(cart)
    appendChildren(body, [overlay, cartContainer])
    body.classList.add('noscroll')
}

function hideCart() {
    document.getElementsByClassName('overlay')[0].remove();
    document.getElementsByClassName('cart-container')[0].remove();
    document.body.classList.remove('noscroll');

}

function refreshCart() { 
    if (document.getElementsByClassName('overlay').length > 0) {
        hideCart();
        displayCart();
    }
}

function getCart() {
    let cart = localStorage.getItem('cart');
    if (!cart) {
        cart = { items: [], total: 0 }
        localStorage.setItem('cart', JSON.stringify(cart));
    }
    else { cart = JSON.parse(cart); }
    return cart;
}

// menuItem = { dishID, dishName, description, price, imageURL, chefID }
// cartItem = { dishID, dishName, description, price, imageURL, chefID, quantity }
function addCartItem(menuItem, quantity = 1) {
    if (typeof (menuItem) == 'string') menuItem = JSON.parse(menuItem);
    
    let cart = getCart();
    let cartItem = cart.items.find(({ dishID }) => menuItem.dishID == dishID);
    if (cartItem) { // if item already in cart, increment item quantity by quantity
        updateItemQuantity(cartItem.dishID, Number(cartItem.quantity) + quantity); return;
    }
    cart.items.push({ ...menuItem, quantity });
    cart.total += quantity * menuItem.price;
    localStorage.setItem('cart', JSON.stringify(cart));
}

function removeCartItem(dishID) {
    let cart = getCart();
    cart.items = cart.items.filter(item => item.dishID != dishID);
    cart.total = getCartTotal(cart.items);
    localStorage.setItem('cart', JSON.stringify(cart));
    refreshCart();
}

function updateItemQuantity(dishID, newQuantity) {
    if (newQuantity == 0) { removeCartItem(dishID); return; }
    if (newQuantity > 10) { return; }

    let cart = getCart();
    let i = cart.items.findIndex(item => item.dishID == dishID);
    if (i > -1) {
        cart.items[i].quantity = newQuantity;
        cart.total = getCartTotal(cart.items);
        localStorage.setItem('cart', JSON.stringify(cart));
        refreshCart();
    }
}

function getCartTotal(items) {
    let total = 0;
    items.forEach(item => { total += item.price * item.quantity; });
    return total;
}

function clearCart() {
    localStorage.setItem('cart', JSON.stringify({ items: [], total: 0 }));
}

function goToCheckout() {
    window.location = '/checkout'
}