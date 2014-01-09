yum -y install wget

sh ./nginx.sh
sh ./supervisor.sh

mkdir -p /var/www/apps/update-server/packages
cp update-server.py /var/www/apps/update-server/
cp supervisord.conf /var/etc/supervisord.conf
useradd update-server-user
chmod 755 /var/www/apps/update-server/

service supervisord restart
service nginx restart