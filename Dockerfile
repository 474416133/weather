FROM python3.11

WORKDIR /usr/src/app

COPY . .

CMD ["uwsgi", "--ini", "uwsgi.ini"]