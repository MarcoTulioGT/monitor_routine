import configparser
import os
import locale
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime, timedelta


#file properties
config = configparser.ConfigParser(interpolation=None)
config.sections()
config.read('properties.ini')
urls = config["URLS"]
accesos = config["ACCESOS"]
to = accesos["to"]
subject = accesos["subject"]
mail_from = accesos["from"]

def configuracion():
  locale.setlocale(locale.LC_ALL, 'es_GT')
  today = datetime.today() 
  #today = datetime.today() - timedelta(days = 2 )
  fecha = today.strftime("%A %d")+" de "+today.strftime("%B")
  f = open("./templates/template_body.txt", "rt")
  body = f.read().replace("#FECHA", fecha)
  #print(body)
  f.close()
  f = open("./html/body.txt","wt")
  f.write(body)
  f.close()
  return body
  
  #os.system("""echo "" | mutt -e 'my_hdr From:"""+str(mail_from)+"""' -s """+str(subject)+"""  `(date +"%d/%m/%Y")`" -i ./html/body.txt """+str(to)+""" -a ./screenshot.png""") 





def send_mail_attachement(body):
    try:
        msg = MIMEMultipart()
        msg.attach(MIMEText(body, 'plain'))
        attach_file_name2 = './reports/rpt_itbackend_27_01_2023.pdf'
        attach_file_name = 'Rutina.pdf'
        payload = MIMEBase('application', 'octate-stream')
        with open(attach_file_name2, 'rb') as fp:
          payload.set_payload(fp.read())
          payload.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
          encoders.encode_base64(payload) 
        msg.attach(payload)
        msg['From'] = mail_from
        msg['To'] = to
        msg['Subject'] = subject
        server = smtplib.SMTP('smtp.tigo.com.gt', 25)
        server.sendmail(mail_from, to, msg.as_string())   
        print("Successfully sent email")
    except Exception as e:
        print(e)
        



