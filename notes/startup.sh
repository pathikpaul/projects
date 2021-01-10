#/bin/bash
groupadd hadoop
useradd hadoop -g hadoop
echo -e "hadoop\nhadoop"|passwd hadoop
echo "hadoop  ALL=(ALL)       ALL" >> /etc/sudoers
sed -i.bak 's/127.0.0.1	hdpmc/\#127.0.0.1	hdpmc/g'   /etc/hosts
cat <<EENNDD >> /etc/hosts
192.168.77.10   hdpmc1  hdpmc1
192.168.77.11   hdpmc2  hdpmc2
192.168.77.12   hdpmc3  hdpmc3
EENNDD
