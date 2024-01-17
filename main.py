import openai 
import json 
import os 
# import request
from flask import Flask,  render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home ():
    if request.method == 'POST':
        user_input = request.form.get('text_field')
        openai_response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=user_input,
          max_tokens=150
        )
        print(openai_response.choices[0].text.strip())
    return render_template('home.html')

