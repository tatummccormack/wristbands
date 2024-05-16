const searchInput = document.getElementById('fest_name');
const resultBox = document.querySelector('.result-box');

searchInput.addEventListener('input', function() {
    const query = this.value.trim(); // Get the current search query
    
    if (query.length < 3) {
        // Clear the result box and hide it if the search query is less than 3 characters
        resultBox.innerHTML = '';
        resultBox.style.display = 'none';
        return;
    }
    
    // Make an AJAX request to the server with the search query
    fetch(`/autocomplete?query=${query}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error fetching autocomplete suggestions');
            }
            return response.json();
        })
        .then(results => {
            // Clear previous autocomplete suggestions
            resultBox.innerHTML = '';
            
            if (results.length === 0) {
                // If no results are found, display a message
                resultBox.innerHTML = '<p>No results found</p>';
            } else {
                // Create a <ul> list for autocomplete suggestions
                const ul = document.createElement('ul');
                
                // Display the new autocomplete suggestions in the result box
                results.forEach(result => {

                    const link = document.createElement('a');
                    link.href = `/festivals/${result.id}`; // Link to festival page
                    link.textContent = result.name;
                    
                    const li = document.createElement('li');
                    li.appendChild(link);
                    ul.appendChild(li);
                });
                
                // Append the <ul> list to the result box
                resultBox.appendChild(ul);
            }
            
            // Show the result box
            resultBox.style.display = 'block';
        })
        .catch(error => {
            console.error('Error fetching autocomplete suggestions:', error);
        });
});




