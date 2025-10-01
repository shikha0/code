FROM python:3.13-slim as base
LABEL authors="shikha p"
RUN groupadd --gid 1000 appgroup && \
    useradd --uid 1000 --gid appgroup --shell /bin/bash --create-home appuser \
COPY . /app
USER appuser
RUN chown -R appuser:appgroup /app
WORKDIR /app
Run pip install -r /app/requirements.txt
EXPOSE 8080
ENTRYPOINT ["python", "mainfile.py"]
