# ---------------- Dockerfile ----------------
FROM python:3.11-slim

# encodage UTF-8 pour éviter les UnicodeDecodeError Windows
ENV PYTHONIOENCODING=utf-8

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY flow.py .

CMD ["python", "flow.py"]
