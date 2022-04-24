function openModel(id){
    let item = await getItemId(id)    
    let first = document.getElementsByClassName("item-info")[0]
    first.style.display = "block"
}

function closeModel(){
    let first = document.getElementsByClassName("item-info")[0]
    first.style.display = "none"
}

async function getItemId(id){
    const response = await fetch('/api/menu/' + id)
    const data = await response.json()
    return data['response']    
}