

// Expose node variables to frontend script via ipcRenderer, ipcHandle bridge

const info = document.getElementById('info')
info.innerText = `This app is using Chrome (v${versions.chrome()}), Node.js (v${versions.node()}), and Electron (v${versions.electron()})`


// Test bridge w. ping

const testPing = async () => {
    const response = await window.electronMessagingAPI.ping()
    console.log(response)
}
testPing()

// Send message from renderer to main process
window.electronMessagingAPI.sendMain('Hi')  // Use response channel to send a value

// Recieve message from main process to renderer
const receiveMsg = async () => {
    const msg = await window.electronMessagingAPI.receiveMain()
    console.log(msg)
}
receiveMsg()


// Load File

const fileButton = document.getElementById('file-btn')
const filePathElement = document.getElementById('filePath')

fileButton.addEventListener('click', async () => {
    const filePath = await window.electronAPI.openFile()  // Use electron dialog to show options, returns selected path 
    filePathElement.innerText = filePath
})

