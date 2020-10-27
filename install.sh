#!/bin/sh

# install ROS 2 Dependent Packages, TurtleBot3 Packages
apt update -y
./../ros_entrypoint.sh


#install colcon
apt install curl wget python3-colcon-common-extensions -y

#install gazebo 9
curl -sSL http://get.gazebosim.org | sh -y 
apt remove gazebo11 libgazebo11-dev -y
apt install gazebo9 libgazebo9-dev -y
apt install ros-dashing-gazebo-ros-pkgs -y

#install catographer
apt insatll ros-dashing-cartographer -y
apt install ros-dashing-cartographer-ros -y

#install navigation2
apt install ros-dashing-navigation2 -y
apt install ros-dashing-nav2-bringup -y

#install vcstool
apt install python3-vcstool -y

# Install TurtleBot3 Packages
mkdir -p ~/turtlebot3_ws/src
cd ~/turtlebot3_ws
wget https://raw.githubusercontent.com/ROBOTIS-GIT/turtlebot3/ros2/turtlebot3.repos
vcs import src < turtlebot3.repos
colcon build --symlink-install



