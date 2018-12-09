# import modules
import lcddriver as lcd
import os
import psutil as ps
from time import time
from time import sleep
from datetime import datetime

# network status get function
def get_bytes(t, iface='enp2s0'):
    with open('/sys/class/net/' + iface + '/statistics/' + t + '_bytes', 'r') as f:
        data = f.read();
        return int(data)

# load lcd
lcd = lcd.lcd()

# test code
#lcd.display_string("11111111111111111111222222222222222222223333333333333333333344444444444444444444", 1)

# get hostname
#hostname=str(os.popen('hostname').readline())[:-1]

lcd.display_string("####################",1)
lcd.display_string("WELCOME TO ODROID H2",2)
lcd.display_string("LCD SERVICE STARTED.",3)
lcd.display_string("####################",4)


sleep(10)



while True:

  # foot powered coding
  #cpuUsage=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
  #tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
  #percentMem=str(round(used_m/tot_m))

  # read hdd state from hdparm
  hddstate=str(os.popen('hdparm -C /dev/sda | grep state | cut -f 2 -d :').readline())[2:][:-1]

  if hddstate=="standby":
    hddstr="SLEEP"
  else :
    hddstr="WAKE"

  # line 1 print (hddstate, friendly name)
  lcd.display_string("HDD:"+hddstr.rjust(5)+"  ODROID-H2", 1)

  # line 2 print (cpu, memory)
  # use psutil to get CPU usage and Memory Usage
  lcd.display_string("CPU:"+str(ps.cpu_percent()).rjust(4)+"%"+"  "+"MEM:"+str(ps.virtual_memory()[2]).rjust(4)+"%", 2)

  # get network speed for 1sec
  tx1 = get_bytes('tx')
  rx1 = get_bytes('rx')
  sleep(1)
  tx2 = get_bytes('tx')
  rx2 = get_bytes('rx')
  tx_speed = (tx2 - tx1)/1000000.0
  rx_speed = (rx2 - rx1)/1000000.0

  # line 3 print (network speed)
  # bps -> mpbs (*8)
  lcd.display_string("TX: "+str(round(tx_speed*8)).zfill(3)+" RX: "+str(round(rx_speed*8)).zfill(3)+" mbps", 3)

  # line 4 print (cputemp, date, time)
  # use lm-sensors to get cpu temp / get time data from python internal method
  dateString = datetime.now().strftime('%m-%d')
  timeString = datetime.now().strftime('%H:%M')
  lcd.display_string("TEMP:"+os.popen('sensors | grep "temp1:" | cut -d+ -f2 | cut -c1-2').read()[:-1]+"C "+dateString+" "+timeString, 4)

  # line 4 print (cputemp, uptime)
  # use /proc/uptime and python divmod method
  #uptime=os.popen('cat /proc/uptime | cut -d " " -f1').read()
  #uptimeDay=divmod(float(uptime),86400)
  #uptimeHour=divmod(uptimeDay[1],3600)
  #uptimeMin=divmod(uptimeHour[1],60)
  #uptimeString=str(int(uptimeDay[0]))+"D:"+str(int(uptimeHour[0]))+"H:"+str(int(uptimeMin[0]))+"M"
  #lcd.display_string("TEMP:"+os.popen('sensors | grep "temp1:" | cut -d+ -f2 | cut -c1-2').read()[:-1]+"C "+uptimeString.zfill(3), 4)


  # sleep(1)
