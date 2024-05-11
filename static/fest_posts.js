
function likePost(festpost_id) {
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
            festlikesCount.textContent = parseInt(likesCount.textContent) + 1;
        } else if (resp['added'] == 'Unliked') {
            festlikesCount.textContent = parseInt(likesCount.textContent) - 1;
        }
    })
    .catch(error => console.error('Error:', error));
}


setTimeout(fetchResults, 500)


function fetchResults() {

    let festId = document.querySelector('#hidden-fest-id').value;
    console.log(festId);

    fetch(`/festpost-results.json/${festId}`, {
        method: 'GET'
    })
    .then((response) => response.json())
    .then((results) => {
        //select the empty div, save it in a variable
        festpost_results = document.querySelector('#festpost-results')
        //for loop over results
        console.log(results)
        for (const festpost of results) {
            // console.log(festpost)
            festpost_results.insertAdjacentHTML('beforeend', 
            `
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
            `)
        }

        console.log(results);
    });
    
}