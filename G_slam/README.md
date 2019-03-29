# slam\_sim\_demo

SLAM建立地图,不需要我们写代码，提供地图用于路径规划
有几种方法可以选择，感觉Gmapping最好

### gmapping示例运行方法

首先运行gazebo仿真场景

```sh
$ roslaunch G_robot robot_spawn.launch
```

再运行建图程序gmapping

```sh
$ roslaunch G_slam gmapping_demo.launch
```


### karto示例运行方法

与gmapping启动方法类似

	roslaunch robot_sim_demo robot_spawn.launch
	roslaunch slam_sim_demo karto_demo.launch

### hector示例运行方法

	roslaunch robot_sim_demo robot_spawn.launch
	roslaunch slam_sim_demo hector_demo.launch

### cartopgrapher示例运行方法

**本demo需要安装cartographer和cartographer-ros，仅供测试使用**

	roslaunch robot_sim_demo robot_spawn.launch
	roslaunch slam_sim_demo cartographer_demo.launch