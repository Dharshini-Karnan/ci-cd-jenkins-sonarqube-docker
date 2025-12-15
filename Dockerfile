FROM python:3.12-slim

WORKDIR /app

COPY app/ app/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-c", "from app.app import add; print('App running, add(2,3)=', add(2,3))"]
