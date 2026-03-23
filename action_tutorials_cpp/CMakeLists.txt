cmake_minimum_required(VERSION 3.8)
project(action_tutorials_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(action_tutorials_interfaces REQUIRED)

include_directories(include)

add_library(action_server SHARED
  src/fibonacci_action_server.cpp
)
target_compile_definitions(action_server
  PRIVATE "ACTION_TUTORIALS_CPP_BUILDING_DLL")
ament_target_dependencies(action_server
  rclcpp
  rclcpp_action
  rclcpp_components
  action_tutorials_interfaces
)
rclcpp_components_register_node(action_server
  PLUGIN "action_tutorials_cpp::FibonacciActionServer"
  EXECUTABLE fibonacci_action_server
)

add_library(action_client SHARED
  src/fibonacci_action_client.cpp
)
target_compile_definitions(action_client
  PRIVATE "ACTION_TUTORIALS_CPP_BUILDING_DLL")
ament_target_dependencies(action_client
  rclcpp
  rclcpp_action
  rclcpp_components
  action_tutorials_interfaces
)
rclcpp_components_register_node(action_client
  PLUGIN "action_tutorials_cpp::FibonacciActionClient"
  EXECUTABLE fibonacci_action_client
)

install(
  DIRECTORY include/
  DESTINATION include
)

install(
  TARGETS action_server action_client
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()