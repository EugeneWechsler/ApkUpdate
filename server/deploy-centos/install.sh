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
## For qr code ##
sudo yum install gcc
sudo yum install python-devel
sudo yum install libtiff-devel libjpeg-devel libzip-devel freetype-devel lcms2-devel libwebp-devel tcl-devel tk-devel
pip install pillow
pip install qrcode

cp -f nginx.conf /etc/nginx/nginx.conf

service supervisord restart
service nginx restart