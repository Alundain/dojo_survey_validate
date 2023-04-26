from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "SECRET"

@app.route('/')
def index():
    return render_template('survey.html')

@app.route('/process', methods = ['POST'])
def process():
    return redirect('success' )