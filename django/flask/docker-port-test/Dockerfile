FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
        curl \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install flask==3.1.0

EXPOSE 5000

CMD ["python", "app.py"]
