#!/bin/bash

if [ "$APP_MODE" = "prod" ]; then
	npm run build
	npm run preview -- --host
else
	npm run dev -- --host 
fi