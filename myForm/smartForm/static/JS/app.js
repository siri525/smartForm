var team_size = document.querySelector('#options');
var mem3 = document.querySelector('.team-3');
team_size.addEventListener('change', () => {
    if (team_size.value == 2) { 
        mem3.style.display = "none";
    }
    else {
        mem3.style.display = "block";
    }
})
