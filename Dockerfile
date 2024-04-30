FROM python:3.8-alpine3.12

WORKDIR /app

EXPOSE 5000
ENV FLASK_APP=app.py

COPY . /app
RUN pip install -r requirements.txt

ENTRYPOINT [ "flask"]
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]