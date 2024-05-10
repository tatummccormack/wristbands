// document.addEventListener('DOMContentLoaded', () => {
//     loadProfile();
// });

// function loadProfile() {
//     fetch('/profile/') // syntax for user in session ??
//     .then(response => response.json())
//     .then(user => {
//         const bioContainer = document.getElementById('bio-container');
//         bioContainer.innerHTML = `<p>${user.bio}</p>`;
//         document.getElementById('bio-textarea').value = user.bio;
//     })
//     .catch(error => console.error('Error:', error));
// }

// function showEditForm() {
//     document.getElementById('edit-form-container').style.display = 'block';
// }

// function updateBio() {
//     const newBio = document.getElementById('bio-textarea').value;
//     fetch('/profile/', { // syntax for user in session ??
//         method: 'PUT',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ bio: newBio })
//     })
//     .then(response => {
//         if (response.ok) {
//             return response.json();
//         } else {
//             throw new Error('Failed to update bio');
//         }
//     })
//     .then(data => {
//         console.log(data);
//         loadProfile(); // Reload the profile to display the updated bio
//     })
//     .catch(error => console.error('Error:', error));
