async function addItem() {
    const obj = {
        id: 10, 
        name: 'Husan', 
        img_url: 'url.png', 
        description: 'ur dad',
        price: 420
    }
    const response = await fetch('http://127.0.0.1:5000/menu', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(obj)
    });
    const data = await response.json()
    console.log(data);
}