from jinja2 import Environment, FileSystemLoader
import os, pdfkit

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


def generate_pdf():
    #pass
    path_wkhtmlopdf = "wkhtmltopdf"
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmlopdf)
    with open("./html/index.html") as f:
        pdfkit.from_file(f, './reports/rpt_itbackend_27_01_2023.pdf',configuration=config)
