async function openModel(id){   // Makes model visible
    let item = await getItemId(id);  
    console.log(item)
    displayItem(item)
    let first = document.getElementsByClassName("item-info")[0]
    first.style.display = "block"
    let button = document.getElementById("actbutton");
    button.onclick = function() {
        addCartItem(JSON.stringify(item));
        closeModel();
        displayCart();
    }
}

function closeModel(){  // Makes model invisible 
    let first = document.getElementsByClassName("item-info")[0]
    first.style.display = "none"
}

async function getItemId(id){   // Retreives an item from Database by ID
    const response = await fetch('/api/menu/' + id);
    const data = await response.json();
    console.log(data['response'])
    return data['response']; 
}

// Get ratings of all dishes, need to change this to get average id

// async function getRatingId(id){
//     const response = await fetch('/api/ratings/' +id);
//     const data = await response.json();
//     return data ['respons']
// }
function displayItem(item){     // Displays an item in the cart.
   let element_names = document.getElementsByClassName("item-name");
   [...element_names].forEach(element => {
       element.textContent = item.dishName
   });

   let element_img = document.getElementsByClassName("item-img")[0];
   element_img.setAttribute('src',item.imageURL)

   document.getElementsByClassName("item-desc")[0].textContent = item.dishDescription

}