FROM python:3.12.4-slim-bookworm

LABEL maintainer="samyak.uttam@wdc.com"

COPY . /src

WORKDIR /src

RUN pip install -r requirements.txt

CMD ["python", "./app.py"]