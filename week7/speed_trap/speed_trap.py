import random

class SpeedTrap:
    speed = 0
    def __init__(self):
        self.speed = 0

    def get_speed(self):
        return self.speed * 1.60934

    def set_speed(self, speed):
        if speed >= 0:
            self.speed = speed
        else:
            print("Invalid speed value received")

    def measure(self):
        self.speed = random.random() * 50 * 0.621371