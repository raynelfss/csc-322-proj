function readlogininfo() {
    let username = document.getElementById("username").value
    let password = document.getElementById("password").value
    return { username, password };
}

async function login() {
    const info = readlogininfo();
    const response = await fetch("/api/auth/login", {
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
