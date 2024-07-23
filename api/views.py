from flask import render_template, request, jsonify, url_for
from flask.views import MethodView
from utils import TriggerEmail

class HomeView(MethodView):
    def get(self):
        return render_template('index.html')

class SendMail(MethodView):
    def post(self):
        success = TriggerEmail(request).send_mail()	
        return redirect(url_for('home')) 

