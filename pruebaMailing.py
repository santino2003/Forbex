# import smtplib
# from email.message import EmailMessage
# email_smtp = "smtp.gmail.com"
# contraseña = "hqfs npzt yyey vaxq"
# mensaje = EmailMessage()


# contenidoEmail = "test de python"

# enviador = "santinopeiretti2003@gmail.com"

# receptor = "fabriciopeiretti@gmail.com"


# mensaje['Subject'] = contenidoEmail
# mensaje['From'] = enviador
# mensaje['To'] = receptor

# mensaje.set_content("Hola pa si lees esto es un mail automatico y significa que esta poronga funciona")

# server = smtplib.SMTP(email_smtp, '587')

# server.ehlo()
# server.starttls()
# server.login(enviador,contraseña)
# server.send_message(mensaje)


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

# Configura los detalles del servidor SMTP y las credenciales
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "santinopeiretti2003@gmail.com"
smtp_password = "hqfs npzt yyey vaxq"

# Crea un objeto MIMEMultipart
msg = MIMEMultipart()

# Agrega el remitente y el destinatario
msg['From'] = "santinopeiretti2003@gmail.com"
msg['To'] = "santinopeiretti2003@gmail.com"
msg['Subject'] = 'Asunto del correo'

# Agrega un mensaje de texto
msg.attach(MIMEText('Este es el mensaje de correo con  imagen adjunta.', 'plain'))

# Adjunta una imagen desde un archivo en tu sistema
image_filename = 'image.jpg'
with open(image_filename, 'rb') as image_file:
    image = MIMEImage(image_file.read(), name='image.jpg')
    msg.attach(image)

# Adjunta una imagen desde una URL (puedes usar requests para descargarla)
# Ejemplo:
# import requests
# image_url = 'https://example.com/imagen.jpg'
# response = requests.get(image_url)
# image_data = response.content
# image = MIMEImage(image_data, name='imagen.jpg')
# msg.attach(image)

# Conecta al servidor SMTP y envía el mensaje
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, msg['To'], msg.as_string())
    server.quit()
    print('Correo enviado exitosamente')
except Exception as e:
    print('Error al enviar el correo:', str(e))


