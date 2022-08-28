FROM nginx

# delete default nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf


COPY ./modules /etc/nginx

# import new nginx configuration file
COPY nginx.conf /etc/nginx

COPY etc/nginx /etc/nginx