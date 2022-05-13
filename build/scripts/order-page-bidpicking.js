
async function autoAssign(id) {
    const allbids = await getBids(id);
    doNotReload = true;
    if (allbids.length > 0) {   // Checks whether there are bids avalable.
        var smallest = selectSmallest(allbids);
        
        if (confirm("The following bid will be selected:\n\tEmplID: " + 
        String(smallest.employeeID) + "\n\tAmount: " + String(smallest.amount.toFixed(2)) + 
        "\n\t BidID: " + String(smallest.bidID))) {
            let order = await getOrderByID(smallest.orderID);
            order.employeeID =  smallest.employeeID;

            let dishes = order.dishIDs.split(',');
            order.dishIDs = dishes;
            
            updateItem(order.orderID, order);
            doNotReload = false;
            setTimeout(() => {
                location.reload();
            }, 1000);
        }
    }
    else {
        alert("There are no bids for this order yet, try again later.");
    }
}

async function getBids(id) {        // Gets bids from database
    const response = await fetch('/api/bids/orderID/' + String(id))
    const data = await response.json();
    // console.log(data);
    return data['response'];
}

function selectSmallest(bids) {
    var smallest = bids[0].amount;
    // console.log(smallest)
    var smallestBid = bids[0];
    bids.forEach(bid => {
        if (bid.amount < smallest) {
            smallestBid = bid;
        }
    });
    return smallestBid;

}