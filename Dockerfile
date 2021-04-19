FROM python:3.9-slim-buster
COPY . /main
WORKDIR /main
RUN pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=main.py
CMD ["flask","run" ,"--host","0.0.0.0" ]
