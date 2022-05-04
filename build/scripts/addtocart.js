async function openModel(id){
    let item = await getItemId(id);  
    console.log(item)
    displayItem(item)
    let first = document.getElementsByClassName("item-info")[0]
    first.style.display = "block"
    let button = document.getElementById("actbutton");
    button.onclick = function() {
        addCartItem(JSON.stringify(item));
        closeModel();
    }
}

function closeModel(){
    let first = document.getElementsByClassName("item-info")[0]
    first.style.display = "none"
}

async function getItemId(id){
    const response = await fetch('/api/menu/' + id);
    const data = await response.json();
    console.log(data['response'])
    return data['response']; 
}

function displayItem(item){
   let element_names = document.getElementsByClassName("item-name");
   [...element_names].forEach(element => {
       element.textContent = item.dishName
   });

   let element_img = document.getElementsByClassName("item-img")[0];
   element_img.setAttribute('src',item.imageURL)

   document.getElementsByClassName("item-desc")[0].textContent = item.dishDescription

}