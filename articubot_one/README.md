## Articubot custom core package

### About

This package provides the custom framework for my articubot. Massive credit goes to Josh Newans for the template. 

### To build

colcon build --packages-select articubot_one

### To run

ros2 launch articubot_one launch_sim.launch.py world:="/path/to/your/workspace/articubot_one/worlds/cones.world"

- Example ***ros2 launch articubot_one launch_sim.launch.py world:="/home/username/dev/pi_dev_ws/articubot_one/worlds/cones.world***

