FROM mariadb:latest
ENV MARIADB_ROOT_PASSWORD=root
WORKDIR /etc/tmp
COPY create_user.sql create_user.sql
COPY create_db.sql create_db.sql
COPY init.sh /docker-entrypoint-initdb.d/init.sh