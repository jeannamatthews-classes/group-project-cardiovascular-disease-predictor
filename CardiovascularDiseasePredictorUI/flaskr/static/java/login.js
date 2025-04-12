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