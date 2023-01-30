const userNameField = document.querySelector('#usernameFeild');
const userNameFeedBackArea = document.querySelector('.errorMsg_username');

userNameField.addEventListener("keyup", (e) => {

    userNameField.classList.remove("is-invalid");
    userNameFeedBackArea.style.display = 'none';
    const usernameVal = e.target.value;

    if (usernameVal.length > 0) {
        fetch('/authentication/validate-username', {
            body: JSON.stringify({
                'username': usernameVal
            }),
            method: "POST",
        }).then(res => res.json()).then(data => {
            if (data.username_error) {
                userNameField.classList.add("is-invalid");
                userNameFeedBackArea.style.display = 'block'
                userNameFeedBackArea.innerHTML = `<p>${data.username_error}</p>`
            }
        });
    }

});

const emailField = document.querySelector('#emailFeild');
const emailFeedBackArea = document.querySelector('.errorMsg_email');

emailField.addEventListener("keyup", (e) => {

    emailField.classList.remove("is-invalid");
    emailFeedBackArea.style.display = 'none';
    const emailVal = e.target.value;

    if (emailVal.length > 0) {
        fetch('/authentication/validate-email', {
            body: JSON.stringify({
                'email': emailVal
            }),
            method: "POST",
        }).then(res => res.json()).then(data => {
            if (data.email_error) {
                emailField.classList.add("is-invalid");
                emailFeedBackArea.style.display = 'block'
                emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`
            }
        });
    }

});