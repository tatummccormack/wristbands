let festForm = document.querySelector('#fest-form');

festForm.addEventListener('submit', (evt) => {
    evt.preventDefault();
    const formInputs = {
        fest_name: document.querySelector('#fest_name').value
    }

    fetch('/fest-results.json', {
        method: 'POST',
        body: JSON.stringify(formInputs),
        headers: {
                'Content-Type': 'application/json',
                },
})

    .then((response) => response.json())
    .then((results) => {
        //select the empty div, save it in a variable
        fest_results = document.querySelector('#fest-results')
        //for loop over results
        for (const fest of results) {
            fest_results.insertAdjacentHTML('beforeend', `<div><h2>${fest.fest_name}</h2></div>`)
        }
            //insert some html using the result

        console.log(fest_results)
    });

});