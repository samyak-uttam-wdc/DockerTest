FROM python:3.12.4-slim-bookworm

LABEL maintainer="samyak.uttam@wdc.com"

RUN apt-get update && \
    apt-get install -y unixodbc unixodbc-dev

COPY . /src

WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]