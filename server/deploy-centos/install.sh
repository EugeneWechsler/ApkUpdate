cd deploy-centos
yum -y install wget

sh ./pythonpackages.sh
sh ./nginx.sh
sh ./supervisor.sh

mkdir -p /var/www/apps/update-server
cp -r ../src/* /var/www/apps/update-server/
cp supervisord.conf /var/etc/
mkdir -p /var/log/update-server
useradd update-server-user
chmod 744 /var/www/apps/update-server/
find /var/www/apps/update-server -name '*.py' -exec chmod 755 {} \;
easy_install tornado

service supervisord restart
service nginx restart