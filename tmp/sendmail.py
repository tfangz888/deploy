import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header


smtp_server = "smtp.163.com"
smtp_port = 25
user = "XXXXXX@163.com"
receiver = "XXXXXX@163.com"

password = "XXXXXX"  # 163 SMTP授权码（如果需要）


def send_mail(subject: str, body: str):
    msg = MIMEText(body, "plain", "utf-8")
    msg["From"] = user
    msg["To"] = receiver
    msg["Subject"] = Header(subject, "utf-8")

    server = smtplib.SMTP(smtp_server, smtp_port, timeout=30)

    # 如果你需要 TLS，取消注释
    # server.starttls()

    if password:
        server.login(user, password)

    server.sendmail(user, receiver, msg.as_string())
    server.quit()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python send_mail.py <subject> <body>")
        sys.exit(1)

    subject = sys.argv[1]
    body = sys.argv[2]

    send_mail(subject, body)
