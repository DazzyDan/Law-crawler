FROM python:3.8.6
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]