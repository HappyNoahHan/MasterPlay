from assist import evolve
class EvolveStone(object):
    def __init__(self,name=None):
        if name == None:
            self.name = '未知'
        else:
            self.name = name

    def __str__(self):
        return self.name

    def use(self,player,pet,pet_id):
        '''
        使用进化石
        :return:
        '''
        if evolve.canEvolveOrNot(pet,stone=self.name):
            player.setPet(pet_id,evolve.isEvolve(pet))
            return True
        else:
            return False