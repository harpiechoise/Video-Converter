# Rootless Python
FROM python:3.11-slim-bullseye

# Build essentials for C dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Define a workdir to install requirements
WORKDIR /home/app
# Copy and install the requirements
COPY ./requirements.txt /home/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . /home/app

# Exposing the port
EXPOSE 5000

# Modify the user to be non-root
RUN useradd -m app
RUN chown -R app:app /home/app
USER app


CMD ["python", "server.py"]