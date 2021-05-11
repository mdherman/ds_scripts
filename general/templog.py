import time
import os
import os.path as path

temp = 0
time_s = 0
print_time = 1

if path.exists("templog.txt"):
	os.system("rm templog.txt")

while True:
	os_temp = open("/sys/class/thermal/thermal_zone0/temp", "r")
	templog = open("templog.txt", "a")
	temp = int(int(os_temp.read())/1000)
	templog.write(str(temp) + " " + str(time_s) + "\n")
	time_s = time_s+print_time
	time.sleep(print_time)

