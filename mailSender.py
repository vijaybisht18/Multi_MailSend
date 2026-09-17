import smtplib as sm
from email.message import EmailMessage

mail = sm.SMTP("smtp.gmail.com",587)

mail.ehlo()
mail.starttls()

mail.login('vijaybisht18122002@gmail.com','app_passkey')

emails = ["vijaysinghbisht18122002@gmail.com",
        "mahendersingh18122002@gmail.com",
        "brandro.2002@gmail.com"]

subject = 'Job Opportunity Inquiry – IT/Technical Roles'


body = """ 

Dear Hiring Team,

I hope you are doing well.

I am writing to inquire about any current or upcoming job opportunities in your organization that match my profile. I have completed my MCA and have 1+ year of experience as a Technical Support Engineer, with hands-on exposure to SQL, databases, troubleshooting, system support, data monitoring, reporting, and software/product testing.

I am currently looking for an opportunity where I can utilize my technical skills, gain further industry experience, and contribute to the organization.

I have attached my updated resume for your reference. I would appreciate it if you could consider my profile for any suitable openings.

Thank you for your time and consideration.

Best regards,
Vijay Bisht
📞 8851966018
📧 vijaybisht18122002@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/vijaybisht18122002
        """

cv_path = 'VIJAY BISHT_resume.pdf'

for address in emails:
    msg = EmailMessage()

    msg["from"] = 'vijaybisht18122002@gmail.com' 
    msg["To"] = address
    msg["Subject"] = subject

    msg.set_content(body)

    with open(cv_path,"rb") as pdf:
        pdf_data = pdf.read()

    msg.add_attachment(
        pdf_data,
        maintype="application",
        subtype="pdf",
        filename="VIJAY BISHT_resume.pdf"
    )

    mail.send_message(msg)

print("Message Sent Successfully")

mail.quit()