from abc import ABC, abstractmethod
from email.mime.text import MIMEText 
import smtplib 
from email.message import EmailMessage

class EmailContext(ABC):
    @abstractmethod
    def email_login(self):
        pass
    
    @abstractmethod
    def set_context(self):
        pass


class TriggerEmail(EmailContext):
    def __init__(self, data):
        self.data = data
        self.sender_email = "*****@gmail.com"
        self.sender_password = "######"
    def email_login(self):
        # Logging in to our email account 
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo() 
        server.starttls() 
        server.login(self.sender_email, self.sender_password) 
        return server
    
    def set_context(self):
        # Sender's and Receiver's email address
        name = self.data.form['name'] 
        subject = self.data.form['Subject'] 
        email = self.data.form['_replyto'] 
        message = self.data.form['message'] 
        msg = EmailMessage() 
        msg.set_content("First Name : "+str(name) 
                        +"\nEmail : "+str(email) 
                        +"\nSubject : "+str(subject) 
                        +"\nMessage : "+str(message)) 
        msg['To'] = email 
        msg['From'] = self.sender_email 
        msg['Subject'] = subject
        return msg

    def send_mail(self):
        # Send the message via our own SMTP server. 
        msg = self.set_context()
        server = self.email_login()
        try: 
            # sending an email 
            server.send_message(msg) 
            print("Send") 
        except: 
            print("Fail to Send")
            return False
        return True 
