import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(**context):
    subject = context["var"]["value"].get("subject_mail")
    from_address = context["var"]["value"].get("email")
    password = context["var"]["value"].get("email_password")
    to_address = context["var"]["value"].get("to_address")
    alert_content = context.get("alert_content", "")

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    html_content = f"""
    <html>
    <body>
        <p>El proceso de ETL a Redshift ha sido realizado con éxito.</p>
        <p><b>Alertas:</b></p>
        <p>{alert_content}</p>
    </body>
    </html>
    """

    msg.attach(MIMEText(html_content, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(from_address, password)

        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        print("Email enviado con éxito")
    except Exception as e:
        print(f"Error al enviar correo: {str(e)}")