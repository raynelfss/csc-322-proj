function readlogininfo() {
    let user = document.getElementById("username").value
    let pass = document.getElementById("password").value

    let info = { "username": user, "password" : pass }
    console.log(info)
    return info
}

async function requestToDB(info) {
    const response = await fetch("/api/login/", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(info),
    })
    const content = await response.json()
    return content
}

async function login(){
    let response = requestToDB(readlogininfo())
    console.log(response)
}

//TO-DO: Implement login functionality using Js.