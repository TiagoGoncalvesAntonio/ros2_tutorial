cmake_minimum_required(VERSION 3.8)
project(cpp_srvcli)

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
# find_package(example_interfaces REQUIRED)
find_package(tutorial_interfaces REQUIRED)         # CHANGE

# Add the following code block to CMakeLists.txt just below the dependencies to create an executable named server/client:
add_executable(server src/add_two_ints_server.cpp)
# ament_target_dependencies(server rclcpp example_interfaces)
ament_target_dependencies(server rclcpp tutorial_interfaces)                      # CHANGE

add_executable(client src/add_two_ints_client.cpp)
# ament_target_dependencies(client rclcpp example_interfaces)
ament_target_dependencies(client rclcpp tutorial_interfaces)                      # CHANGE

# So ros2 run can find the executable, add the following lines to the end of the file, right before ament_package():
install(TARGETS
    server
    client
  DESTINATION lib/${PROJECT_NAME})


ament_package()
