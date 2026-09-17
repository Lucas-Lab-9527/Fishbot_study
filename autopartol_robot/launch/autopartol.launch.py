import os
import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # 获取 autopartol_robot 功能包的安装目录
    autopartol_robot_dir = get_package_share_directory(
        'autopartol_robot'
    )

    # 获取 patrol_config.yaml 的完整路径
    patrol_config_path = os.path.join(
        autopartol_robot_dir,
        'config',
        'partol_config.yaml'
    )

    # 创建巡逻节点
    action_node_turtle_control = launch_ros.actions.Node(
        package='autopartol_robot',
        executable='partol_node',
        parameters=[patrol_config_path]
    )

    # 创建语音节点
    action_node_patrol_client = launch_ros.actions.Node(
        package='autopartol_robot',
        executable='speaker'
    )

    # 返回 LaunchDescription
    return launch.LaunchDescription([
        action_node_turtle_control,
        action_node_patrol_client
    ])