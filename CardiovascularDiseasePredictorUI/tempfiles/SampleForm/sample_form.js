// Prevent invalid input
function limitToIntegerInput(inputBox) {
    const currentInput = inputBox.value;
    const allowedCharsRegex = /^[0-9]*$/;

    if(allowedCharsRegex.test(currentInput)) {
        inputBox.dataset.previousInput = currentInput;
    } 
    else {
        inputBox.value = inputBox.dataset.previousInput;
    }
}

function limitToNumericalInput(inputBox) {
    const currentInput = inputBox.value;
    const allowedCharsRegex = /^[0-9-.]*$/;

    if(allowedCharsRegex.test(currentInput)) {
        inputBox.dataset.previousInput = currentInput;
    } 
    else {
        inputBox.value = inputBox.dataset.previousInput;
    }
}

// Verify input
function verifyNumericalInput(inputBox, min, max) {    
    // Reset the error state  
    const inputErrorMessage = inputBox.parentElement.nextElementSibling;
    
    inputErrorMessage.innerHTML = "";
    inputErrorMessage.classList.replace("shown-error", "hidden-error");
    inputBox.classList.remove("invalidEntry");
    updateNavigationButtons();
    
    const inputAge = inputBox.value;
    if(inputAge === "") {
        inputErrorMessage.innerHTML = `Fill out field to continue.`;
        inputErrorMessage.classList.replace("hidden-error", "shown-error");
        inputBox.classList.add("invalidEntry");
        nextInputsButton.classList.replace("enabled", "disabled");
        prevInputsButton.classList.replace("enabled", "disabled");
    }
    else if(isNaN(Number(inputAge)) || (Number(inputAge) < min) || (Number(inputAge) > max)) {
        inputErrorMessage.innerHTML = `Value must be in the range ${min} to ${max}.`;
        inputErrorMessage.classList.replace("hidden-error", "shown-error");
        inputBox.classList.add("invalidEntry");
        nextInputsButton.classList.replace("enabled", "disabled");
        prevInputsButton.classList.replace("enabled", "disabled");
    }
}

// Set invalid input and verify input for ageInput
document.getElementById("ageInput").dataset.previousInput = "";
document.getElementById("ageInput").addEventListener("input", event => limitToIntegerInput(event.target));
document.getElementById("ageInput").addEventListener("change", event => verifyNumericalInput(event.target, 0, 120));

document.getElementById("testInput1").addEventListener("change", event => verifyNumericalInput(event.target, 0, 120));
document.getElementById("testInput2").addEventListener("change", event => verifyNumericalInput(event.target, 0, 120));
document.getElementById("testInput3").addEventListener("change", event => verifyNumericalInput(event.target, 0, 120));
document.getElementById("testInput4").addEventListener("change", event => verifyNumericalInput(event.target, 0, 120));
document.getElementById("testInput5").addEventListener("change", event => verifyNumericalInput(event.target, 0, 120));

document.getElementById("testInput6").addEventListener("change", event => verifyNumericalInput(event.target, 0, 120));
document.getElementById("testInput7").addEventListener("change", event => verifyNumericalInput(event.target, 0, 120));
document.getElementById("testInput8").addEventListener("change", event => verifyNumericalInput(event.target, 0, 120));
document.getElementById("testInput9").addEventListener("change", event => verifyNumericalInput(event.target, 0, 120));
document.getElementById("testInput10").addEventListener("change", event => verifyNumericalInput(event.target, 0, 120));


// Verify input for selection dropdowns
document.querySelectorAll("select").forEach(selectDropdown => {
    selectDropdown.addEventListener("change", event => {
        const selectErrorMessage = selectDropdown.parentElement.nextElementSibling;    
        selectErrorMessage.classList.replace("shown-error", "hidden-error");
        selectDropdown.classList.remove("invalidEntry");
        updateNavigationButtons();

        if(selectDropdown.value === "") {
            selectErrorMessage.classList.replace("hidden-error", "shown-error");
            selectDropdown.classList.add("invalidEntry");
            nextInputsButton.classList.replace("enabled", "disabled");
            prevInputsButton.classList.replace("enabled", "disabled");
        }
    })
})


// Adjust visibility of inputs
const inputNodeList = document.querySelectorAll("div.inputRowDiv");
const TOTAL_PAGES = 3;
let inputPage = 1;
document.getElementById("navigateP").innerHTML = `${inputPage}/${TOTAL_PAGES}`;

function updateNavigationButtons() {
    if(document.querySelectorAll(".shown-error").length === 0) {
        nextInputsButton.classList.replace("disabled", "enabled");
        prevInputsButton.classList.replace("disabled", "enabled");    
    }
    if(inputPage === TOTAL_PAGES) {
        nextInputsButton.classList.replace("enabled", "disabled");
    }
    if(inputPage === 1 && (document.querySelectorAll(".shown-error").length === 0)) {
        prevInputsButton.classList.replace("enabled", "disabled");
    }
}

function prevInputs() {
    const prevInputsButton = document.getElementById("prevInputsButton");
    if(prevInputsButton.classList.contains("disabled")) {
        return;
    }

    const nextInputsButton = document.getElementById("nextInputsButton");
    prevInputsButton.classList.replace("disabled", "enabled");
    nextInputsButton.classList.replace("disabled", "enabled");

    const startIndex = (-1 + inputPage) * 5;
    for(let i = startIndex; i <= startIndex + 4; i++) {
        inputNodeList[i].classList.replace("shown", "hidden");
        inputNodeList[i-5].classList.replace("hidden", "shown");
    }

    if(inputPage === TOTAL_PAGES) {
        document.querySelector(".submit").classList.replace("enabled", "disabled");
    }

    if(inputPage !== 1) {
        inputPage--;
    }
    document.getElementById("navigateP").innerHTML = `${inputPage}/${TOTAL_PAGES}`;

    if(inputPage === 1) {
        prevInputsButton.classList.replace("enabled", "disabled");
    }
}

async function nextInputs() {
    const nextInputsButton = document.getElementById("nextInputsButton");
    if(nextInputsButton.classList.contains("disabled")) {
        return;
    }

    const startIndex = (-1 + inputPage) * 5;
    for(let i = startIndex; i <= startIndex + 4; i++) {
        const changeEvent = new Event('change');
        inputNodeList[i].childNodes[3].dispatchEvent(changeEvent);
    }
    if(document.querySelectorAll(".shown-error").length > 0) {
        return;
    }

    const prevInputsButton = document.getElementById("prevInputsButton");
    prevInputsButton.classList.replace("disabled", "enabled");
    nextInputsButton.classList.replace("disabled", "enabled");

    for(let i = startIndex; i <= startIndex + 4; i++) {        
        inputNodeList[i].classList.replace("shown", "hidden");
        inputNodeList[i+5].classList.replace("hidden", "shown");
    }

    if(inputPage !== TOTAL_PAGES) {
        inputPage++;
    }
    document.getElementById("navigateP").innerHTML = `${inputPage}/${TOTAL_PAGES}`;

    if(inputPage === TOTAL_PAGES) {
        nextInputsButton.classList.replace("enabled", "disabled");
        document.querySelector(".submit").classList.replace("disabled", "enabled");
    }
}

// Submit the Form
document.getElementById("sampleForm").addEventListener("submit", event => {
    if(document.querySelector("button.submit").classList.contains("disabled")) {
        event.preventDefault();
        return;
    }

    const startIndex = (-1 + inputPage) * 5;
    for(let i = startIndex; i <= startIndex + 4; i++) {
        const changeEvent = new Event('change');
        inputNodeList[i].childNodes[3].dispatchEvent(changeEvent);
    }
    if(document.querySelectorAll(".shown-error").length > 0) {
        event.preventDefault();
        return;
    }

    //otherwise, the form submits
});



//FOR TESTING PURPOSES
/*
document.getElementById("ageInput").value = 15;
document.getElementById("genderInput").value = 0;
document.getElementById("smokingInput").value = 1;
document.getElementById("alcoholInput").value = 1;
document.getElementById("priorCMPInput").value = 1;

document.getElementById("testInput1").value = 1;
document.getElementById("testInput2").value = 1;
document.getElementById("testInput3").value = 1;
document.getElementById("testInput4").value = 1;
document.getElementById("testInput5").value = 1;
*/