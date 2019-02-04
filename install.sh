#!/bin/sh

echo "# install dependent packages.."
sleep 5
apt update && apt install i2c-tools git python3-dev libi2c-dev python3-smbus lm-sensors hdparm python3-psutil -y

echo "# check i2c-dev module.."
sleep 5
MODULE=`cat /etc/modules | grep i2c-dev`
if [ "i2c-dev" != "$MODULE" ];then
  echo "i2c-dev" >> /etc/modules
  modprobe i2c-dev
  echo "# i2c-dev module not enabled.. enabling.."
  echo "# You need to restart ODROID-H2"
  sleep 5
fi

echo "# download LCD python code..."
sleep 5
mkdir -p /home/odroidlcd
git clone https://github.com/djjproject/odroidh2_i2c_lcd /home/odroidlcd

echo "# detect i2c ports.."
sleep 5
echo "# i2c port 1.."
i2cdetect -y -r 1
echo "# i2c port 2.."
i2cdetect -y -r 2
echo "# i2c port 3.."
i2cdetect -y -r 3
echo "# i2c port 4.."
i2cdetect -y -r 4
echo "# i2c port 5.."
i2cdetect -y -r 5
echo "# i2c port 6.."
i2cdetect -y -r 6
echo "# i2c port 7.."
i2cdetect -y -r 7
echo "# i2c port 8.."
i2cdetect -y -r 8

echo -e '# find address 27 and enter port number : \c'
read PORT
echo "# edit i2c port number.."
sleep 5
sed -i -e "s/BUS = 2/BUS = $PORT/g" /home/odroidlcd/lcddriver.py

echo "# install init.d script.."
sleep 3
cp /home/odroidlcd/odroidlcd.sh /etc/init.d/odroidlcd
chmod a+x /home/odroidlcd/run.sh
chmod a+x /etc/init.d/odroidlcd
update-rc.d odroidlcd defaults

echo "# start oroidlcd service.."
sleep 3
service odroidlcd start

echo "# installation of odroidlcd service finished.."





