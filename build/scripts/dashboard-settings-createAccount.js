
async function createUser() {
    let data = parseData();
    //console.log(data);
    if (data != false) {
        if (confirm(`Are you sure you want to create the following employee user?\nUsername: ${data['username']}\nEmployee type: ${data['employeeType']}`)) {
             response = await postUser(data);
             if (response == 'exists') {
                 alert("User was not created due to existing username.");
             }
             else {
                 alert("User was created successfully!");
             }
         }
    }
}

function parseData() {      // Returns dict with user data
    let username = document.getElementById("username").value;
    let password = getPassword();
    let employeeType = getEmployeeType();
    if (password == false) {
        return false;
    }

    return {username, password, employeeType}
}

function getPassword() {        // gets the password from document
    let pass = document.getElementById("unew").value;
    let conf = document.getElementById("unewconfirm").value;
    let donotmatch = document.getElementsByClassName("donotmatch")[0];

    if (pass == conf) {
        donotmatch.style.display = "none";
        return pass;
    }
    else {
        donotmatch.style.display = "block";
        return false;
    }
}

function getEmployeeType() { // gets employeetype from options.
    let number = document.getElementById("employeeselector").value;
    let employeeTypes = ["manager", "chef", "deliveryPerson"];
    return employeeTypes[number];
}

async function postUser(user){
    const response = await fetch("/api/auth/hire", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(user),
    });
    const data = await response.json();
    console.log(data['response']);
    return data['response'];
}