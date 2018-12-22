import random
from assist import capture

class Ball(object):
    info = '球'
    def __str__(self):
        return self.info

#普通球
class PetBall(Ball):
    def __init__(self,ball_name='',capture_index = 1):
        self.ball_name = ball_name
        self.capture_index = capture_index
        #self.info = '精灵球，捕获野生精灵'

    def usePetBall(self,obj_defense):
        return capture.captureOrNot(obj_defense,self.capture_index)


#元素球
class ProptyPetBall(PetBall):
    def __init__(self,ball_name='',property=''):
        super().__init__(ball_name=ball_name,capture_index=1)
        self.property = property

    def usePetBall(self,obj_defense):
        if self.property in obj_defense.property:
            self.capture_index = 1.5
        print('球调整',self.capture_index)

        return capture.captureOrNot(obj_defense,self.capture_index)
