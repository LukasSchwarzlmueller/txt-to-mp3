FROM ghcr.io/astral-sh/uv:python3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN uv pip install --system --no-cache -r requirements.txt

COPY server.py .
COPY static/ static/

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
