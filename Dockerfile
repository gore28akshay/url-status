FROM python:latest
WORKDIR /app
COPY src/ .
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["python3", "app.py"]
