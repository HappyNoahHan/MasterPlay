from pets import fire,fly

class Player(object):
    def __init__(self):
        self.name = '小智'


    master_pet = fire.Charmander(level=5)

    pet_list = {
        '1': master_pet,
        '2': fire.Charmeleon(level=15),
        '3': fire.Charmeleon(level=20),
    }

    #获得经验的度 1满 0.5一半
    #exp_status = 1

    #战斗是否交换精灵
    change_pet = False

    def setPet(self,key,value):
        self.pet_list[key] = value


