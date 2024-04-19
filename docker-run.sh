docker stop weather
docker rm weather
docker run \
  -p 8080:5000 \
  -dt \
  --restart=always \
  --env TZ=Asia/Shanghai \
  --env ENV=prod \
  -v /home/www/sites/weather/logs:/var/app/logs \
  -v /home/www/sites/weather:/var/app \
  --log-driver json-file \
  --log-opt max-size=10m \
  --name weather python:3.11 \
  sh -c 'uwsgi uwsgi.ini'
