from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace

# This launch file includes a set of other launch files.
# Each of these included launch files contains nodes, parameters, and possibly, nested includes, which pertain to one part of the system.

def generate_launch_description():
    launch_dir = PathJoinSubstitution([
        FindPackageShare('py_launch_tutorial'),
        'launch'
    ])

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                # This launch file starts the turtlesim_node node, which starts the turtlesim simulation, 
                # with simulation configuration parameters that are defined and passed to the nodes.
                PathJoinSubstitution([launch_dir, 'turtlesim_world_1_launch.py'])
            )
        ),
        GroupAction(
            actions=[
                PushRosNamespace('turtlesim2'),
                IncludeLaunchDescription(
                    PythonLaunchDescriptionSource(
                    # This launch file will launch the same turtlesim_node with parameter values that are loaded 
                    # directly from the YAML configuration file. 
                    # Defining arguments and parameters in YAML files make it easy to store and load a large number 
                    # of variables. It is also worth noting that this YAML file is not another launch file, it is a 
                    # configuration file for the turtlesim_node that sets parameters for the node.
                    # YAML files can be easily exported from the current ros2 param list. 
                    PathJoinSubstitution([launch_dir, 'turtlesim_world_2_launch.py'])
                    )
                ),
            ]
        ),
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource(
        #         # When we want to set the same parameters in more than one node. These nodes could have different 
        #         # namespaces or names but still have the same parameters.
        #         # Defining separate YAML files that explicitly define namespaces and node names is not efficient. 
        #         # A solution is to use wildcard characters, which act as substitutions for unknown characters in 
        #         # a text value, to apply parameters to several different nodes.
        #         # instead of creating a new configuration for the same node that use the same parameters, we can 
        #         # use wildcards syntax. /** will assign all the parameters in every node, despite differences in 
        #         # node names and namespaces.
        #         PathJoinSubstitution([launch_dir, 'turtlesim_world_3_launch.py'])
        #     )
        # ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([launch_dir, 'broadcaster_listener_launch.py'])
            ),
            # This syntax allows us to change the default goal target frame to carrot1. If you would like turtle2 
            # to follow turtle1 instead of the carrot1, just remove the line that passes the target_frame argument. 
            # This will assign target_frame its default value, which is turtle1
            launch_arguments={'target_frame': 'carrot1'}.items()
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                # This launch file will start the mimic node, which will give commands to one turtlesim to follow the other.
                # The node is designed to receive the target pose on the topic /input/pose. In our case, we want to remap 
                # the target pose from /turtle2/pose topic. Finally, we remap the /output/cmd_vel topic to /turtlesim2/turtle1/cmd_vel.
                # This way turtle1 in our turtlesim2 simulation world will follow turtle2 in our initial turtlesim world. 
                PathJoinSubstitution([launch_dir, 'mimic_launch.py'])
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                # This launch file shows the way environment variables can be called inside the launch files. Environment 
                # variables can be used to define or push namespaces for distinguishing nodes on different computers or robots.
                # If you are running the launch file where the USER environment variable is not defined (like in the ROS docker file), 
                # then you can replace the environment variable reference above with any other word of your liking.
                PathJoinSubstitution([launch_dir, 'fixed_broadcaster_launch.py'])
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                # This launch file will start the RViz with the configuration file defined in the turtle_tf2_py package. 
                # This RViz configuration will set the world frame, enable TF visualization, and start RViz with a top-down view.
                PathJoinSubstitution([launch_dir, 'turtlesim_rviz_launch.py'])
            )
        ),
        
    ])