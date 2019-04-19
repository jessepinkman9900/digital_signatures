from digital_signatures import digital_signatures
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(digital_signatures)

if __name__ == '__main__':
    db.create_all()


