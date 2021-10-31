FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "main.py" ]
