from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_flatpages import FlatPages

app = Flask(__name__)
Bootstrap(app)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)


@app.route('/')
def index():
    return render_template('index.html', pages=pages)


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/resume/')
def resume():
    return render_template('resume.html')


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.run(debug=True)
