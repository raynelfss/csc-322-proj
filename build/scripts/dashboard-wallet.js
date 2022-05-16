async function displayAccountBalance() {      // Displays current balance availale in account
    const balance = document.getElementById("balance");
    const currBalance = await getBalance();
    balance.innerText = parseBalance(currBalance['balance']);
}

async function getBalance() {   // Gets balance from the SQL Server
    const response = await fetch('/api/wallet/');
    const data = await response.json();
    return data['response'];
}

function parseBalance(balance) {    // Ensures specificity in balance.
    return '$' + Number(String(balance)).toFixed(2);
}

function openModel(modelName) { // Opens a selected modal.
    const back = document.getElementById('displayblock');
    back.onclick = function() {closeModel(modelName);};
    back.style.display = "block";
    const model = document.getElementById(modelName);
    model.style.display = "flex";
}

function closeModel(modelName) { // Closes a selected modal.
    document.getElementById('displayblock').style.display = "none";
    const model = document.getElementById(modelName);
    model.style.display = "none";
}

async function deposit() {
    let amount = document.getElementById('depositamount').value;
    let newAmount = parseBalance(amount)
    if (Number(amount) >= 1) {
        if (confirm(`Are you sure you want to deposit ${newAmount} to your account?`)) {
            setTimeout(() => {
                depositToDB(amount);
                let success = document.getElementsByClassName('success');
                Array.from(success).forEach(element => {
                    element.style.display = 'block'
                });
            }, 3000);
            setTimeout(() => {
                location.reload();
            }, 5000);
        }
    }
    else {
        alert("The minimal transaction amount is $1.00, try again.")
    }
}

async function depositToDB(amount) {
    const response = await fetch('/api/wallet/', {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({'balance' : amount}),
    });
    const data = await response.json();
}
displayAccountBalance()