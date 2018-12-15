import random
from assist import capture

class Ball(object):
    info = '球'
    def __str__(self):
        return self.info

class PetBall(Ball):
    def __init__(self):
        self.ball_name = '精灵球'
        self.capture_index = 1
        self.info = '精灵球，捕获野生精灵'

    def usePetBall(self,obj_defense):
        return capture.captureOrNot(obj_defense,self.capture_index)