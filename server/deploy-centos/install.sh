yum -y install wget

sh ./pythonpackages.sh
sh ./nginx.sh
sh ./supervisor.sh

mkdir -p /var/www/apps/update-server
cp -fr ../src/* /var/www/apps/update-server/
cp supervisord.conf /etc/
mkdir -p /var/log/update-server
useradd update-server-user
chmod 755 /var/www/apps/update-server/
find /var/www/apps/update-server -name '*.py' -exec chmod 755 {} \;
easy_install tornado

cp -f nginx.conf /etc/nginx/nginx.conf

service supervisord restart
service nginx restart