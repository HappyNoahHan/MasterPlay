from  props import petballmap,propmap,drugmap
from battle import skilllistmap
def getPrize(player,dict):
    for key,value in dict.items():
        if key == 'money':
            print("获得 %s  金钱！" % value)
            player.money += value
        else:
            if key in petballmap.petball_dict:
                petballmap.getPetBall(key)
            elif key in propmap.prop_dict:
                propmap.getProp(key)
            elif key in drugmap.drug_dict:
                drugmap.getDrug(key)
            elif key in skilllistmap.skill_dict:
                skilllistmap.getSkill(key)
            else:
                print("未知物品！")