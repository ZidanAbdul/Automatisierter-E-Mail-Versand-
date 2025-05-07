import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Deine Zugangsdaten (App-Passwort verwenden!)
EMAIL = "E.Mail"
PASSWORT = "passwort"  # Niemals öffentlich posten!
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

try:
    # Excel-Datei laden
    firmen = pd.read_excel('firmen_erweitert_1 (1).xlsx')
    print("Verfügbare Spalten:", firmen.columns.tolist())

    # Bewerbungsanhang
    anhang_pfad = ".pdf"#________________________

    # Verbindung zu Gmail-Server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL, PASSWORT)
    print("Erfolgreich mit Gmail verbunden.\n")

    # Firmen durchgehen
    for index, firma in firmen.iterrows():
        try:
            empfaenger = firma['E-Mail']
            if pd.isna(empfaenger):
                print(f"Keine E-Mail für {firma.get('Name', 'Unbekannt')} – übersprungen.")
                continue

            # Anrede & Name
            raw_anrede = str(firma['Anrede']).strip() if not pd.isna(firma['Anrede']) else ""
            ansprechpartner = str(firma['Ansprechpartner']).strip() if not pd.isna(firma['Ansprechpartner']) else ""
            firmenname = firma['Name']

            if raw_anrede.lower() == "herr":
                anrede_text = f"Sehr geehrter Herr {ansprechpartner}"
            elif raw_anrede.lower() == "frau":
                anrede_text = f"Sehr geehrte Frau {ansprechpartner}"
            else:
                anrede_text = "Sehr geehrte Damen und Herren"

            # E-Mail vorbereiten
            msg = MIMEMultipart()
            msg['From'] = EMAIL
            msg['To'] = empfaenger
            msg['Subject'] = f"um ein Praktikumplatz bei {firmenname} vom 22.Mai_18.Februar"

            inhalt = f"""
{anrede_text},

anbei übersende ich Ihnen meine vollständigen Bewerbungsunterlagen für die Position als Anwendungsentwickler in Ihrem Unternehmen für den Zeitraum von 22. Mai 2025 bis 18. Februar 2026.

Meine Unterlagen umfassen meinen Lebenslauf, ein Bewerbungsschreiben sowie die bisherigen Zeugnisse. Es wäre mir eine große Freude, Sie in einem persönlichen Gespräch von meiner Eignung zu überzeugen.

Für Ihre Zeit und die Berücksichtigung meiner Bewerbung danke ich Ihnen herzlich.

Mit freundlichen Grüßen  
Name

            msg.attach(MIMEText(inhalt, 'plain'))

            # Anhang hinzufügen
            with open(anhang_pfad, "rb") as anhang:
                part = MIMEApplication(anhang.read(), Name=".pdf")
                part['Content-Disposition'] = 'attachment; filename=".pdf"'#____________________________
                msg.attach(part)

            # E-Mail senden
            server.send_message(msg)
            print(f"E-Mail erfolgreich gesendet an: {empfaenger}")

        except Exception as e:
            print(f"Fehler bei {firma.get('E-Mail', 'Unbekannt')}: {str(e)}")
            continue

except Exception as e:
    print(f"Schwerwiegender Fehler: {str(e)}")

finally:
    if 'server' in locals():
        server.quit()
        print("\nVerbindung zum E-Mail-Server wurde beendet.")
