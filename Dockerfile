FROM python:3.10.7-slim-bullseye
RUN pip install --no-cache-dir qrcode Cryptography googletrans==3.1.0a0 colorama pillow numpy
WORKDIR /app
COPY . .
CMD [ "python", "./main.py" ]
