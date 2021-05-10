# PX4 - ROS 2 - NoPain

Shell scrips for installing FastDDS and creating a PX4 ROS2 workspace

**Tested and works with**
* Ubuntu 20.04 and ROS2 Foxy
* Ubuntu 20.04 and ROS2 Eloquent
* Ubuntu 18.04 and ROS2 Eloquent

## How to use

1. Clone repo or just download the scripts raw.
```
git clone https://github.com/mdherman/px4_ros2_nopain.git
```

2. Run installation script:
```
./fastdds_installation.sh
./ros2_px4_ws_builder.sh
```

> Note: you may need to make the script an executable using `sudo chmod +x your_script.sh`.

3. In ROS2_PX4__WS_Builder script you will be prompted to choose ROS2 distribution (foxy or eloquent).

