cd /tmp
wget http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm
rpm -ivh nginx-release-centos-6-0.el6.ngx.noarch.rpm
cd ..

yum install nginx
chkconfig nginx on
iptables -I INPUT 1 -p tcp -m state --state NEW -m tcp --dport 80 -j ACCEPT
service iptables save
