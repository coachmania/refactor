FROM	node:22-alpine

WORKDIR	/usr/src/vue

COPY	. /usr/src/vue
RUN		npm install
EXPOSE	5173

CMD		["npm", "run", "dev"]