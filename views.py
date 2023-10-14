from app import app
from flask import render_template
from models import Portfolio

@app.route('/')
def index():
    portfolio = Portfolio.query.all()
    return render_template('index.html',portfolio=portfolio)