import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class NNmodel(Node):

    def __init__(self):
        super().__init__('nnmodel')
        self.subscription_nn = self.create_subscription( Float32MultiArray,'processed_data', self.sub_feeder_msg,10)
        self.publisher_infer = self.create_publisher(Float32MultiArray, 'nnmodel_data', 10)


    def sub_feeder_msg(self, msg):
        data = msg.data
        self.get_logger().info(f"Subscribing processed data: {len(data)}")
        self.pub_nnmodel_msg(msg)

    def pub_nnmodel_msg(self,msg):
        data = msg.data
        self.publisher_infer.publish(msg)
        self.get_logger().info(f"Publishing processed data: {len(msg.data)}")

def main(args=None):
    rclpy.init(args=args)
    nn_model = NNmodel()
    
    try:
        rclpy.spin(nn_model)

    except Exception as e:
        print(f"ERROR: {e}")
        return None
    
    finally:
        nn_model.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
