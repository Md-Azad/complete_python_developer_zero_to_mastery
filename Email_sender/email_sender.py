import smtplib

from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Md Azad Hossain'
email['to'] = 'azadh4110@gmail.com'
email['subject'] = ' leanring how to send email with python'

email.set_content('Azad you have to learn properly python.')

with smtplib.SMTP(host= 'smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mdazadh498@gmail.com','Hadiulbaba1')
    smtp.send_message(email)
    print('all good Azad')