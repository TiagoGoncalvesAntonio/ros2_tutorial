# The first import statement imports the AddTwoInts service type from the example_interfaces package. 
# from example_interfaces.srv import AddTwoInts
from tutorial_interfaces.srv import AddThreeInts                                                           # CHANGE
# The following import statement imports the ROS 2 Python client library, and specifically the Node class.
import rclpy
from rclpy.node import Node

# The MinimalService class constructor initializes the node with the name minimal_service
class MinimalService(Node):
# Then, it creates a service and defines the type, name, and callback.
    def __init__(self):
        super().__init__('minimal_service')
        # self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        self.srv = self.create_service(AddThreeInts, 'add_three_ints', self.add_three_ints_callback)       # CHANGE

    # def add_two_ints_callback(self, request, response):
    def add_three_ints_callback(self, request, response):
        # response.sum = request.a + request.b
        # self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))
        response.sum = request.a + request.b + request.c                                                   # CHANGE
        self.get_logger().info('Incoming request\na: %d b: %d c: %d' % (request.a, request.b, request.c))  # CHANGE

        return response

# The main class initializes the ROS 2 Python client library, instantiates the MinimalService class to create 
# the service node and spins the node to handle callbacks.
def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()