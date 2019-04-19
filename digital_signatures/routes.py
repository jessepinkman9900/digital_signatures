from flask import render_template
from digital_signatures import digital_signatures

@digital_signatures.route('/digital_signatures')
@digital_signatures.route('/')
@digital_signatures.route('/digital_signatures/introduction')
def introduction():
    return render_template('introduction.html')


@digital_signatures.route('/digital_signatures/theory')
def theory():
    return render_template('theory.html')


@digital_signatures.route('/digital_signatures/objective')
def objective():
    return render_template('objective.html')


@digital_signatures.route('/digital_signatures/experiment')
def experiment():
    return render_template('experiment.html')


@digital_signatures.route('/digital_signatures/manual')
def manual():
    return render_template('manual.html')


@digital_signatures.route('/digital_signatures/quiz', methods=['GET', 'POST'])
def quiz():
    os.remove('answers.sqlite3')
    db.create_all()
    if request.method == 'POST':
        try:
            a1 = request.form['a1']
        except:
            a1 = ""
        try:
            a2 = request.form['a2']
        except:
            a2 = ""
        try:
            a3 = request.form['a3']
        except:
            a3 = ""
        try:
            a4 = request.form['a4']
        except:
            a4 = ""

        answer = answers(a1, a2, a3, a4, request.form['a5'], request.
        form
        ['a6'], request.form['a7'])
        db.session.add(answer)
        db.session.commit()
        flash('Answer Submitted')
        return redirect(url_for('answer'))
    return render_template('quiz.html')


@digital_signatures.route('/digital_signatures/procedure')
def procedure():
    return render_template('procedure.html')


@digital_signatures.route('/digital_signatures/further_reading')
def further_reading():
    return render_template('further_readings.html')


@digital_signatures.route('/digital_signatures/feedback')
def feedback():
    return render_template('feedback.html')

@digital_signatures.route('/digital_signatues/answers',methods=['GET','POST'])
def answer():
    return render_template('answer.html',answers = answers.query.all())

@digital_signatures.route('/api/hash')
def hash():
    val = str(request.args.get('val'))
    dsO.set_message(val)
    h = dsO.gen_hash()
    res = {'hash': h}
    return json.dumps(res)

@digital_signatures.route('/api/generate')
def generate_keys():
    e = int(request.args.get('e'))
    bits = int(request.args.get('sz'))
    if e==0:
        e = 65537
    key = dsO.gen_keys(2*bits, e)
    res = {'e': e, 'key': key}
    return json.dumps(res)

@digital_signatures.route('/api/encrypt')
def encrypt():
    h = str(request.args.get('h'))
    ds, ds64 = dsO.gen_DS(h)
    res = {'ds': ds, 'ds64': ds64}
    return json.dumps(res)

