async function quickLoginVerification(enteredUsername, enteredPassword) {
    let dataLoginPairs = [];

    try{
        const response = await fetch("login.json");
        if(!response.ok) throw new Error("Could not fetch resource");
        dataLoginPairs = await response.json();
    }
    catch(error){
        console.error(error);
    }

    const loginValidated = dataLoginPairs.some(dataLoginPair => ((enteredUsername === dataLoginPair.username) && (enteredPassword === dataLoginPair.password)));
    if(loginValidated){
        window.location = "../UserHome/user_home.html";
    }
    else{
        const loginErrorMessage = document.getElementById("loginErrorMessage");
        loginErrorMessage.innerHTML = "Incorrect username or password.";
        loginErrorMessage.classList.replace("hidden-error", "shown-error");
        document.getElementById("passwordInput").value = "";
    }
}

document.getElementById("loginForm").addEventListener("submit", event => {
    event.preventDefault(); //MAYBE MOVE AROUND, send form data to next page
    const enteredUsername = document.getElementById("usernameInput").value;
    const enteredPassword = document.getElementById("passwordInput").value;
    quickLoginVerification(enteredUsername, enteredPassword);
});

// Prevent invalid input (emojis, UNICODE)
document.querySelectorAll("input").forEach(inputBox => {
    inputBox.dataset.previousInput = "";
    inputBox.addEventListener("input", event => {
        const currentInput = event.target.value;
        const allowedCharsRegex = /^[ A-Za-z0-9!#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~\"]*$/;
    
        if(allowedCharsRegex.test(currentInput)) {
            event.target.dataset.previousInput = currentInput;
        } 
        else {
            event.target.value = event.target.dataset.previousInput;
        }
    });
});