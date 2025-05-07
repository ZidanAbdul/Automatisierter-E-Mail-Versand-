# Automatisierter-E-Mail-Versand-

Dieses Python-Skript sendet personalisierte Bewerbungen per E-Mail an eine Liste von Firmen, die in einer Excel-Datei gespeichert sind. Es verwendet smtplib zur Verbindung mit einem SMTP-Server (z. B. Gmail) und fügt ein PDF-Dokument als Anhang hinzu.

🔧 Voraussetzungen

Python 3.x

Paketinstallationen:

pip install pandas openpyxl

Benötigte Dateien

Excel-Datei: firmen_erweitert_1 (1).xlsxMuss folgende Spalten enthalten:

Name – Firmenname

E-Mail – Zieladresse

Anrede – z. B. "Herr" oder "Frau"

Ansprechpartner – Name der Ansprechperson

PDF-Datei: Dein BewerbungsanhangStelle sicher, dass du den Dateipfad in der Variable anhang_pfad korrekt angibst, z. B.:

anhang_pfad = "Bewerbung_Max_Mustermann.pdf"

Gmail-Versand einrichten

Aktiviere Zwei-Faktor-Authentifizierung in deinem Gmail-Konto.

Erstelle ein App-Passwort

Trage E-Mail und App-Passwort ins Skript ein:

EMAIL = "deine.email@gmail.com"
PASSWORT = "dein_app_passwort"

Ausführen

Führe das Skript aus:

python bewerbung_senden.py

Das Skript:

Liest die Excel-Datei ein

Erstellt personalisierte E-Mails (Anrede & Betreff)

Hängt das PDF an

Sendet die Nachricht an jede Firma

Gibt Rückmeldung über Erfolg oder Fehler

Sicherheitshinweis

Poste niemals dein Passwort oder App-Passwort öffentlich!Erwäge, sensible Daten in einer .env-Datei zu speichern und mit dotenv zu laden.

Noch zu beachten

Stelle sicher, dass dein Gmail-Konto den Versand über SMTP erlaubt.

Die Betreffzeile und Inhalte kannst du anpassen, z. B. für verschiedene Bewerbungen.

Teste zuerst mit deiner eigenen E-Mail-Adresse, bevor du alle Mails versendest.

