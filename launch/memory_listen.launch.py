import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    memory_pub = launch_ros.actions.Node(
        package='mypkg' ,
        executable='memory_pub',
        )

    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen'
        )

    return launch.LaunchDescription([memory_pub, listener])
