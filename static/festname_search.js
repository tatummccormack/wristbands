// let festForm = document.querySelector('#fest-form');

// festForm.addEventListener('submit', (evt) => {
//     evt.preventDefault();
//     const formInputs = {
//         fest_name: document.querySelector('#fest_name').value
//     }

//     fetch('/fest-results.json', {
//         method: 'POST',
//         body: JSON.stringify(formInputs),
//         headers: {
//                 'Content-Type': 'application/json',
//                 },
// })

//     .then((response) => response.json())
//     .then((results) => {
//         //select the empty div, save it in a variable
//         fest_results = document.querySelector('#fest-results')
//         //for loop over results
//         for (const fest of results) {
//             fest_results.insertAdjacentHTML('beforeend', `<div><h2>${fest.fest_name}</h2></div>`)
//         }
//             //insert some html using the result

//         console.log(fest_results)
//     });

// });


// festForm.addEventListener('submit', (evt) => {
//     evt.preventDefault();
//     const formInputs = {
//         fest_name: document.querySelector('#fest_name').value
//     }

//     fetch('/fest-results.json', {
//         method: 'POST',
//         body: JSON.stringify(formInputs),
//         headers: {
//             'Content-Type': 'application/json',
//         },
//     })
//     .then((response) => response.json())
//     .then((results) => {
//         // Select the fest-table and save it in a variable
//         const festTable = document.querySelector('.fest-table');
        
//         // Clear previous search results
//         festTable.innerHTML = '';
        
//         // Loop over search results
//         for (const fest of results) {
//             // Create a div element for each festival
//             const festRow = document.createElement('div');
//             festRow.classList.add('fest-row');
            
//             const festCell = document.createElement('div');
//             festCell.classList.add('fest-cell');
//             festCell.innerHTML = `<a href="/festivals/${fest.fest_id}">${fest.fest_name}</a>`;
            
//             // Append the festCell to the festRow
//             festRow.appendChild(festCell);
            
//             // Append the festRow to the festTable
//             festTable.appendChild(festRow);
//         }
//     });
// });