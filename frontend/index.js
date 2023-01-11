const { app, BrowserWindow } = require('electron');

// Erstelle neue Electron APP

function createWindow () {
  const window = new BrowserWindow({

    width: 1920,
    height: 1080,
    titleBarStyle: 'hidden',
    autoHideMenuBar: "true",

    webPreferences: {
      nodeIntegration: true
    }

  });
  // Lade Hauptseite
  window.loadFile('index.html');

}
app.whenReady().then(createWindow);
