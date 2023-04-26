from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "SECRET"

from flask_app.controllers import surveys 



if __name__ == '__main__':
    app.run(debug=True)