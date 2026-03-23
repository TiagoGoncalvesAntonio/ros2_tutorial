# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

#from std_msgs.msg import String
from tutorial_interfaces.msg import Num                        # CHANGE


# The constructor creates a subscriber with the same arguments as the publisher. 
# The topic name and message type used by the publisher and subscriber must match to allow them to communicate.
class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        # The subscriber’s constructor and callback don’t include any timer definition, 
        # because it doesn’t need one. Its callback gets called as soon as it receives a message
        self.subscription = self.create_subscription(
            # String,
            Num,                                               # CHANGE
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # The callback definition simply prints an info message to the console, along 
        # with the data it received. Recall that the publisher 
        # defines msg.data = 'Hello World: %d' % self.i
    def listener_callback(self, msg):
        # self.get_logger().info('I heard: "%s"' % msg.data)
        self.get_logger().info('I heard: "%d"' % msg.num)  # CHANGE


# The main definition is almost exactly the same, replacing the creation and 
# spinning of the publisher with the subscriber.
def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
