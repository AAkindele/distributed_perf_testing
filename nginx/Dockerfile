FROM nginx

USER nginx

ADD ./index.html /data/www/index.html
ADD ./nginx.conf /etc/nginx/nginx.conf

ENTRYPOINT ["nginx"]