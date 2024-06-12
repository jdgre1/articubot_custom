import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

def generate_launch_description():

    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='articubot_one' #<--- CHANGE ME
    pkg_path = os.path.join(get_package_share_directory('articubot_one'))
    world_path = os.path.join(pkg_path, 'worlds', 'cones.world')

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true',
                                       'world':world_path}.items()
    )

        # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]))

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'articubot_one'],
                        output='screen')
    
    navigation = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory(package_name),'launch','navigation_launch.launch.py'
            )]), launch_arguments={'use_sim_time': 'true',
                                    'map': './src/robot/maps/map_save.yaml'}.items()
)
    
        # Launch them all!
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        # navigation,
    ])