FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Non-root user — matches the runbook's securityContext (runAsUser: 1000)
RUN useradd -u 1000 -m appuser
USER 1000

EXPOSE 5007

# gunicorn only writes to stdout/stderr, so this works fine under
# readOnlyRootFilesystem: true with just /tmp mounted writable
CMD ["gunicorn", "--bind", "0.0.0.0:5007", "--workers", "2", "app:app"]
