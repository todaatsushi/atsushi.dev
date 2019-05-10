window.onload = adjustScore

var adjustScore = (val) => {
    var allScoreCards = Array.from(
        document.getElementsByClassName('score')
    );
    console.log(allScoreCards);

    allScoreCards.map(card => {
        console.log(card);
        card.style.display = 'none';
    })

    var scoreDiv = document.getElementById('score-x'.replace('x', val));
    console.log(scoreDiv);
    scoreDiv.style.display = 'block';
};