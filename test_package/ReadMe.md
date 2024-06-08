# Test package to start workspace

A test package to run on both the raspberry-pi5 and dev-machine to validate communication setup

## To Run

### On the pi5

source /opt/ros/humble/setup.bash <br>
**or** <br>
source ~/.devenv/humble.sh (*customised environment setup*)
- ros2 launch test_package talker_launch.py

### On the dev-machine

source /opt/ros/humble/setup.bash <br>
**or** <br>
source ~/.devenv/humble.sh (*customised environment setup*)
- ros2 launch test_package listener_launch.py
