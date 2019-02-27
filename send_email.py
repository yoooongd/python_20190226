import csv
import smtplib
import os
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from jinja2 import Template


smtp = smtplib.SMTP_SSL("smtp.naver.com",465)
smtp.login("tel4730", "Yang1749**")

# filename="1.jpg"
# with open(filename,"rb") as img_file:
#     img = img_file.read()
    
with open("email.html","r",encoding="utf-8") as html:
    email_template=html.read()
    



t=Template(email_template)


with open("student_list.csv","r") as f:
    csv_reader = csv.reader(f)    
    
    for student in csv_reader:
        msg = EmailMessage()
        msg["Subject"] = f"{student[0]} 삼성 공채 정보입니다."
        msg["From"] = "tel4730@naver.com"
        msg["To"] = student[1]
        render_html=t.render(name=student[0])
        
        for filename in os.listdir("./images"):
            with open(f'./images/{filename}',"rb") as f:
                img = f.read()
                part=MIMEApplication(img, name=filename)
                part.add_header("Content-ID",f'<{filename}>')
                msg.attach(part)
                
        
        msg.add_alternative(render_html, subtype="html")
        part = MIMEApplication(img, name=filename)
        msg.attach(part)
        
        smtp.send_message(msg)
        print(student[0])