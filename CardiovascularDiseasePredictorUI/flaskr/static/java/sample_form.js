// Submit the Form
document.getElementById("sampleForm").addEventListener("submit", event => {
    // files.length returns 0 when no file is present
    if(!document.getElementById('fileInput').files.length) {
        event.preventDefault();
        fileInputErrorMessage.innerHTML = "A file must be selected.";
        fileInputErrorMessage.classList.replace("hidden-error", "shown-error");
        return;
    }
});

// Update File Input Label
document.getElementById("fileInput").addEventListener("change", event => {
    selectFileLabel = document.getElementById("selectFileLabel");
    
    const file = event.target.files[0];
    if(file) {
        let fileName = file.name;
        if(fileName.length > 10) fileName = fileName.substr(0, 4) + "....csv";
        selectFileLabel.innerHTML = fileName;
    }
});
