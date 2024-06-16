## Articubot custom core package

### About

This package provides the custom framework for my articubot. Massive credit goes to Josh Newans for the template. 

### To build

colcon build --packages-select articubot_custom

### To run

ros2 launch articubot_custom launch_sim.launch.py  ***default world saved in launch file***

- Example ***ros2 launch articubot_custom launch_sim.launch.py world:="/home/username/dev/pi_dev_ws/src/articubot_custom/worlds/cones.world***

### Slam

ros2 launch slam_toolbox online_async_launch.py slam_params_file:=./src/articubot_custom/config/mapper_params_online_async.yaml use_sim_time:=true


### Nav2

#### Terminal 1
ros2 launch articubot_custom launch_sim.launch.py
#### Terminal 2
ros2 run nav2_map_server map_server --ros-args -p yaml_filename:=./src/articubot_custom/config/my_map_save.yaml -p use_sim_time:=true
#### Terminal 3
ros2 run nav2_amcl amcl use_sim_time 
#### Terminal 4
ros2 run nav2_util lifecycle_bringup map_server
ros2 run nav2_util lifecycle_bringup amcl


### Nav2 edited
ros2 launch articubot_custom launch_sim.launch.py use_sim_time:=true
ros2 launch articubot_custom online_async_launch.py
