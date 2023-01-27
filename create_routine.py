import configparser
from selenium import webdriver
from dahsboards.grafana import grafana_display_default
from dahsboards.elasticsearch import elastic_display_default
from dahsboards.instana import instana_display_default
from dahsboards.solarwinds import solarwinds_display_default
from dahsboards.inhouseweb import inhouseweb_display_default

#file properties
config = configparser.ConfigParser(interpolation=None)
config.sections()
config.read('properties.ini')
urls = config["URLS"]
accesos = config["ACCESOS"]

#Driver selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False
driver = webdriver.Chrome(urls["DRIVER"], chrome_options=chrome_options, service_args=['--verbose', '--log-path=chrome.log'])


correo_destino = accesos["correo_destino"]

grafana_display_default(driver, urls["URL_METRICAS"], 60, accesos["usr_graf_docker"], accesos["pass_graf_docker"], 'grafana_display_default.png')
elastic_display_default(driver, urls["URL_HIPERION"], 60, accesos["usr_ekl_hiperion"],accesos["pass_ekl_hiperion"],'elastic_display_hiperion.png')
elastic_display_default(driver, urls["URL_FENIX"], 60, accesos["usr_ekl_fenix2"],accesos["pass_ekl_fenix2"],'elastic_display_fenix.png')
elastic_display_default(driver, urls["URL_KANSAS"], 60, accesos["usr_ekl_kansas"],accesos["pass_ekl_kansas"], 'elastic_display_kansas.png')
instana_display_default(driver, urls["URL_INSTANA"], 60, accesos["usr_instana"],accesos["pass_instana"],'instana_display_default.png')
solarwinds_display_default(driver, urls["URL_SOLARWINDS"], 30, accesos["usr_sam"], accesos["pass_sam"], 'solarwinds_display_default.png')
inhouseweb_display_default(driver, urls["URL_KPI"], 10,'inhouseweb_display_default.png')
