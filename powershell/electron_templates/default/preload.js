const { contextBridge, ipcRenderer } = require('electron')

// Expose node variables to frontend script
contextBridge.exposeInMainWorld('versions', {
    node: () => process.versions.node,
    chrome: () => process.versions.chrome,
    electron: () => process.versions.electron,
})

contextBridge.exposeInMainWorld('electronMessagingAPI', {
    ping: () => ipcRenderer.invoke('ping'),
    sendMain: (value) => ipcRenderer.send('from-render', value),
    receiveMain: () => ipcRenderer.invoke('to-render'),
})

contextBridge.exposeInMainWorld('electronAPI', {
    openFile: () => ipcRenderer.invoke('dialog:openFile'),
    setTitle: (title) => ipcRenderer.send('set-title', title),
    closeWindow: () => ipcRenderer.invoke('main:close-window'),
    toggleFullscreen: () => ipcRenderer.invoke('main:fullscreen-window'),
    minimizeWindow: () => ipcRenderer.invoke('main:minimize-window'),
})
// We wrap in ipcRenderer.invoke in a helper funcion rather than expose the ipcRenderer module directly to the context bridge

// to attach to renderer, pass path to WebPreferences.preload in BrowserWindow constructor
