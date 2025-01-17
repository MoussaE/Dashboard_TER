FROM python:3.8-slim
WORKDIR . 
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY ./ ./
EXPOSE 8050
CMD ["python", "./server.py"]