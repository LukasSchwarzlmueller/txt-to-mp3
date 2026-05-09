FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

COPY requirements.txt ./
RUN uv pip install --system --no-cache -r requirements.txt

COPY server.py .
COPY static/ static/

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
