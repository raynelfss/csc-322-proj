
async function autoAssign(id) {
    const allbids = await getBids(id);
    console.log(id);
    console.log(allbids);
}

async function getBids(id) {
    const response = await fetch('/api/bids/orderID/' + String(id))
    const data = await response.json();
    // console.log(data);
    return data['response'];
}