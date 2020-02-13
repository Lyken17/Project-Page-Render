import yaml
import jinja2
from jinja2 import Environment, FileSystemLoader
import os
import markdown


def load_yaml(filename):
    with open(filename, 'rb') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def generate_index(info):
    env = Environment(
        loader=FileSystemLoader(os.path.dirname(os.path.abspath(__file__))),
        trim_blocks=True
    )

    md = markdown.Markdown(extensions=['meta'])
    env.filters['markdown'] = lambda text: jinja2.Markup(md.convert(text))

    template = env.get_template('template.html')
    htmlpage = template.render(
        authors=info["authors"],
        beamers=info["beamers"],
		paragraphs=info["paragraphs"],
		affiliations=info["affiliations"],
        info=info
    )

    filename = "index.html"
    with open(filename, 'w') as f:
        f.write(htmlpage)
        print("Successfuly generate_index %s" % filename)


data = load_yaml("info.yaml")

generate_index(data)
