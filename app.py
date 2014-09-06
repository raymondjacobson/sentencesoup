from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, _app_ctx_stack
from flask.ext.triangle import Triangle

app = Flask(__name__, static_path='/static')
Triangle(app)

@app.route("/")
def index():
  return_vals = {
    'title': 'Sentence Soup'
  }
  return render_template('index.html', return_vals=return_vals)

if __name__ == "__main__":
    app.run()