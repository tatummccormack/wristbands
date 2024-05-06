let body = document.body;
const followButtons = document.querySelectorAll('.follow-button')


followButtons.forEach(btn => {
    btn.addEventListener('click', e => followUnFollow(e.target))
})

function followUnFollow(button) {
    button.classList.toggle("followed");
    if (button.innerText == "Follow") button.innerText = "Unfollow";
    else button.innerText = "Follow"
}

