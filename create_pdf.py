from jinja2 import Environment, FileSystemLoader
import os, pdfkit
from send_email import configuracion, send_mail_attachement

def generate_html(title, description):
    images = []
    for path in os.scandir('./images'):
        if path.is_file():
            graph = {}
            graph["path"] = path.name
            graph["name"] = (path.name.replace("_"," ").replace(".png", ""))
            images.append(graph)
    
    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template('template.html')
    
    root = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(root, 'html', 'index.html')
    
    with open(filename, 'w') as fh:
        fh.write(template.render(
            h1 = description,
            title = title,
            images = images
        ))
    generate_pdf()
    body = configuracion()
    send_mail_attachement(body)


def generate_pdf():
    #pass
    path_wkhtmlopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  #Windows
    #path_wkhtmlopdf = "/usr/local/bin/wkhtmltopdf"   #linux
    kitoptions = { "enable-local-file-access": None }
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmlopdf)
    with open(r"C:\Users\ctcatalan\Desktop\Proyectos\monitor_routine\html\index.html") as f:
        pdfkit.from_file(f, r'C:\Users\ctcatalan\Desktop\Proyectos\monitor_routine\reports\rpt_itbackend_27_01_2023.pdf',configuration=config , options=kitoptions)    
    '''Docker
    with open("/opt/app/html/index.html") as f:
        pdfkit.from_file(f, '/opt/app/reports/rpt_itbackend_27_01_2023.pdf',configuration=config, options=kitoptions)
    '''


