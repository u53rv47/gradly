server {
    listen ${LISTEN_PORT};
    server_name backend.gradly.org 3.220.120.229 ec2-3-220-120-229.compute-1.amazonaws.com 127.0.0.1 localhost;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}