#!/bin/bash
export ROS_MASTER_URI=http://192.168.1.183:11311
export ROS_IP=192.168.1.183

cd
cd catkin_ws/src/lidarbot/launch
roslaunch lidarbot.launch

