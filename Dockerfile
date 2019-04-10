FROM python:3.6-slim

COPY . /digital_signatures
WORKDIR /digital_signatures

RUN pip install --trusted-host pypi.python.org -r requirements.py
EXPOSE 80
ENV NAME World
CMD ["python3","digital_signatures.py"]
CMD ["export FLASK_APP=./digital_signatures.py"]
CMD ["flask run"]
