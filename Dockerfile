FROM python:3.9-slim-buster
COPY . /main
WORKDIR /main
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","main.py"]
