import time
from assist import capture

class Ball(object):
    info = '球'
    def __str__(self):
        return self.info

#普通球
class PetBall(Ball):
    def __init__(self,show_name='',capture_index = 1):
        self.show_name = show_name
        self.capture_index = capture_index
        #self.info = '精灵球，捕获野生精灵'

    def usePetBall(self,obj_defense):
        print("使用 %s ！" % self.show_name)
        time.sleep(3)
        return capture.captureOrNot(obj_defense,self.capture_index)


#元素球
class ProptyPetBall(PetBall):
    def __init__(self,show_name='',property=''):
        super().__init__(show_name=show_name,capture_index=1)
        self.property = property

    def usePetBall(self,obj_defense):
        print("使用 %s ！" % self.show_name)
        time.sleep(3)
        if self.property in obj_defense.property:
            self.capture_index = 1.5
        print('球调整',self.capture_index)

        return capture.captureOrNot(obj_defense,self.capture_index)

#大师球 100%成功
class MasterPetBall(Ball):
    def __init__(self):
        self.show_name = '大师球'

    def usePetBall(self,obj_defense):
        print("使用 %s ！" % self.show_name)
        time.sleep(3)
        if obj_defense.has_captured != False:
            print("无法捕捉有主的精灵！")
            return False
        else:
            print("捕获 %s 成功！" % obj_defense.name)
            return True
