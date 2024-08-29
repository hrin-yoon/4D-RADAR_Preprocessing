import os
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray


class PsudoRadar(Node):

    def __init__(self, data_dir):
        super().__init__('psudoRadar_node')
        self.data_dir = data_dir 
        self.data_index = 0  
        self.publisher_ = self.create_publisher(Float32MultiArray, 'radar_data', 10)
        self.timer = self.create_timer(1.0, self.publish_data)  

    def data_simple_loader(self, path):
        try:
            data = np.load(path) 
            return data
        except Exception as e:
            self.get_logger().error(f"Failed to load data from {path}: {e}")
            return None

    def publish_data(self):
        if self.data_index >= len(self.data_dir):
            self.get_logger().info("All data has been published.")
            rclpy.shutdown()
            return

        current_path = self.data_dir[self.data_index]
        data = self.data_simple_loader(current_path)

        if data is not None:
            msg = Float32MultiArray()
            msg.data = data.flatten().tolist()  
            self.publisher_.publish(msg)
            self.get_logger().info(f'Published radar data from: {current_path} with shape {data.shape}')
        
        self.data_index += 1  


def main(args=None):

    rclpy.init(args=args)

    data_dir = os.listdir('DATA/rtnh_wider_1p_1/15')
    data_dir = np.sort(data_dir)
    data_dir = [f"DATA/rtnh_wider_1p_1/15/{filename}" for filename in data_dir]

    psudo_radar_node = PsudoRadar(data_dir)

    try:
        rclpy.spin(psudo_radar_node)
    except Exception as e:
        psudo_radar_node.get_logger().error(f"An error occurred: {e}")
    finally:
        psudo_radar_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
