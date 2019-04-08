FROM python:3.6-slim

WORKDIR /digital_signatures

COPY ./digital_signatures   

RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 80
ENV NAME World
CMD ["python3","digital_signatures.py"]
