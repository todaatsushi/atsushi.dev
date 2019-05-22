const adjustScore = (val) => {
    let allScoreCards = Array.from(
        document.getElementsByClassName('score')
    );
    
    // Start by hiding all options
    allScoreCards.map(card => {
        card.style.display = 'none';
    })

    // Show the valid option
    let scoreDiv = document.getElementById('score-x'.replace('x', val));
    scoreDiv.style.display = 'block';
};

window.onload = adjustScore(1);