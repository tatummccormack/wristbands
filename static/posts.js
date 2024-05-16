
// let postForm = document.querySelector('#post-form');


setTimeout(fetchResults, 500)


function likePost(post_id) {
    // still listening for the onclick
    // check if <i> with class of SOMETHING hasClass('bx bx-heart')
        // then remove the bx bx-heart, addClass bx bxs-heart
    // else if <i> has bx bxs-heart
        // then remove bx bxs-heart, addClass bx bx-heart


    fetch(`/like/${post_id}`, { method: 'POST' })
    .then((response) => response.json())
    .then((resp) => {
        // toggle heart icon file
        let heartIcon = document.querySelector(`#heart-${post_id}`); // icon in the dom
        if (heartIcon.classList.contains('bx-heart')) {
            heartIcon.classList.remove('bx-heart');
            heartIcon.classList.add('bxs-heart');
        } else if (heartIcon.classList.contains('bxs-heart')) {
            heartIcon.classList.remove('bxs-heart');
            heartIcon.classList.add('bx-heart');
        }
        // Increment or decrement the like count displayed on the page
        const likesCount = document.getElementById(`likes-count-${post_id}`);
        if (resp['added'] == 'Success!') {
            likesCount.textContent = parseInt(likesCount.textContent) + 1;
        } else if (resp['added'] == 'Unliked') {
            likesCount.textContent = parseInt(likesCount.textContent) - 1;
        }
    })
    .catch(error => console.error('Error:', error));
}


function fetchResults() {
    fetch('/post-results.json', {
        method: 'GET'
    })
    .then((response) => response.json())
    .then((results) => {
        //select the empty div, save it in a variable
        const postResultsContainer = document.querySelector('#post-results');
        
        // Clear existing posts before appending new ones
        postResultsContainer.innerHTML = '';
        // Loop over each post in the results array
        results.forEach(post => {
            // Create HTML elements for each post
            const postElement = document.createElement('div');
            // postElement.classList.add('post');
            postElement.innerHTML = `
                <div class="post-container">
                    <div class="content">

                        <div class="post-avatar"> <img src=${post.avatar}> </div>
                        <div class="username">@${post.username}</div>
                        <p>${post.content}</p>

                        <div class="iconbx">
                            <div class"commentbtn"><i class='bx bx-message-dots bx-flip-horizontal'></i></div>
                            <div class"sharebtn"><i class='bx bx-share'></i></div>
                            <button class="heartbtn" onclick="likePost(${post.post_id})"><i class='bx bx-heart' id="heart-${post.post_id}"></i>
                            <span><span id="likes-count-${post.post_id}"> ${post.like_count} </span></span></button>
                        </div>

                    </div>
                </div>
            `;
            // Append the post element to the container
            postResultsContainer.appendChild(postElement);
        });
    })
    .catch(error => console.error('Error:', error));

}
