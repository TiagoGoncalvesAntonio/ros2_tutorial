import time
import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci


# Defines a class FibonacciActionServer that is a subclass of Node
class FibonacciActionServer(Node):

    def __init__(self):
        # The class is initialized by calling the Node constructor, naming our node fibonacci_action_server
        super().__init__('fibonacci_action_server')
        # In the constructor we also instantiate a new action server
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback)

    # This callback must return a result message for the action type.
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        feedback_msg = Fibonacci.Feedback()
        feedback_msg.partial_sequence = [0, 1]
        
        for i in range(1, goal_handle.request.order):
            feedback_msg.partial_sequence.append(
                feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

                
        goal_handle.succeed()

        result = Fibonacci.Result()
        result.sequence = feedback_msg.partial_sequence
                
        return result

    # An action server requires 4 arguments: 
    #   A ROS 2 node to add the action client to: self. 
    #   The type of the action: Fibonacci (imported in line 5). 
    #   The action name: 'fibonacci'. 
    #   A callback function for executing accepted goals: self.execute_callback. This callback must return a result message for the action type.  

def main(args=None):
    rclpy.init(args=args)

    fibonacci_action_server = FibonacciActionServer()

    rclpy.spin(fibonacci_action_server)


if __name__ == '__main__':
    main()
