import sys

# Paquete necesario para el servicio que realiza el cuadrado
from tutorials_interfaces.srv import SquareInt

import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(SquareInt, 'square_int')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().error('service not available, waiting again...')
        self.req = SquareInt.Request()

    # Metodo que manda un numero al servidor
    def send_request(self, a):
        self.req.a = a
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    future = minimal_client.send_request(int(sys.argv[1]))
    rclpy.spin_until_future_complete(minimal_client, future)
    response = future.result()
    minimal_client.get_logger().info(
        'Result of square: for %d^2= %d' %
        (int(sys.argv[1]), response.square))

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()