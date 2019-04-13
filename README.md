![Image text](https://raw.github.com/gaozhangyang/our_p3dx/blob/master/Our_Project.png)

# G_robot:

提供机器人与仿真环境，不需要我们管

# G_slam

建立地图，可以用它导航，不需要我们管

# G_navigation

导航，需要我们写代码
连续输入：当前地图(有已知区域和未知区域)
连续输出:下一个想要到达的目标点坐标
注意：当机器人被墙堵住、夹住时，如何调整至正常状态

## 运行方法
1.提供仿真环境
roslaunch G_robot robot_spawn.launch

2.手动控制机器人
rosrun G_robot robot_keyboard_teleop.py

3.运行建图程序gmapping
roslaunch G_slam gmapping_demo.launch

4.导航
roslaunch G_navigation move_base.launch
