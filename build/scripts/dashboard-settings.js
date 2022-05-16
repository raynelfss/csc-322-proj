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
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newpass),
    });
    const data = await response.json();
    console.log(data['response']);
    return data['response'];
}