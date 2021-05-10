import getpass
import os
import time
username = getpass.getuser()

try:
    # Reading system_setup file
    system_setup = open("/home/" + username + "/drone_setup.txt")
    for line in system_setup:
        if "use: " in line:
            space = line.find(" ", 0, len(line))
            use = int(line[space:])
        elif "drone: " in line:
            space = line.find(" ", 0, len(line))
            drone = int(line[space:])

    # Checking if drone and use is within range
    if (drone in range(1,10) and use in range(1,10)):
        string = "use_0" + str(use) + "/drone_0" + str(drone)
    elif (use >= 10 and drone == 10):
        string = "use_" + str(use) + "/drone_" + str(drone)
    elif (use >= 10 and drone in range(1,10)):
        string = "use_" + str(use) + "/drone_0" + str(drone)
    elif (drone == 10 and use in range(1,10)):
        string = "use_0" + str(use) + "/drone_" + str(drone)
    else:
        string = "none"

    # Starting ROS2 node and micrortps_agent if drone and use is in range
    if (string != "none"):
        os.system("micrortps_agent start -t UART -b 921600 -d /dev/ttyS0 -n '" + string + "' &")
        time.sleep(10)
        os.system("ros2 run ds_ros2_drone_pkg px4_offboard_control --ros-args -r __ns:=/" + string)
    else:
        print("Something went wrong...")
        print("Have you remebered to select drone- and use nr in ~/drone_setup.txt?")
except:
    print("Something went wrong...")
    print("Have you remebered to select drone- and use nr in ~/drone_setup.txt?")
