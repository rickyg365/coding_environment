// This script controls the main process, 
// runs in a Node.js environment 
// responsible for controlling 
// - your app's lifecycle, 
// - displaying native interfaces, 
// - performing privileged operations 
// - managing renderer processes (more on that later).This script controls the main process, which runs in a Node.js environment and is responsible for controlling your app's lifecycle, displaying native interfaces, performing privileged operations, and managing renderer processes (more on that later).

const { app, BrowserWindow, dialog, ipcMain, Menu, desktopCapturer } = require('electron')
const path = require('node:path')
const { title, electron } = require('node:process')
// require("electron-reload")(__dirname)  // Needs electron-reload install


// Helper Functions
function getEventWindow(e) {
    const webContents = e.sender;
    const newWindow = BrowserWindow.fromWebContents(webContents);
    
    return newWindow
}

// App Functions
function handleSetTitle(event, title) {
    const win = getEventWindow(event)  // Get window that triggered event
    win.setTitle(title)  // Sets title on browser window
}

// System Functions
async function handleFileOpen() {
    const { canceled, filePaths } = await dialog.showOpenDialog({})
    if (!canceled) {
        return filePaths[0]
    }
}

// Title Bar Actions
function closeWindow(event) {
    const win = getEventWindow(event);
    win.close()
}

function fullscreenWindow(event) {
    const win = getEventWindow(event);
    win.setFullScreen(!win.isFullScreen())
}

function minimizeWindow(event) {
    const win = getEventWindow(event);
    
    if (!win.isMinimized()) {
        win.minimize()
    }
}


const createWindow = () => {
    const window = new BrowserWindow({
        width: 800,
        height: 600,
        frame: false,  // Hide frame
        autoHideMenuBar: false, // hides menu bar and finder on max
        webPreferences: {
            // contextIsolation: false,
            // nodeIntegration: true,  // Lets us use node directly
            preload: path.join(__dirname, 'preload.js')  // __dirname points to path of currently executing script
        },
        // expose window controlls in Windows/Linux
        ...(process.platform !== 'darwin' ? { titleBarOverlay: true } : {}),
    })

    window.loadFile(__dirname + '/index.html')
}

// Start App
app.whenReady().then(() => {
    // Main
    ipcMain.handle('main:close-window', closeWindow)
    ipcMain.handle('main:fullscreen-window', fullscreenWindow)
    ipcMain.handle('main:minimize-window', minimizeWindow)
    
    ipcMain.on('set-title', handleSetTitle)
    
    // System Access
    ipcMain.handle('dialog:openFile', handleFileOpen)
    
    // IPC
    ipcMain.handle('ping', () => 'pong')
    
    ipcMain.on('from-render', (_event, value) => {
        console.log(value)
    })
    ipcMain.handle('to-render', (_event) => {
        console.log(_event)
        return "This message was sent from the main process!"
    })

    // Open Main Window
    createWindow()

    // Open window if none are created (Mac)
    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow()
    })
})


// Exit Windows & Linux
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit()
})
