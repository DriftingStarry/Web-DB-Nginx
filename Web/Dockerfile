FROM python:3.8.18
WORKDIR /work
COPY . /work/
EXPOSE 11451
ENV FLASK_APP main.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN pip install -r requirements.txt
CMD ["flask","run"]