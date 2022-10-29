FROM python:latest
WORKDIR /app
COPY src/ .
RUN pip3 install -r requirements.txt
EXPOSE 80
CMD ["python3", "app.py"]
