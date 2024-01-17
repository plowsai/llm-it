import openai 
import json 
import os 
import request
from flask import Flask,  render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home ():
    if request.method == 'POST':
        user_input = request.form.get('text_field')
        print(user_input)
    return render_template('home.html')