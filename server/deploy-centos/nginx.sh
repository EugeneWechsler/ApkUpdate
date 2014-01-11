cd /tmp
wget http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm
rpm -ivh nginx-release-centos-6-0.el6.ngx.noarch.rpm
cd ..

yum install nginx
chkconfig nginx on
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
service iptables save

