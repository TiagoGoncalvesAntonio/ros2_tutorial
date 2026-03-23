# ROS 2 Humble Tutorial Workspace

This repository contains a complete ROS 2 Humble workspace developed while following the official tutorials, progressing from beginner to advanced concepts.

The workspace consolidates multiple packages covering core ROS 2 functionalities including communication (publishers/subscribers, services), parameters, actions, launch files, TF2, pluginlib, and URDF-based robot description.

---

## Overview

This repository serves as:

* A structured learning environment for ROS 2 Humble
* A reference implementation of official tutorials
* A consolidated workspace with both C++ and Python examples

All packages are located in the `src/` directory of a standard ROS 2 workspace.

---

## Package Structure

### Communication (Publishers, Subscribers, Services)

* `cpp_pubsub` — Publisher/Subscriber (C++)
* `py_pubsub` — Publisher/Subscriber (Python)
* `cpp_srvcli` — Service/Client (C++)
* `py_srvcli` — Service/Client (Python)

---

### Parameters

* `cpp_parameters` — Parameter usage (C++)
* `python_parameters` — Parameter usage (Python)
* `cpp_parameter_event_handler` — Parameter event monitoring

---

### Actions

* `action_tutorials_cpp` — Actions (C++)
* `action_tutorials_py` — Actions (Python)
* `action_tutorials_interfaces` — Custom action definitions

---

### Interfaces

* `tutorial_interfaces` — Custom message/service definitions
* `more_interfaces` — Additional interface examples

---

### Launch System

* `cpp_launch_example`
* `py_launch_example`
* `cpp_launch_tutorial`
* `py_launch_tutorial`

---

### TF2 (Transforms)

* `learning_tf2_cpp`
* `learning_tf2_py`

---

### Pluginlib / Polymorphism

* `polygon_base` — Base polygon interface
* `polygon_plugins` — Plugin implementations

---

### URDF

* `urdf_tutorial_r2d2` — Robot description example

---

### Custom / Practice Packages

* `my_package` — Custom experiments in C++
* `my_package_py` — Custom experiments in Python
* `ros_tutorials` — General tutorial workspace content

---

## Requirements

* Ubuntu 22.04
* ROS 2 Humble
* Python 3
* `colcon`

---

## Build Instructions

From the workspace root:

```bash
cd ~/projects/ros2_ws
colcon build
```

---

## Setup Environment

```bash
source /opt/ros/humble/setup.bash
source ~/projects/ros2_ws/install/setup.bash
```

---

## Running Examples

### C++

```bash
ros2 run cpp_pubsub talker
ros2 run cpp_pubsub listener
```

### Python

```bash
ros2 run py_pubsub talker
ros2 run py_pubsub listener
```

---

## Development Workflow

Build specific packages:

```bash
colcon build --packages-select cpp_pubsub py_pubsub
```

Re-source after building:

```bash
source ~/projects/ros2_ws/install/setup.bash
```

---

## Notes

* This repository follows the ROS 2 Humble tutorial progression
* Packages include both direct tutorial implementations and small modifications
* Intended for learning, experimentation, and reference

---

## Author

Tiago Gonçalves António
