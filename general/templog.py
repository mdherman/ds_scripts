import time
import os

temp = 0
time = 0

templog = open("templog.txt", "a")
timelog = open("timelog.txt", "a")

try:
	while True:
		temp = os.system("/sys/class/thermal/thermal_zone0/temp")/1000
		time = time+1
		templog.write(temp)
		timelog.write(time)
		time.sleep(1)
	pass
except:
	print("Error occured.")
