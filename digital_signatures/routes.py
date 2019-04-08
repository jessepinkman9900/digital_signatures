from flask import render_template
from digital_signatures import digital_signatures

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')