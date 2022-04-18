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

const createSelectField = (id, quantity) => {
    const select = cE('select', { onchange: `onSelect('${id}')`, id: `${id}-quantity` });
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        .forEach(value => {
            const option = cE('option', { value, text: value, selected: value == quantity });
            select.appendChild(option);
        })
    return select;
}

const onSelect = (id) => {
    const select = document.getElementById(`${id}-quantity`);
    updateItemQuantity(id, select.value);
}

const createItemInfo = (name, price) => {
    const cartItemInfo = cE('div', { class: 'cart-item-info' });
    const itemName = cE('p', { class: 'item-name', text: name });
    const itemPrice = cE('p', { class: 'item-price', text: price });
    appendChildren(cartItemInfo, [itemName, itemPrice]);
    return cartItemInfo;
}

const createCartItem = ({ id, name, img_url, price, quantity }) => {
    const cartItem = cE('div', { class: 'cart-item ' });
    const select = createSelectField(id, quantity);
    const cartItemInfo = createItemInfo(name, price);
    const img = cE('img', { src: img_url });
    appendChildren(cartItem, [select, cartItemInfo, img]);
    return cartItem
}

const createCartItems = (items = []) => {
    const cartItems = cE('div', { class: 'cart-items' });
    if (items.length != 0) {
        items.forEach(item => {
            const cartItem = createCartItem(item);
            cartItems.appendChild(cartItem);
        });
    } else {
        const p = cE('p', { text: 'No items in cart yet.' })
        cartItems.appendChild(p)
    }
    return cartItems;
}

const createCartContainer = ({ items, total }) => {
    const cartContainer = cE('div', { class: 'cart-container' });
    const h2 = cE('h2', { text: 'Cart' });
    const img = cE('img', { class: 'close', src: './imgs/close.svg', onclick: 'hideCart()' })
    const cartItems = createCartItems(items);
    const buttonAttr = items.length == 0 ?
        { text: `Checkout | $${total}`, disabled: true, onclick: 'hideCart()' } :
        { text: `Checkout | $${total}`, onclick: 'hideCart()' };
    const button = cE('button', buttonAttr)
    appendChildren(cartContainer, [h2, img, cartItems, button]);
    return cartContainer;
}

const displayCart = () => {
    const cart = getCart();
    const body = document.body;
    const overlay = cE('div', { class: 'overlay', onclick: 'hideCart()' });
    const cartContainer = createCartContainer(cart)
    appendChildren(body, [overlay, cartContainer])
    body.classList.add('noscroll')
}

const hideCart = () => {
    document.getElementsByClassName('overlay')[0].remove();
    document.getElementsByClassName('cart-container')[0].remove();
    document.body.classList.remove('noscroll');

}

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

const clearCart = () => {
    localStorage.setItem('cart', JSON.stringify({ items: [], total: 0 }));
}