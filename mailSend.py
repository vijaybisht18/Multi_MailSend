import smtplib as sm

mail = sm.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('vijaybisht18122002@gmail.com','bnwysrpuofsjgcps')

subject= "First Message"

body= """Hey Vijay Bisht,

Keep Doing Coding
"""

address = ['vijaysinghbisht18122002@gmail.com',
            'mahendersingh18122002@gmail.com',
            'brandro.2002@gmail.com']

for recipient in address:

    message = f"""From: your_email@gmail.com
To: {recipient}
Subject: {subject}

{body}"""

    mail.sendmail(
        'your_email@gmail.com',
        recipient,
        message
    )


print("Mail Sent Successfully")
mail.quit()


