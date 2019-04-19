from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dss import DSS

dsO=DSS()
digital_signatures = Flask(__name__)
digital_signatures.config['SQLALCHEMY_DATABASE_URI']='sqlite:///students.sqlite3'
digital_signatures.config['SECRET_KEY']="random"
db = SQLAlchemy(digital_signatures)




class answers(db.Model):
    id = db.Column('ans_id', db.Integer, primary_key=True)
    a1 = db.Column(db.String(5))
    a2 = db.Column(db.String(5))
    a3 = db.Column(db.String(5))
    a4 = db.Column(db.String(5))
    a5 = db.Column(db.String(200))
    a6 = db.Column(db.String(200))
    a7 = db.Column(db.String(200))

    def _init_(self, a1, a2, a3, a4, a5, a6, a7):
        self.a1 = a1;
        self.a2 = a2;
        self.a3 = a3;
        self.a4 = a4;
        self.a5 = a5;
        self.a6 = a6;
        self.a7 = a7;

from digital_signatures import routes



