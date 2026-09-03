FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml .
COPY main.py .

RUN pip install --no-cache-dir .

EXPOSE 8080

CMD ["python", "main.py"]
