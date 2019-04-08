from digital_signatures import digital_signatures

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"