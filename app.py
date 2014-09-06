from flask import Flask, request, redirect
from twilio.rest import TwilioRestClient
import twilio.twiml
from firebase import firebase
firebase = firebase.FirebaseApplication('https://sentencesoup.firebaseio.com', None)

account_sid = "ACec64a5b0feb7121fd6a33718d1fc4390"
auth_token = "0a4ecac03a0cb832a0cbfd221c329b20"
client = TwilioRestClient(account_sid, auth_token)

app = Flask(__name__)

DB = 'lib/db_methods.py'

# @app.route("/")
# def index():
#     return "Hello World!"

@app.route("/", methods=['GET', 'POST'])
def getResponse():
	word = request.values.get('Body', None)

	resp = twilio.twiml.Response()
	resp.message(word)

	result = firebase.post('/texts/', {'Sentence': word})

	return str(resp)

if __name__ == "__main__":
    app.run()



# from flask import Flask, request, session, g, redirect, url_for, abort, \
#     render_template, flash, _app_ctx_stack
# from flask.ext.triangle import Triangle

# app = Flask(__name__, static_path='/static')
# Triangle(app)

# @app.route("/")
# def index():
#   return_vals = {
#     'title': 'Sentence Soup'
#   }
#   return render_template('index.html', return_vals=return_vals)

# if __name__ == "__main__":
#     app.run()