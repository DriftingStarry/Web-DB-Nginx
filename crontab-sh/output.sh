#!/bin/bash
cd ../MariaDb/data/hddata/
if [ -f news.csv ]; then
    echo aly_dbcz1107 | sudo -S rm news.csv
fi
cd ../../../crontab-sh/
docker exec -i compose-mydb-1 mariadb -uops -pops < output.sql
