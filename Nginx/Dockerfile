FROM centos:centos7
EXPOSE 80
WORKDIR /usr/local/src/
RUN yum -y install gcc gcc-c++\
    && yum -y install pcre-devel\
    && yum -y install zlib-devel\
    && yum -y install openssl openssl-devel\
    && yum -y install wget
RUN wget http://downloads.sourceforge.net/project/pcre/pcre/8.35/pcre-8.35.tar.gz\
    && tar zxvf pcre-8.35.tar.gz
WORKDIR /usr/local/src/pcre-8.35/
RUN ./configure\
    && make && make install
WORKDIR /usr/local/src/
RUN wget http://nginx.org/download/nginx-1.6.2.tar.gz\
    && tar zxvf nginx-1.6.2.tar.gz
WORKDIR /usr/local/src/nginx-1.6.2
RUN ./configure --prefix=/usr/local/nginx --with-http_stub_status_module --with-http_ssl_module --with-pcre=/usr/local/src/pcre-8.35\
    && make && make install
WORKDIR /usr/local/nginx/
COPY nginx.conf ./conf/nginx.conf
COPY index.html ./html/index.html
COPY index.md ./html/html.md 
COPY cert ./conf/cert
CMD ["/usr/local/nginx/sbin/nginx","-g","daemon off;"]