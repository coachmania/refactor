# DOCKERFILE DJANGO
FROM	python:3.12-slim-bookworm

# Set environment variables
ENV		PYTHONDONTWRITEBYTECODE 1
ENV		PYTHONUNBUFFERED 1
ENV		DJANGO_SETTINGS_MODULE=mainProject.settings

# Ports
EXPOSE	8000

WORKDIR	/usr/src/django

# Install apt requirements
COPY	./requirements-apt.txt /tmp
RUN		apt-get update
RUN		xargs -a /tmp/requirements-apt.txt apt-get install -y
RUN		apt-get clean
RUN		rm -rf /var/lib/apt/lists/*

# Install pip requirements
COPY	./requirements-pip.txt /tmp
RUN		pip install --upgrade pip
RUN		pip install --no-cache-dir -r /tmp/requirements-pip.txt

# Copy project
COPY	. /usr/src/django
RUN		chmod +x ./entrypoint.sh
CMD		./entrypoint.sh