import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 1)
        self.timer_ = self.create_timer(0.1, self.move_turtle)
        self.twist_msg_ = Twist()
        self.timer = 0
        
    def first_movement(self):
        self.twist_msg_.linear.y = 4.0
        self.twist_msg_.linear.x = 2.0
        self.publisher_.publish(self.twist_msg_)
        self.timer += 1
        
    def second_movement(self):
        self.twist_msg_.linear.y = -4.5
        self.twist_msg_.linear.x = 1.0
        self.publisher_.publish(self.twist_msg_)
        self.timer += 1
        
    def third_movement(self):
        self.twist_msg_.linear.y = -4.0
        self.twist_msg_.linear.x = -2.0
        self.publisher_.publish(self.twist_msg_)
        self.timer += 1
        
    def fourth_movement(self):
        self.twist_msg_.linear.y = 2.0
        self.twist_msg_.linear.x = -0.5
        self.publisher_.publish(self.twist_msg_)
        self.timer += 1

    def diamond(self):
        if (self.timer < 10):
            self.first_movement()
            
        if (self.timer >= 10 and self.timer < 20):
            self.second_movement()
            
        if (self.timer >= 20 and self.timer < 30):
            self.third_movement()
        
        if (self.timer >= 30 and self.timer < 40):
            self.fourth_movement()

def main():
    print("The turtle is moving")
    rclpy.init()
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("The turtle stopped")
        print(e)

