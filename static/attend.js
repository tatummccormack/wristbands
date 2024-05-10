let body = document.body;
const attendButtons = document.querySelectorAll('.attending-button')

attendButtons.forEach(btn => {
    btn.addEventListener('click', e => attendUnattend(e.target))
})

function attendUnattend(button) {
    const festId = document.getElementById('hidden-fest-id').value;
    const isAttending = button.classList.contains('attending');
    
    fetch(`/attend-festival/${festId}`, {
        method: isAttending ? 'DELETE' : 'POST', // Use DELETE method to unattend
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (response.ok) {
            button.classList.toggle("attending");
            button.innerText = isAttending ? "Attend" : "Attending";
            
        } else {
            throw new Error('Failed to attend/unattend festival');
        }
    })
    .catch(error => console.error('Error attending/unattending festival:', error));
}
