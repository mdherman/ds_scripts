import matplotlib.pyplot as plt

temp = []
time = []

for line in open("templog.txt", "r"):
	lines = [i for i in line.split()]
	temp.append(int(lines[0]))
	time.append(int(lines[1]))
	
plt.title("Tempraturmåling av prosessoren til RPi CM4")
plt.xlabel("Tid i sekunder")
plt.ylabel("Temperatur i grader celsius")

plt.plot(time,temp)

plt.xlim(0,int(time[-1]))
plt.ylim(40,84)

plt.xticks(range(0,int(time[-1]),180))
plt.yticks(range(40,84,2))

plt.grid()
plt.show()
	
8
