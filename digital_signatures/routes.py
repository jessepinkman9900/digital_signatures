from flask import render_template
from digital_signatures import digital_signatures

# may need modification
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


@digital_signatures.route('/digital_signatures/experiment', methods=['GET', 'POST'])
def experiment():
    return render_template('experiment.html')


@digital_signatures.route('/digital_signatures/manual')
def manual():
    return render_template('manual.html')


@digital_signatures.route('/digital_signatures/quizzes', methods=['GET', 'POST'])
def quizzes():
    return render_template('quizzes.html')


@digital_signatures.route('/digital_signatures/procedure')
def procedure():
    return render_template('procedure.html')


@digital_signatures.route('/digital_signatures/further_reading')
def further_reading():
    return render_template('further_readings.html')


@digital_signatures.route('/digital_signatures/feedback')
def feedback():
    return render_template('feedback.html')
