FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir flask
EXPOSE 8000
CMD ["python", "app.py"]