import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Balázs Szalai"
email["to"] = "szal.balazs@gmail.com"
email["subject "] = "Very important email!"

email.set_content("The important message.")

with smtplib.STMP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("randomemail@gmail.com", "1234ASD")
    smtp.send_messega(email)
    print("Done!")
