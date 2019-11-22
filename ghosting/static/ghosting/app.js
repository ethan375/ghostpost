// console.log('testing')

let upVotes = document.getElementsByClassName('up-vote')
let downVotes = document.getElementsByClassName('down-vote')

for(let i = 0; i < upVotes.length; i++) {
    let id = upVotes[i].parentElement.children[0].innerHTML 

    upVotes[i].addEventListener('click', () => {
        fetch(`http://localhost:8000/ghosting/vote/up/${id}`, {
            method: "POST",
        })
    })
}

for(let i = 0; i < downVotes.length; i++) {
    let id = downVotes[i].parentElement.children[0].innerHTML 

    downVotes[i].addEventListener('click', () => {
        fetch(`http://localhost:8000/ghosting/vote/down/${id}`, {
            method: "POST",
        })
    })
}