# Shell script for creating ROS 2 workspace for PX4 bridge with companion computer.
# Works with: foxy, eloquent
# ------------------------------------

## Prompt user for distribution.
echo "Distribution"
echo "* foxy"
echo "* eloquent"
read -p "Select: " ros2_distribution
echo ""

# Check if valid version.
if [ $ros2_distribution != 'foxy' ] && [ $ros2_distribution != 'eloquent' ]
then 
    echo "Distribution invalid: $ros2_distribution"
    exit 0
fi

# Create ws directiory.
mkdir -p ~/px4_ros_com_ros2/src

# Clone PX4 repos.
git clone https://github.com/PX4/px4_ros_com.git ~/px4_ros_com_ros2/src/px4_ros_com
git clone https://github.com/PX4/px4_msgs.git ~/px4_ros_com_ros2/src/px4_msgs

cd ~/px4_ros_com_ros2

# Install some neat dependencies
sudo apt update && sudo apt install -y \
    python3-rosdep \
    build-essential \
    cmake \
    python3-colcon-common-extensions \
    python3-flake8 \
    python3-pip \
    python3-pytest-cov \
    python3-setuptools \
    python3-vcstool \
    wget \
    


# Rosdep init and update.
sudo rosdep init
rosdep update --include-eol-distros

# Source ROS 2 environment and check pakcages..
if [ $ros2_distribution == 'eloquent' ] 
then 
  source /opt/ros/eloquent/setup.bash 
  rosdep install -i --from-path src --rosdistro eloquent -y
fi

if [ $ros2_distribution == 'foxy' ]
then 
  source /opt/ros/foxy/setup.bash 
  rosdep install -i --from-path src --rosdistro foxy -y
fi

# Install packaging.
sudo pip3 install packaging
sudo pip3 install pyros-genmsg

# Set one avaliable core for system when running colcon build.
cpu=$(nproc)
cpu_in_use="$(($cpu-1))"
export MAKEFLAGS="-j $cpu_in_use"

# Build packages.
colcon build --cmake-args -DCMAKE_BUILD_TYPE=RELWITHDEBINFO --executor sequential --symlink-install --event-handlers console_direct+
