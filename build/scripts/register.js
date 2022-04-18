function getRegisterInfo() {
    let name = '';
    let phoneNumber = '';
    let username = document.getElementById("username").value
    let password = document.getElementById("password").value
    return { name, phoneNumber, username, password };
}

function displayError() {

}

async function login() {
    const info = readlogininfo();
    const response = await fetch("/api/auth/register", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(info),
    })
    if (response.redirected) {
        location.href = response.url;
    } else {
        // handle errors
    }
}
