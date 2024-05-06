
let postForm = document.querySelector('#post-form');

// const myTimeout = setTimeout(fetchResults, 3000);

setTimeout(fetchResults, 3000)


function likePost(post_id) {
    fetch(`/like/${post_id}`, { method: 'POST' })
    .then((resp) => {
        console.log(resp);
        // Increment the like count displayed on the page
        const likesCount = document.getElementById(`likes-count-${post_id}`);
        likesCount.textContent = parseInt(likesCount.textContent) + 1;
    })
    .catch(error => console.error('Error:', error));
}

// function addComment(post_id) {
//     const commentInput = document.getElementById(`comment-input-${post_id}`);
//     const comment = commentInput.value.trim();
//     if (comment !== '') {
//         fetch(`/comment/${post_id}`, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({ comment })
//         })
//         .then(() => {
//             // Clear the comment input field
//             commentInput.value = '';
//             // Reload posts to display new comment
//             getPosts();
//         })
//         .catch(error => console.error('Error:', error));
//     }
// }

function fetchResults() {


// postForm.addEventListener('submit', (evt) => {
    // evt.preventDefault();
    // const formInputs = {
    //     post_id: document.querySelector('#post_id').value
    // }

    fetch('/post-results.json', {
        method: 'GET'
    })
    .then((response) => response.json())
    .then((results) => {
        //select the empty div, save it in a variable
        post_results = document.querySelector('#post-results')
        //for loop over results
        for (const post of results) {
            // console.log(post)
            post_results.insertAdjacentHTML('beforeend', 
            `<div>
                <h3>${post.avatar}@${post.username}</h3>
                <p>${post.content}</p>
                <button onclick="likePost(${post.post_id})">Like</button>
                <span><span id="likes-count-${post.post_id}">${post.likes}</span></span>
            </div>`)
        }
            //insert some html using the result

        console.log(results);
    });
    
}

