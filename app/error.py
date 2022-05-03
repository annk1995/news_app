from flask import render_template
from app import app


@app.errorhandler(404)
def four(error):
    return render_template('four.html'),404