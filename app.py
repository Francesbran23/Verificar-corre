from flask import Flask, request, jsonify, send_file
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import smtplib

app = Flask(__name__)


@app.route('/imagen')
def obtener_imagen():
    # Lógica para obtener la imagen
    # ...
    
    # Devuelve la imagen como respuesta
    return send_file('/home/Francis/mysite/ax.png', mimetype='image/png')

@app.route('/enviar_codigo', methods=['POST'])
def enviar_codigo():
    # Obtener la dirección de correo electrónico del cuerpo del POST
    correo = request.json['correo']
    
    msg = MIMEMultipart()
    # setup the parameters of the message 
    password = "sffjxbrtpitcdest"
    msg['From'] = "faststernverificacion@gmail.com"
    msg['To'] = correo
    msg['Subject'] = "Verificacion"

    # Generar un número aleatorio de 6 dígitos
    codigo = str(random.randint(100000, 999999))
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            /* Estilos CSS aquí */
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                padding: 20px;
            }
            
            .container {
                max-width: 540px;
                height: 700px;
                margin: 0 auto;
                background-color: #ffffff;
                padding: 40px;
                border-radius: 5px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                background-image: url("https://Francis.pythonanywhere.com/imagen");
                background-position: center;
                background-repeat: no-repeat;
                background-size: 100% auto;
            }
            
            h1 {
                text-align: center;
                color: #fff;
                text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px;
                margin-top: 50%;
            }
            
            p {
                color: #666666;
            }
            
            .verification-code {
                font-size: 24px;
                font-weight: bold;
                color: #fff;
                text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px ;
                text-align: center;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Código de Verificacion:</h1>
            <p class="verification-code">"""+codigo+"""</p>
        </div>
    </body>
    </html>
    """
    
    
    # add in the message body 
    msg.attach(MIMEText(html, 'html'))
    
    #create server 
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    
    # Login Credentials for sending the mail 
    server.login(msg['From'], password)
    # send the message via the server. 
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    
    
    # # Enviar el código por correo electrónico
    # smtp_server = 'smtp.gmail.com'
    # smtp_port = 587
    # username = 'tucorreo@gmail.com'
    # password = 'tupassword'

    # message = f'Su código de verificación es: {codigo}'

    # with smtplib.SMTP(smtp_server, smtp_port) as server:
    #     server.starttls()
    #     server.login(username, password)
    #     server.sendmail(username, correo, message)

    # Devolver el código como respuesta al cliente
    return jsonify({'codigo': codigo})