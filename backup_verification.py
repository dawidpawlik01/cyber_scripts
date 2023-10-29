#dpawlik

import os
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Ustawienia ścieżki do katalogu i wzorca nazwy pliku
katalog = "/ścieżka/do/katalogu"  
wzorzec_nazwy_pliku = "nazwa_pliku*.txt"  

# Ustawienia e-mail
adres_nadawcy = "#"
haslo_nadawcy = "#"
adres_odbiorcy = "#"

# aktualną datę i godzinę
aktualna_data_godzina = datetime.datetime.now()

# godzina weryfikacji 
godzina_weryfikacji = datetime.time(7, 0)


if aktualna_data_godzina.time() == godzina_weryfikacji:
   
    pliki = [f for f in os.listdir(katalog) if f.startswith(wzorzec_nazwy_pliku)]
    if not pliki:
        
        subject = "Brak pliku o wzorcu nazwy w katalogu"
        message = "Nie znaleziono pliku o wzorcu nazwy '{}' w katalogu: {}".format(wzorzec_nazwy_pliku, katalog)

        # Konfiguracja serwera SMTP
        smtp_server = "#"  
        smtp_port = #

        # Logowanie do serwera SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(adres_nadawcy, haslo_nadawcy)

        # Tworzenie wiadomości e-mail
        msg = MIMEMultipart()
        msg["From"] = adres_nadawcy
        msg["To"] = adres_odbiorcy
        msg["Subject"] = subject

        
        msg.attach(MIMEText(message, "plain"))
 
        server.sendmail(adres_nadawcy, adres_odbiorcy, msg.as_string())

        # Zamykanie połączenia z serwerem SMTP
        server.quit()

        print("E-mail wysłany: Brak pliku w katalogu")
    else:
        print("Plik(y) znaleziono: {}".format(pliki))
else:
    print("Aktualna data i godzina nie odpowiadają godzinie weryfikacji ({}).".format(godzina_weryfikacji))
