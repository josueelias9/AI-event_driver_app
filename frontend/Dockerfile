FROM node:16

RUN apt-get update && \
    apt-get upgrade

WORKDIR /usr/src

RUN mkdir frontend

WORKDIR /usr/src/frontend

COPY . .

WORKDIR /usr/src/frontend/my-app

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]