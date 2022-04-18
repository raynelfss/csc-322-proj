// Functions for the clock

function currentTime() {
    let clock = document.getElementById("currentTime")
    var today = new Date()
    let hours = hourParse(today)
    let meridiam = ampm(today)
    let min = parseTime(today.getMinutes())
    let sec = parseTime(today.getSeconds())
    var time = String(hours + ":" + min + ":" + sec + " " + meridiam)
    clock.innerText = time
}

function hourParse(today) {
    let hour = today.getHours()
    if (hour%12 == 0) {
        return 12
    }
    else {
        return hour%12
    }
}

function ampm(today) {
    let hour = today.getHours()
    if (hour < 12) {
        return "AM"
    }
    else {
        return "PM"
    }
}

function parseTime(temp) {
    if (temp < 10) {
        return "0" + temp
    }
    else {
        return temp
    }
}

currentTime()

setInterval(() => {
    currentTime()    
}, 1000);

