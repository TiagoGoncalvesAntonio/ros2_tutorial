# The import statements at the top are used to import the package dependencies.
import rclpy
import rclpy.node

# The next piece of code creates the class and the constructor. 
class MinimalParam(rclpy.node.Node):
    def __init__(self):
        # Name the node.
        super().__init__('minimal_param_node')
        
        from rcl_interfaces.msg import ParameterDescriptor
        my_parameter_descriptor = ParameterDescriptor(description='This parameter is mine!')
        
        # The line self.declare_parameter('my_parameter', 'world') of the 
        # constructor creates a parameter with the name my_parameter and a default value of world. 
        # The parameter type is inferred from the default value, so in this case it would be set to a string type. 
        self.declare_parameter('my_parameter', 'world', my_parameter_descriptor)

        # Next the timer is initialized with a period of 1, which causes the timer_callback function to be executed once a second
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        # The first line of our timer_callback function gets the parameter my_parameter from the node, and stores it in my_param.
        my_param = self.get_parameter('my_parameter').get_parameter_value().string_value

        # Next the get_logger function ensures the event is logged.
        self.get_logger().info('Hello %s!' % my_param)

        my_new_param = rclpy.parameter.Parameter(
            'my_parameter',
            rclpy.Parameter.Type.STRING,
            'world'
        )
        all_new_parameters = [my_new_param]
        
        # The set_parameters function then sets the parameter my_parameter back to the default string value world.
        # In the case that the user changed the parameter externally, this ensures it is always reset back to the original.
        self.set_parameters(all_new_parameters)

# Here ROS 2 is initialized, an instance of the MinimalParam class is constructed, and rclpy.spin starts processing data from the node.
def main():
    rclpy.init()
    node = MinimalParam()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
    