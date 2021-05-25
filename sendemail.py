import smtplib
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
SUBJECT = "VM test"
def sendgridmail(user,TEXT):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(#mail, #pass)
    
    
    #mailtemptest
    conte="""
<!DOCTYPE html>
<html>
    <body>
        <div style="background-color:#eee;padding:10px 20px;">
            <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;"><center>Expense Manager Registration Successful</center></h2><br>
<center><p> This is a prototype built for VMware Buildathon'21</p><center>

                    <div><br/>with ❤️
        <a href="https://ritchiepulikottil.netlify.app/" target="_blank" > Ritchie Pulikottil </a></div>
<p>Also known as expense manager and money manager, an expense tracker is a software or application that helps to keep an accurate record of your money inflow and outflow. Many people in India live on a fixed income, and they find that towards the end of the month they don't have sufficient money to meet their needs.</p>
        <div style="padding:20px 0px">
            <div style="height: 500px;width:400px">
    
                <div style="text-align:center;">
                    
                    <br>
                    <br>
                    
                </div>
            </div>
        </div>
    </body>
</html>
"""
    
    content1=Content("text/html",conte)




    sg = sendgrid.SendGridAPIClient(#SENDGRID API KEY)
    from_email = Email("")  # Change to your verified sender
    to_email = To(user)  # Change to your recipient
    subject = "VM ware"
    content = Content("text/plain",TEXT)
    mail = Mail(from_email, to_email, subject, content1)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
    s.quit()
