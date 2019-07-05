from  props import petballmap,propmap,drugmap,assmap
from battle import skilllistmap
import random

prize_box_dict = {
    'MAP01':{
        '1':['精灵球',1],
        '2':['小型回复药剂',1],
    },
}

def getPrizeFromBox(map_id):
    '''
    获得隐藏宝物
    :param map_id:
    :return:
    '''
    try:
        dict = prize_box_dict[map_id]
    except KeyError:
        return None

    select_box = []
    for key,item in dict.items():
        select_box.append(key)

    if len(select_box) == 0:
        return None

    select_item = random.choice(select_box)
    item_name = dict[select_item][0]
    dict[select_item][1] -= 1
    if dict[select_item][1] == 0:
        dict.pop(select_item)
    return item_name



def putPrizeToBag(item):
    if item in petballmap.petball_dict:
        petballmap.getPetBall(item)
    elif item in propmap.prop_dict:
        propmap.getProp(item)
    elif item in drugmap.drug_dict:
        drugmap.getDrug(item)
    elif item in skilllistmap.skill_dict:
        skilllistmap.getSkill(item)
    elif item in assmap.ass_dict:
        assmap.getAss(item)
    else:
        print("未知物品！")



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
            elif key in assmap.ass_dict:
                assmap.getAss(key)
            elif key in player.badge_dict:
                print("获得了 %s ！" % key)
                player.setBadge(key)
            else:
                print("未知物品！")
    #奖品清0
    dict.clear()