class Weather():
    def __init__(self,name=None,code = None,turns=2):
        self.name = name
        self.code = code
        self.turns = turns
        self._max_turns = self.turns

    def weatherEffect(self,obj):
        return True

    def propUpOrDown(self,obj):
        return True

class Sandstorm(Weather):
    def __init__(self):
        super().__init__(name='沙暴',code='W004',turns=10)

    def weatherEffect(self,obj):
        for prop in obj.prop:
            if prop in ['ground','rock','steel']:
                return True
        obj.health -= round(obj._max_health / 16)
        print("因%s 天气损失了 %s HP！" % (self.name,round(obj._max_health / 16)))

    def propUpOrDown(self,obj):
        for prop in obj.prop:
            if prop in ['rock']:
                obj.tmp_spell_defense += round(obj.spell_defense * 0.5)