FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

COPY ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh

COPY . .

ENTRYPOINT ["sh", "/app/entrypoint.sh"]

