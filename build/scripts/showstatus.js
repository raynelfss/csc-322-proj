var ratings; //retrieve ratings from db?
var total = 0;
for(var i = 0; i < ratings.length; i++) {
    total += ratings[i];
}
var avg = total/ratings.length;

var complaints;
var demotes;
var compliments;

function showStatus() {
    if ((avg <= 2) || (complaints >= 3)) {
        document.getElementById('doThis').innerHTML = "You have been demoted";
    }
    
    if (demotes = 2) {
        document.getElementById('doThis').innerHTML = "You have been demoted";
    }

    if ((avg >= 4) || (compliments >= 3)) {
        document.getElementById('doThis').innerHTML = "You have been demoted";
    }
}