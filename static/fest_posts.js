
let festpostForm = document.querySelector('#festpost-form');

// const myTimeout = setTimeout(fetchResults, 3000);

setTimeout(fetchResults, 500)


function festlikePost(festpost_id) {
    fetch(`/like/${festpost_id}`, { method: 'POST' })
    .then((response) => response.json())
    .then((resp) => {
        let heartIcon = document.querySelector(`#heart-${festpost_id}`);
        if (heartIcon.classList.contains('bx-heart')) {
            heartIcon.classList.remove('bx-heart');
            heartIcon.classList.add('bxs-heart');
        } else if (heartIcon.classList.contains('bxs-heart')) {
            heartIcon.classList.remove('bxs-heart');
            heartIcon.classList.add('bx-heart');
        }
        
        const likesCount = document.getElementById(`likes-count-${festpost_id}`);
        if (resp['added'] == 'Success!') {
            likesCount.textContent = parseInt(likesCount.textContent) + 1;
        } else if (resp['added'] == 'Unliked') {
            likesCount.textContent = parseInt(likesCount.textContent) - 1;
        }
    })
    .catch(error => console.error('Error:', error));
}


function fetchResults() {

    let festId = document.querySelector('#hidden-fest-id').value;
    console.log(festId);

    fetch(`/festpost-results.json/${festId}`, {
        method: 'GET'
    })
    .then((response) => response.json())
    .then((results) => {
        //select the empty div, save it in a variable
        const festpostResultsContainer = document.querySelector('#festpost-results');
        
        // Clear existing posts before appending new ones
        festpostResultsContainer.innerHTML = '';
        console.log(results)
        // Loop over each post in the results array
        results.forEach(festpost => {
            // Create HTML elements for each post
            const festpostElement = document.createElement('div');
            // postElement.classList.add('post');
            festpostElement.innerHTML = `
                <div class="festpost-container">
                    <div class="content">

                        <div class="username">@${festpost.username}</div>
                        <p>${festpost.content}</p>

                        <div class="iconbx">
                            <div class"commentbtn"><i class='bx bx-message-dots bx-flip-horizontal'></i></div>
                            <div class"sharebtn"><i class='bx bx-share'></i></div>
                            <button class="heartbtn" onclick="likePost(${festpost.festpost_id})"><i class='bx bx-heart' id="heart-${festpost.post_id}"></i>
                            <span><span id="likes-count-${festpost.post_id}"> ${festpost.like_count} </span></span></button>
                        </div>

                    </div>
                </div>
            `;
            // Append the post element to the container
            festpostResultsContainer.appendChild(festpostElement);
        });
    })
    .catch(error => console.error('Error:', error));

}


{/* <div class="festpost-avatar"> <img src=${festpost.avatar}> </div> */}