import smtplib as sm

mail = sm.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('vijaybisht18122002@gmail.com','bnwysrpuofsjgcps')

subject= "Regrading Job Oppurnuty"

body= """Hey Vijay Bisht,

I am from your future and I want to say that you're doing great things.
You have a successful life and you have achieved everything you wanted.
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

    
#for emails in address:
 #   message = f"""From: vijaybisht18122002@gmail.com
  #              To: {emails}
   #             Subject: {subject} 
    #            
     #           {body}"""

    #mail.sendmail('vijaybisht18122002@gmail.com',emails,message)



print("Mail Sent Successfully")
mail.quit()


