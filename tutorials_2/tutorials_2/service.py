# Paquete necesario para el servicio que realiza el cuadrado
from tutorials_interfaces.srv import SquareInt

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(SquareInt, 'square_int', self.square_int_callback)

    # Metodo que recibe el numero mandado por el cliente y realiza el cuadrado
    def square_int_callback(self, request, response):
        response.square = request.a*request.a
        self.get_logger().info('Incoming request\na: %d' % (request.a))

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()