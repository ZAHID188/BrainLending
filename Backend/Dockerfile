FROM python:3.12.0

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]