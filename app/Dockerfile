FROM python:3.10.12
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY weather-app.py .
CMD ["python3", "weather-app.py"]