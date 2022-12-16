FROM python:3
LABEL maintainer="Prometheus <99234@qq.com>" version="0.3.2.11" description="Vulfocus for Docker"
EXPOSE 80
RUN mkdir /vulfocus-api/
WORKDIR /vulfocus-api/
ADD vulfocus-api/ /vulfocus-api/
ENV VUL_IP="" EMAIL_HOST="" EMAIL_HOST_USER="" EMAIL_HOST_PASSWORD="" DOCKER_URL="unix://var/run/docker.sock"
RUN mv /etc/apt/sources.list /etc/apt/sources.list.back && \
    cp /vulfocus-api/sources.list /etc/apt/sources.list && \
    apt update && \
    apt upgrade -y && \
    apt install redis-server -y && \
    apt install nginx -y && \
    rm -rf /var/www/html/* && \
    cp /vulfocus-api/nginx.conf /etc/nginx/nginx.conf && \
    cp /vulfocus-api/default /etc/nginx/sites-available/default && \
    cp /vulfocus-api/default /etc/nginx/sites-enabled/default && \
    python3 -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package -r requirements.txt && \
    chmod u+x /vulfocus-api/run.sh && \
    python3 /vulfocus-api/manage.py makemigrations
ADD dist/ /var/www/html/
CMD ["sh", "/vulfocus-api/run.sh"]