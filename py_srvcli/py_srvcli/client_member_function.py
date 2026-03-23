# As with the service code, we first import the necessary libraries
import sys
# from example_interfaces.srv import AddTwoInts
from tutorial_interfaces.srv import AddThreeInts                            # CHANGE
import rclpy
from rclpy.node import Node

# The MinimalClientAsync class constructor initializes the node with the name minimal_client_async.
class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        # The constructor definition creates a client with the same type and name as the service node.
        # The type and name must match for the client and service to be able to communicate.
        # self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        self.cli = self.create_client(AddThreeInts, 'add_three_ints')       # CHANGE
        # The while loop in the constructor checks if a service matching the type and name of the client is available once a second.
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        # Finally it creates a new AddTwoInts request object.
        # self.req = AddTwoInts.Request()
        self.req = AddThreeInts.Request()                                   # CHANGE
        
    # Below the constructor is the send_request method, which will send the request and spin until it receives the response or fails.
    def send_request(self):
        self.req.a = int(sys.argv[1])
        self.req.b = int(sys.argv[2])
        self.req.c = int(sys.argv[3])                                       # CHANGE
        self.future = self.cli.call_async(self.req)

# Finally we have the main method, which constructs a MinimalClientAsync object, sends the request using the passed-in 
# command-line arguments, calls rclpy.spin_until_future_complete to wait for the result, and logs the results.
def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClientAsync()
    minimal_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                minimal_client.get_logger().info(
                    'Result of add_three_ints: for %d + %d + %d = %d' %                                # CHANGE
                    (minimal_client.req.a, minimal_client.req.b, minimal_client.req.c, response.sum))  # CHANGE
            break

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()