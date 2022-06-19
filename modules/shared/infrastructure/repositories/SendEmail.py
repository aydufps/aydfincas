# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from modules.administrador.domain.services.usuarios import UsuarioR


class SendEmail(object):
    def sendTextEmail(self, emisor, receptor, subject, message, password, name, id):
        # create message object instance
        msg = MIMEMultipart()

        #message = mensaje
        html = """\
      <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <meta name="x-apple-disable-message-reformatting">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="telephone=no" name="format-detection">
    <title></title>
    <!--[if (mso 16)]>
    <style type="text/css">
    a {text-decoration: none;}
    </style>
    <![endif]-->
    <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]-->
    <!--[if gte mso 9]>
<xml>
    <o:OfficeDocumentSettings>
    <o:AllowPNG></o:AllowPNG>
    <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
</xml>
<![endif]-->
</head>

<body>
    <div class="es-wrapper-color">
        <!--[if gte mso 9]>
			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
				<v:fill type="tile" color="#efefef"></v:fill>
			</v:background>
		<![endif]-->
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
            <tbody>
                <tr>
                    <td class="esd-email-paddings" valign="top">
                        <table cellpadding="0" cellspacing="0" class="es-header esd-header-popover" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" esd-custom-block-id="1735" align="center">
                                        <table class="es-header-body" style="background-color: #fef5e4;" width="600" cellspacing="0" cellpadding="0" bgcolor="#fef5e4" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p5t es-p5b es-p15r es-p15l" align="left" bgcolor="#E8F9FD" style="background-color: #e8f9fd;">
                                                        <!--[if mso]><table width="570" cellpadding="0" cellspacing="0"><tr><td width="180" valign="top"><![endif]-->
                                                        <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="es-m-p0r esd-container-frame" width="180" valign="top" align="center">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-image es-m-p0l es-p15l es-m-txt-c" align="left" style="font-size: 0px;"><a href="https://viewstripo.email/" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/4388/4388935.png" alt="Petshop logo" title="Petshop logo" width="118" style="display: block;"></a></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td><td width="20"></td><td width="370" valign="top"><![endif]-->
                                                        <table cellspacing="0" cellpadding="0" align="right">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="370" align="left">
                                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-text">
                                                                                        <p style="font-size: 28px; font-family: helvetica, 'helvetica neue', arial, verdana, sans-serif; color: #132743;"><strong>Gestion&nbsp;de fincas ganaderas</strong></p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                        <!--[if mso]></td></tr></table><![endif]-->
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table class="es-content esd-footer-popover" cellspacing="0" cellpadding="0" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center">
                                        <table class="es-content-body" style="background-color: #edf2f7;" width="600" cellspacing="0" cellpadding="0" bgcolor="#edf2f7" align="center">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p20t es-p5b es-p20r es-p20l" esd-general-paddings-checked="false" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0">
                                                            <tbody>
                                                                <tr>
                                                                    <td class="esd-container-frame" width="560" valign="top" align="center">
                                                                        <table style="border-radius: 0px; border-collapse: separate;" width="100%" cellspacing="0" cellpadding="0">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td class="esd-block-text" align="center">
                                                                                        <h1 style="color: #d7385e;">Hola! alias</h1>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-text es-p10t" align="left">
                                                                                        <p style="font-size: 20px; font-family: helvetica, 'helvetica neue', arial, verdana, sans-serif;">Ingresa al formulario y cambia tu clave de usuario</p>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td class="esd-block-button es-p25t h-auto" align="center" height="73"><span class="es-button-border" style="border-radius: 5px; border-width: 2px; border-color: #333333; background: #132743;"><a href="@url" class="es-button es-button-1655593772118" target="_blank" style="border-radius: 5px; border-top-width: 10px; border-bottom-width: 10px; background: #132743; border-color: #132743; color: #f8efd4; font-family: helvetica, &quot;helvetica neue&quot;, arial, verdana, sans-serif; font-size: 20px;">Cambiar mi clave</a></span></td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>

</html>
        """
        url = "https://aydufps.github.io/vistas/registrarclave/index.html?id=" + \
            str(id)
        html = html.replace("\xf3", " ")
        html = html.replace("alias", name)
        html = html.replace("@url", url)
        part2 = MIMEText(html, 'html')
        # setup the parameters of the message
        # password =
        msg['From'] = emisor
        msg['To'] = receptor
        msg['Subject'] = subject

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        msg.attach(part2)
        # create server
        server = smtplib.SMTP('smtp.gmail.com: 587')

        server.starttls()

        # Login Credentials for sending the mail
        server.login(msg['From'], password)

        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()


''' 
emisor = "jefersonurielhc@ufps.edu.co"
receptor = "asimplemailmore@gmail.com"
asunto = "Cambio de clave"
mensaje = ""
clave = "mjsytbqwyfgsgzdg"
obj = SendEmail()
obj.sendTextEmail(emisor, receptor, asunto, mensaje, clave) '''


def enviarEmail(correo, name, id):
    emisor = "jefersonurielhc@ufps.edu.co"
    receptor = correo  # "asimplemailmore@gmail.com"
    asunto = "Cambio de clave"
    mensaje = ""
    clave = "mjsytbqwyfgsgzdg"
    obj = SendEmail()
    obj.sendTextEmail(emisor, receptor, asunto, mensaje, clave, name, id)
