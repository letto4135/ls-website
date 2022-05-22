FROM python:3.10

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    python3-dev \
    python3-setuptools \
    python3-wheel

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8080

RUN python3 manage.py migrate

CMD ["daphne", "ls_church.asgi:application", "-b", "0.0.0.0", "-v", "2", "-p", "8080"]
#CMD ["gunicorn", "--bind", ":8080", "--workers", "2", "ls_church.asgi"]
