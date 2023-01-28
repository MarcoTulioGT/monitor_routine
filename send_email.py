import configparser
import os
import locale
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
  leerfichero()


def leerfichero():
  today = datetime.today() 
  #today = datetime.today() - timedelta(days = 2 )
  fecha = today.strftime("%A %d")+" de "+today.strftime("%B")
  f = open("./templates/template_body.txt", "rt")
  body = f.read().replace("#FECHA", fecha)
  #print(body)
  f.close()
  escribirfichero(body)
  
def escribirfichero(body):
  f = open("./html/body.txt","wt")
  f.write(body)
  f.close()



os.system("""echo "" | mutt -e 'my_hdr From:"""+str(mail_from)+"""' -s """+str(subject)+"""  `(date +"%d/%m/%Y")`" -i ./html/body.txt """+str(to)+""" -a ./screenshot.png""") 