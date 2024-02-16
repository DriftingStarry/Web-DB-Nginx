cd /home/dfsr/
echo yourpasswd | cp -r ./compose/MariaDb/data ./tmp/MariaDb/data
docker compose -f ./compose/docker-compose.yml down --rmi all
if [ -d lastver ]; then
    echo yourpasswd | sudo -S rm -r lastver
fi
mv compose lastver
mv tmp compose
mkdir tmp
docker compose -f ./compose/docker-compose.yml up -d