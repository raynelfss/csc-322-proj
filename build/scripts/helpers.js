function createElement(tag, attributes = {}) {
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
    return element;
}

function appendChildren(parent, children = []) {
    children.forEach(child => parent.appendChild(child));
}