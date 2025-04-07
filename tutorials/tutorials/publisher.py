import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Paquete necesario para la posicion
from sensor_msgs.msg import NavSatFix

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        self.publisher = self.create_publisher(NavSatFix, 'topic', 10)
        self.timer = self.create_timer(1.0, self.publish_message)

    # Metodo que publica en el topic la posicion
    def publish_message(self):
        msg = NavSatFix()
        msg.latitude = 40.0 
        msg.longitude = -8.0
        msg.altitude = 100.0
        self.publisher.publish(msg)
        self.get_logger().debug('Obteniendo coordenadas GPS')
        self.get_logger().info(f'Publicando GPS -> Lat: {msg.latitude}, Lon: {msg.longitude}, Alt: {msg.altitude}')
        self.get_logger().warn('Precision de GPS baja')

def main(args=None):
    rclpy.init(args=args)
    node = SimplePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
