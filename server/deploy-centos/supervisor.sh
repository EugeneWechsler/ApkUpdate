easy_install supervisor
cp initd /etc/rc.d/init.d/supervisord
chmod +x /etc/rc.d/init.d/supervisord
chkconfig --add supervisord
chkconfig supervisord on
mkdir -p /var/log/supervisord