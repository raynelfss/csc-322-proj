// Information update == customers Only for now.

async function updateCustomerInfo(){
    let data = parseInfo();
    if (confirm("Are you sure you want to update your information?")) {
        response = await updateInfoDB(data);
        if (data['name'] == response['name'] && data['number'] == response['number']) {
            alert("Your information has been updated successfuly!");
        }
        else{
            alert("There's been an error updating your information, changes have been made.");
        }
        location.reload();
    }
}

function parseInfo() {
    let name = document.getElementById("fullname").value;
    let number = document.getElementById("phone").value;

    return {name, number};
}

async function filltextboxes() {
    let data = await getCustomerInfo();
    document.getElementById("fullname").value =  data['name'];
    document.getElementById("phone").value = data['number'];
}

async function getCustomerInfo() {
    const response = await fetch("/api/customer/editcustomer");
    const data = await response.json();
    return data['response'];
}

async function updateInfoDB(newinfo) {
    const response = await fetch("/api/customer/editcustomer", {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newinfo),
    });
    const data = await response.json();
    return data['response'];
}

filltextboxes();
