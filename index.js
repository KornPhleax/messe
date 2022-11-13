const { app, BrowserWindow } = require('electron');

function createWindow () {
  const window = new BrowserWindow({

    width: 1920,
    height: 1080,

    webPreferences: {
      nodeIntegration: true
    }

  });

  window.loadFile('index.html');

}

app.whenReady().then(createWindow);
