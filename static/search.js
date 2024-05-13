// let searchForm = document.querySelector('#search-form');

// searchForm.addEventListener('submit', (evt) => {
//     evt.preventDefault();
//     const formInputs = {
//         fest_location: document.querySelector('#fest_location').value
//     }

//     fetch('/search-results.json', {
//         method: 'POST',
//         body: JSON.stringify(formInputs),
//         headers: {
//                 'Content-Type': 'application/json',
//                 },
// })

//     .then((response) => response.json())
//     .then((results) => {
//         //select the empty div, save it in a variable
//         search_results = document.querySelector('#search-results')
//         //for loop over results
//         for (const fest of results) {
//             search_results.insertAdjacentHTML('beforeend', `<div><h2>${fest.fest_name}</h2></div>`)
//         }
//             //insert some html using the result

//         console.log(results)
//     });
    
// });

