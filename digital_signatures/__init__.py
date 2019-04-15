from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

digital_signatures = Flask(__name__)
digital_signatures.config['SECRECT_KEY']='digital_signatures'
digital_signatures.config.from_object(Config)
db = SQLAlchemy(digital_signatures)
# migrate = Migrate(digital_signatures, db)

from digital_signatures import routes
