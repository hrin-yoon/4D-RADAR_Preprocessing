import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class Preprocessing(Node):
    cont = 0
    def __init__(self):
        super().__init__('data_feeder')
        
        self.subscription_radar = self.create_subscription( Float32MultiArray,'radar_data', self.sub_radar_msg, 10)
        self.publisher_feeder = self.create_publisher(Float32MultiArray, 'processed_data', 10)

    def sub_radar_msg(self, msg): 
        data = msg.data
        self.get_logger().info(f"Subscribing processed data: {len(data)}")
        self.pub_model_msg(msg)

    def pub_model_msg(self, msg): 
        data = msg.data
        self.publisher_feeder.publish(msg)
        self.get_logger().info(f"Publishing processed data: {len(msg.data)}")

def main(args=None):

    rclpy.init(args=args) 
    data_feeder = Preprocessing() 
    
    try:
        rclpy.spin(data_feeder)

    except Exception as e:
        print(f"ERROR: {e}")
        return None
    
    finally:
        data_feeder.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
