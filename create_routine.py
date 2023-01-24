import configparser



#file properties
config = configparser.ConfigParser()
config.sections()
config.read('properties.ini')

urls = config["URLS"]
accesos = config["ACCESOS"]



url_metricas = urls["URL_METRICAS"]
correo_destino = accesos["correo_destino"]
print(url_metricas)
print(correo_destino)
