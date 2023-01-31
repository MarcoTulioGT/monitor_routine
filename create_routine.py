import configparser
from selenium import webdriver
from dahsboards.grafana import grafana_display_default
from dahsboards.elasticsearch import elastic_display_default
from dahsboards.instana import instana_display_default
from dahsboards.solarwinds import solarwinds_display_default
from dahsboards.inhouseweb import inhouseweb_display_default
from create_pdf import generate_html
from send_email import configuracion


#file properties
config = configparser.ConfigParser(interpolation=None)
config.sections()
config.read('properties.ini')
urls = config["URLS"]
accesos = config["ACCESOS"]


configuracion()

#Driver selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False
driver = webdriver.Chrome(urls["DRIVER"], chrome_options=chrome_options, service_args=['--verbose', '--log-path=chrome.log'])




grafana_display_default(driver, urls["URL_METRICAS"], 60, accesos["usr_graf_docker"], accesos["pass_graf_docker"], 'Metricas_alertas_SMS.png')
elastic_display_default(driver, urls["URL_HIPERION"], 60, accesos["usr_ekl_hiperion"],accesos["pass_ekl_hiperion"],'Metricas_hiperion.png')
elastic_display_default(driver, urls["URL_FENIX"], 60, accesos["usr_ekl_fenix2"],accesos["pass_ekl_fenix2"],'Metricas_fenix_1_y_2.png')
elastic_display_default(driver, urls["URL_KANSAS"], 60, accesos["usr_ekl_kansas"],accesos["pass_ekl_kansas"], 'Metricas_kansas.png')
instana_display_default(driver, urls["URL_INSTANA"], 60, accesos["usr_instana"],accesos["pass_instana"],'Metricas_instana.png')
solarwinds_display_default(driver, urls["URL_SOLARWINDS"], 40, accesos["usr_sam"], accesos["pass_sam"], 'Alertas_solarwinds.png')
inhouseweb_display_default(driver, urls["URL_KPI"], 20,'KPI_regional.png')

driver.close()
driver.quit()


generate_html(accesos["html_title"], accesos["html_description"])
