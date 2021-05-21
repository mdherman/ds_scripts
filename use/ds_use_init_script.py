import os
import sys

try:
    # Get current file path
    file_path = sys.path[0]

    # Reading use_init file
    system_setup = open(file_path + "/use_init.txt")
    for line in system_setup:
        if "use: " in line:
            space = line.find(" ", 0, len(line))
            use_number = int(line[space:])
            use_namespace = str(use_number)

    # Source ros 2
    os.system("source /opt/ros/foxy/setup.bash")
    os.system("source /home/ubuntu/dronesverm_ws/install/local_setup.bash")

    if (use_number > 10):
        os.system("ros2 run ds_ros2_use use_transfer --ros-args -r __ns:=/use_" + use_namespace)
    elif (use_number in range(1,10)):
        os.system("ros2 run ds_ros2_use use_transfer --ros-args -r __ns:=/use_0" + use_namespace)
    else:
        print("Invalid number of use..")
except:
    print("Could not read 'use_init.txt'..")
