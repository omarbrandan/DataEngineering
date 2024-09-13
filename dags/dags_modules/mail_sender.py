import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(**context):
    subject = context["var"]["value"].get("subject_mail")
    from_address = context["var"]["value"].get("email")
    password = context["var"]["value"].get("email_password")
    to_address = context["var"]["value"].get("to_address")

    # Crear el objeto MIME
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Contenido HTML
    html_content = """
    <html>
    <body>
        <p>El proceso de ETL a Redshift ha sido realizado con éxito.</p>
    </body>
    </html>
    """

    # Adjuntar el contenido HTML
    msg.attach(MIMEText(html_content, 'html'))

    try:
        # Crear la sesión SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Usa tu servidor SMTP y puerto
        server.starttls()  # Activar TLS

        # Iniciar sesión en el servidor
        server.login(from_address, password)

        # Enviar el correo
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        print("Email enviado con éxito")
    except Exception as e:
        print(f"Error al enviar correo: {str(e)}")