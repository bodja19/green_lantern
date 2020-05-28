FROM python:3.7

COPY . /app


WORKDIR /app


RUN pip freeze > requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "wsgi.py"]
