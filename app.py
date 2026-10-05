from flask import Flask,render_template,request
import smtplib as sm
from email.message import EmailMessage


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send",methods=["POST"])
def sende_mail():
    sender_email = request.form["sender_email"]
    app_password = request.form["app_password"]
    recipients = request.form["recipients"]
    subject = request.form["subject"]
    message = request.form["message"]
    attachment = request.files.get("attachment")

    emails = recipients.splitlines()    #ye split ko alag alag line me karega

    mail = sm.SMTP("smtp.gmail.com",587)

    mail.ehlo()
    mail.starttls()

    mail.login("sender_mail","app_password")

    for address in emails:
        msg = EmailMessage()

        msg["From"] = sender_email
        msg["To"] = address
        msg["Subject"] = subject

        msg.set_content(body)

        if attachment and attachment.filename:
            file_data = attachment.read()

            msg.add_attachment(
                file_data,
                maintype="application",
                subtype="octet-stream",
                filename = attachment.filename
            )
        mail.send_message(msg)
    
    mail.quit()

    return render_template("index.html",success=True )

                                                                                                            
if __name__ == "__main__":
    app.run(debug=True)