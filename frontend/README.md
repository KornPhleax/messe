# ITS Projekt zur Plannung und Umsetzung eines Messeauftritts

##  Aufbau

*Hauptseite*
index.html
index.js - Electron app
form.js
form.css

*Bestätigungsseite*
danke.html
danke.css

*Login Seite*
login.html
login.css
login.js

*Mitarbeiter Seite*
table.html
table.css
table.js

## Funktionsweise

Die Electron Bibliothek erstellt ein Chromium Fenster und lädt darin die Index.html

Sobald man auf Senden clickt, wird ein API-request gemacht. Bei Einem erfolgreichen POST, wird man zur Bestätigungsseite geleitet.

Über den Login Button gelangt man zur login.html

Der Login-API-request wird gepürft. Wenn dieser erfolgreich war, wird man zur Mitarbeiterseite geleitet.
Hier wird erneut ein API-request gemacht, der alle Kundendaten abfrägt. Die Daten werden dann in einer Tabelle angezeigt.

Über den Logout Button wird auch ein API-request gemacht. Wenn dieser erfolgreich war, wird man wieder zur Startseite geleitet.


## Development 

Um die Elecetron App zu entwicklen, wird folgendes benötigt:

- NPM
- NodeJS
- node-fetch
- Electron Bibliothek

Klone das Repository und gehe in den Ordner „frontend“. 
NPM und NodeJS sollten bereits installiert sein. 
Danach installiere Electron und Abhängigkeiten mit „npm install“.
Jetzt muss lediglich das Frontend mit „npm start“ gestartet werden, und die App öffnet sich.








