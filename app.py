from flask import Flask
from flask import Request
from jinja2 import Template
app = Flask(__name__)

@app.route("/")
def hello():
    return "<a href='/modis'>Modis Video</a><br/><a href='/user-agent'>Mon user-agent</a>"

@app.route("/modis")
def modis():
    return '<iframe width="560" height="315" src="https://www.youtube.com/embed/4hzGMqk0-us" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

@app.route("/user-agent")
def useragent():
    template = "mon user agent est {{ ua }}"
    data = {
        "ua": Request.headers.get('User-Agent')
    }
    jtemplate = Template(template)
    return jtemplate.render(data)
