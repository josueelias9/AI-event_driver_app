FROM python:3.10

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get upgrade -y

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["waitress-serve", "--call", "flaskr:create_app"]

# docker build -t flask_image .
# docker run -t -i -p 5000:5000 --name flask_container flask_image bash