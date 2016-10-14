use https://github.com/seanly/vagrant-centos create a vagrant box

mv /etc/salt{,.bak}
ln -s `pwd`/salt/etc /etc/salt
ln -s `pwd`/salt/roots/salt /srv/salt

