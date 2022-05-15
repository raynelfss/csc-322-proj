function displaySidebar() {
    document.getElementById('sidebar').style.width = "300px";
    doNotReload = true;
}

function hideSidebar() {
    document.getElementById('sidebar').style.width = "0";
    doNotReload = false;
}