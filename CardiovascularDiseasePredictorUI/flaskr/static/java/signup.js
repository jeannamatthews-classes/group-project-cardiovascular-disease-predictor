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


// Check password characters
validPassword = false;
validConfirmPassword = false;

document.getElementById("passwordInput").addEventListener("change", event => {
    const inputPasswordArray = Array.from(event.target.value);    
    const specialCharArray = Array.from(" !#$%&'()*+,-./:;<=>?@[\\]^_`{|}~\"");
    const passwordErrorMessage = document.getElementById("passwordErrorMessage");
    const LOWER_CHARS_REQUIRED = 1;
    const UPPER_CHARS_REQUIRED = 1;
    const NUMBER_CHARS_REQUIRED = 1;
    const SPECIAL_CHARS_REQUIRED = 1;
    const LENGTH_REQUIRED = 8;

    // Reset the Error State
    validPassword = false;
    passwordErrorMessage.innerHTML = "";
    passwordErrorMessage.classList.replace("shown-error", "hidden-error");
    event.target.classList.remove("invalidEntry");
    let lower = upper = num = special = 0;
    
    inputPasswordArray.forEach(char => {
        if(specialCharArray.some(specialChar => (char === specialChar))) {
            special++;
        }
        else if(!isNaN(Number(char))) {
            num++;
        }
        else if(char === char.toUpperCase()){
            upper++;
        }
        else if(char === char.toLowerCase()){
            lower++;
        }
    });

    // Compare password metrics to the requirements and update errorMessage
    let errorMessage = ``;
    let error = false;
    if(lower < LOWER_CHARS_REQUIRED){
        if(LOWER_CHARS_REQUIRED === 1) {
            errorMessage += `Password requires 1 lowercase character.<br />`;
        } 
        else if(LOWER_CHARS_REQUIRED > 1) {
            errorMessage += `Password requires ${LOWER_CHARS_REQUIRED} lowercase characters.<br />`;
        }
        error = true;
    }

    if(upper < UPPER_CHARS_REQUIRED){
        if(UPPER_CHARS_REQUIRED === 1) {
            errorMessage += `Password requires 1 uppercase character.<br />`;
        } 
        else if(UPPER_CHARS_REQUIRED > 1) {
            errorMessage += `Password requires ${UPPER_CHARS_REQUIRED} uppercase characters.<br />`;
        }
        error = true;
    }

    if(num < NUMBER_CHARS_REQUIRED){
        if(NUMBER_CHARS_REQUIRED === 1) {
            errorMessage += `Password requires 1 number.<br />`;
        } 
        else if(NUMBER_CHARS_REQUIRED > 1) {
            errorMessage += `Password requires ${NUMBER_CHARS_REQUIRED} numbers.<br />`;
        }
        error = true;
    }

    if(special < SPECIAL_CHARS_REQUIRED){
        if(SPECIAL_CHARS_REQUIRED === 1) {
            errorMessage += `Password requires 1 special character.<br />`;
        } 
        else if(SPECIAL_CHARS_REQUIRED > 1) {
            errorMessage += `Password requires ${NUMBER_CHARS_REQUIRED} special characters.<br />`;
        }
        error = true;
    }

    if(inputPasswordArray.length < LENGTH_REQUIRED){
        errorMessage += `Password must be ${LENGTH_REQUIRED} characters long.<br />`;
        error = true;
    }

    // Show the error message if present, or set validPassword = true;
    if(error){
        passwordErrorMessage.innerHTML = errorMessage;
        passwordErrorMessage.classList.replace("hidden-error", "shown-error");
        event.target.classList.add("invalidEntry");
    }   
    else{
        validPassword = true;
    }
});

function confirmPassword() {
    const confirmPasswordInputBox = document.getElementById("confirmPasswordInput");

    // Reset the error state
    validConfirmPassword = false;
    confirmPasswordErrorMessage.innerHTML = "";
    confirmPasswordErrorMessage.classList.replace("shown-error", "hidden-error");
    confirmPasswordInputBox.classList.remove("invalidEntry");
    
    const inputPassword = document.getElementById("passwordInput").value;
    const inputConfirmPassword = confirmPasswordInputBox.value;
    if(inputPassword !== inputConfirmPassword) {
        confirmPasswordErrorMessage.innerHTML = "Passwords must match.";
        confirmPasswordErrorMessage.classList.replace("hidden-error", "shown-error");
        confirmPasswordInputBox.classList.add("invalidEntry");
    }   
    else{
        validConfirmPassword = true;
    }
}

// Add event listeners
document.getElementById("passwordInput").addEventListener("change", confirmPassword);
document.getElementById("confirmPasswordInput").addEventListener("change", confirmPassword);


// Submit the form only if the input is valid 
document.getElementById("signupForm").addEventListener("submit", async event => {
    if(!validPassword || !validConfirmPassword){
        event.preventDefault();
        document.getElementById("passwordInput").value = "";
        document.getElementById("confirmPasswordInput").value = "";
    }
});