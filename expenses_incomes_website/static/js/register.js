const usernameField = document.querySelector('#usernameFeild');
const feedBackUserNameArea = document.querySelector('.errorMsg_username');

usernameField.addEventListener("keyup", (e) => {

    usernameField.classList.remove("is-invalid");
    feedBackUserNameArea.style.display = 'none';
    const usernameVal = e.target.value;

    if (usernameVal.length > 0) {
        fetch('/authentication/validate-username', {
            body: JSON.stringify({
                'username': usernameVal
            }),
            method: "POST",
        }).then(res => res.json()).then(data => {
            if (data.username_error){
                usernameField.classList.add("is-invalid");
                feedBackUserNameArea.style.display = 'block'
                feedBackUserNameArea.innerHTML = `<p>${data.username_error}</p>`
            }
        });
    }

})