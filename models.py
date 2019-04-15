from digital_signatures import db

class Quiz(db.Model):
    q_no = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(4096), index=True, unique=True)
    answer = db.Column(db.String(32768), index=True)

    def __repr__(self):
        return '<Answer {}>'.format(self.answer)