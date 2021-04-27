FROM debian:latest

ADD . /app
WORKDIR /app

#ENV http_proxy http://10.0.75.1:3128
#ENV https_proxy https://10.0.75.1:3128

RUN echo "Acquire::http::proxy=\"http://10.0.75.1:3128\";" >> /etc/apt/apt.conf

RUN apt-get update
RUN apt-get install -y python3 python3-pip nginx libpcre3-dev

RUN python3 -m pip install --upgrade pip  --trusted-host pypi.python.org \
                                         --trusted-host files.pythonhosted.org \
                                         --trusted-host pypi.org

RUN pip3 install -r requirements.txt --trusted-host pypi.python.org \
                                     --trusted-host files.pythonhosted.org \
                                     --trusted-host pypi.org

COPY default.conf /etc/nginx/conf.d/default.conf

CMD ["/bin/sh", "/app/run.sh"]
