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


const  previousBtn  =  document.getElementById('previousBtn');
const  nextBtn  =  document.getElementById('nextBtn');
// const  finishBtn  =  document.getElementById('finishBtn');
const  content  =  document.getElementById('content');
const  bullets  =  [...document.querySelectorAll('.circle')];

const MAX_STEPS = 3;
let currentStep = 1;

nextBtn.addEventListener('click',  ()  =>  {
	bullets[currentStep  -  1].classList.add('completed');
	currentStep  +=  1;
	previousBtn.disabled  =  false;
	if  (currentStep  ===  MAX_STEPS)  {
		nextBtn.disabled  =  true;
		// finishBtn.disabled  =  false;
	}
	content.innerText  =  `Step ${currentStep}`;
});


previousBtn.addEventListener('click',  ()  =>  {
	bullets[currentStep  -  2].classList.remove('completed');
	currentStep  -=  1;
	nextBtn.disabled  =  false;
	// finishBtn.disabled  =  true;
	if  (currentStep  ===  1)  {
		previousBtn.disabled  =  true;
	}
	content.innerText  =  `Step ${currentStep}`;
});

// finishBtn.addEventListener('click',  ()  =>  {
// 	location.reload();
// });
// when done with order, page will reload