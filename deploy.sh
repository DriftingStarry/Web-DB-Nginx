cd /home/dfsr/
docker compose -f ./compose/docker-compose.yml down --rmi all
cp -r ./compose/MariaDb/data ./tmp/MariaDb/data
if [ -d lastver ]; then
    echo yourpasswd | sudo -S rm -r lastver
fi
mv compose lastver
mv tmp compose
mkdir tmp
docker compose -f ./compose/docker-compose.yml up -d