// Password change functions

async function changePassword() {
    let data = parsePassword();
    // console.log(data)
    if (data != false) {
        if (confirm("Are you sure you want to change your password?")) {
            response = await postPassword(data);
            if (response == 'wrongpassword') {
                alert("Your current password is wrong. Password had not been changed.");
            }
            else{
                alert("Your password has been changed. You have been logged out!")
                location.replace("/");
            }
        }
    }
}

function parsePassword() {
    let password = document.getElementById("current").value;
    let newPassword = document.getElementById("new").value;
    let confirmnew = document.getElementById("confirmnew").value;
    let donotmatch = document.getElementsByClassName("donotmatch")[0]

    if (newPassword == confirmnew) {
        donotmatch.style.display = "none";
        return {password, newPassword};
    }
    else {
        donotmatch.style.display = "block";
        return false;
    }
}

async function postPassword(newpass) {
    const response = await fetch("/api/auth/password", {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newpass),
    });
    const data = await response.json();
    return data['response'];
}

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
