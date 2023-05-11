import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.office365.com"
port = 587

with smtplib.SMTP(smtp_server, port) as server:
    # 請填寫您的電子郵件帳戶和密碼
    print("Start to login")
    email = "ctchow@DONGHWATelecom.onmicrosoft.com"
    password = "Vam44078Vam44078"

    # 登入SMTP伺服器
    server.starttls()  # 如果使用 SSL，請改用 server.startssl()
    server.login(email, password)

    # 創建郵件內容
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = "cht_frank@cht.com.tw"
    msg["Subject"] = "Email Subject"
    msg.attach(MIMEText("Email body text", "plain"))

    print("Start to send email")
    # 寄送電子郵件
    recipient = "cht_frank@cht.com.tw"
    server.sendmail(email, recipient, msg.as_string())
