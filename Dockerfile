FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .

RUN apt-get update && apt-get upgrade -y && apt-get clean && \
    pip install --upgrade pip setuptools wheel

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]