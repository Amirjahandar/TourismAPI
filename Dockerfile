FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR  /tourism-api

COPY . /tourism-api/

COPY requirements .

RUN pip3 install -r requirements/base.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]