import lcddriver as lcd
import os
import psutil as ps
from time import time
from time import sleep
from datetime import datetime

def get_bytes(t, iface='enp2s0'):
    with open('/sys/class/net/' + iface + '/statistics/' + t + '_bytes', 'r') as f:
        data = f.read();
        return int(data)


lcd = lcd.lcd()

#lcd.display_string("11111111111111111111222222222222222222223333333333333333333344444444444444444444", 1)

hostname=str(os.popen('hostname').readline())[:-1]



while True:
#  cpuUsage=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
#  tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
#  percentMem=str(round(used_m/tot_m))

  hddstate=str(os.popen('hdparm -C /dev/sda | grep state | cut -f 2 -d :').readline())[2:][:-1]
#  print(hddstate)
  if hddstate=="standby":
    hddstr="SLEEP"
  else :
    hddstr="WAKE"

  lcd.display_string("HDD:"+hddstr.rjust(5)+"  ODROID-H2", 1)
#  lcd.display_string("                    ",2)
  lcd.display_string("CPU:"+str(ps.cpu_percent()).rjust(4)+"%"+"  "+"MEM:"+str(ps.virtual_memory()[2]).rjust(4)+"%", 2)

  dateString = datetime.now().strftime('%m-%d')
  timeString = datetime.now().strftime('%H:%M')


  tx1 = get_bytes('tx')
  rx1 = get_bytes('rx')

  sleep(1)

  tx2 = get_bytes('tx')
  rx2 = get_bytes('rx')

  tx_speed = round((tx2 - tx1)/1000000.0)
  rx_speed = round((rx2 - rx1)/1000000.0)

  lcd.display_string("TX: "+str(tx_speed*8).zfill(3)+" RX: "+str(rx_speed*8).zfill(3)+" mbps", 3)
  lcd.display_string("TEMP:"+os.popen('sensors | grep "temp1:" | cut -d+ -f2 | cut -c1-2').read()[:-1]+"C "+dateString+" "+timeString, 4)
#  sleep(1)
