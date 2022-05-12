function update(){
    circles.forEach((circle, idx) => {
        if (idx < currenActive) {
            circle.classList.add("active");
        }
        else {
            circle.classList.remove("active");
        }
    });

    const actives = document.querySelectorAll(".active");
    progress.style.wdith = 
        ((actives.length -1) / (circles.length -1)) * 100 + "%";

    if (currentActive === 1) {
        prev.disabled = true;

    }
    else if(currentActive === circles.length) {
        next.disabled = true;
    }
    else {
        prev.disabled = false;
        next.disabled = false;
    }
}