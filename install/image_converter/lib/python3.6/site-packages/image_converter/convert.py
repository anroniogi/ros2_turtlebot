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

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class MinimalSubscriber(Node):

    to_convert = 'rgb8'

    """
    변환가능한 encoding type
    mono8: CV_8UC1, grayscale image
    mono16: CV_16UC1, 16-bit grayscale image
    bgr8: CV_8UC3, color image with blue-green-red color order
    rgb8: CV_8UC3, color image with red-green-blue color order
    bgra8: CV_8UC4, BGR color image with an alpha channel
    rgba8: CV_8UC4, RGB color image with an alpha channel
    """

    """
    image라는 이름의 topic subscribe
    """

    def __init__(self):
        super().__init__('minimal_subscriber')
        print("write encoding type to convert (default : bgr8)")
        self.to_convert = input()
        if self.to_convert == "":
            self.to_convert = "bgr8"
        self.subscription = self.create_subscription(
            Image,
            'image',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning


    # subscriber가 받은 image message를 encoding에 맞게 numpy array로 변환하는 함수
    def image_convert(self, image_msg):
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(image_msg, desired_encoding=self.to_convert)
        
        return cv_image

    # subscriber callback, msg:image message
    # data가 변환된 numpy array
    def listener_callback(self, msg):
        data = self.image_convert(msg)
        




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
