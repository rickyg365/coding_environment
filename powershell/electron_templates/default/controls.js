
// Title Bar Controls Setup

let minimize_btn = document.getElementById('minimize-btn');
let fullscreen_btn = document.getElementById('fullscreen-btn');
let close_btn = document.getElementById('close-btn');

minimize_btn.addEventListener('click', () => {
    window.electronAPI.minimizeWindow()
})

fullscreen_btn.addEventListener('click', () => {
    window.electronAPI.toggleFullscreen()
})

close_btn.addEventListener('click', () => {
    window.electronAPI.closeWindow();
})


// Change Title Controls

const titleElement = document.getElementById('title')
const titleInput = document.getElementById('title-input')
const setButton = document.getElementById('btn')

function updateTitle() {
    const title = titleInput.value
    window.electronAPI.setTitle(title)  // Set title for window/app
    titleElement.innerText = title  // Updates frontend w. new title
}

// Submit via button
setButton.addEventListener('click', updateTitle)

// Submit via [ Enter ] key
titleInput.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        // event.preventDefault();
        updateTitle();
        titleInput.value = ''  // Reset input Value
    }
});
