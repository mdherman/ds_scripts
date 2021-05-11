import matplotlib.pyplot as plt

temp = []
time = []

for line in open("templog.txt", "r"):
	lines = [i for i in line.split()]
	temp.append(lines[0])
	time.append(lines[1])
	
plt.title("Tempraturmåling av prosessoren til RPi CM4")
plt.xlabel("Tid")
plt.ylabel("Temperatur")
plt.plot(time,temp)
plt.xticks(range(0,int(time[-1]),10))

plt.grid()
plt.show()
	

