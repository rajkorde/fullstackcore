FROM node:20-bookworm

WORKDIR /app

COPY ./package*.json /app/
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]