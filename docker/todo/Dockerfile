FROM node:lts-alpine as build-stage

#COPY . /usr/src/todos
#WORKDIR /usr/src/todos
#RUN npm i
#RUN npm run build
#RUN npm pack

WORKDIR /app


# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

FROM nginx as production-stage
RUN mkdir /app
COPY --from=build-stage /app/dist /app
COPY examples/todos /app/todos
COPY nginx.conf /etc/nginx/nginx.conf

