// let postForm = document.querySelector('#fest-post-form');

// const myTimeout = setTimeout(fetchResults, 3000);

setTimeout(fetchResults, 3000)

function fetchResults() {


// postForm.addEventListener('submit', (evt) => {
//     evt.preventDefault();
//     const formInputs = {
//         post_id: document.querySelector('#post_id').value
//     }

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
            `<div class="fest-details">
                <div class="post-container">
                    <div class="username">@${festpost.username}</div>
                    ${festpost.content}
                </div>
            </div>`)
        }
            // <button onclick="likePost(${festId})">Like</button>
            // <span><span id="likes-count-${festId}">${festpost.likes}</span></span>
            
            // include in html the like functionality that's in the posts.js file
            //insert some html using the result

        console.log(results);
    });
    
}