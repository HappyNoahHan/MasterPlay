'''
    进化表
    继承  技能列表  已领悟技能
'''

from pets import fire,rock,poison,skilltree,fly,wood,water,electric,insect,normal,ground,fairy
from assist import  show
from battle import learnskill
import time

evolve_dict={
    '妙蛙种子': [wood.Ivysaur,16,'level_up'],
    '妙蛙草': [wood.Venusaur,36,'level_up'],
    '小火龙': [fire.Charmeleon,16,'level_up'],
    '火恐龙': [fire.Charizard,36,'level_up'],
    '杰尼龟': [water.Wartortle,16,'level_up'],
    '卡咪龟': [water.Blastoise,36,'level_up'],
    '绿毛虫': [insect.Metapod,7,'level_up'],
    '铁甲蛹': [insect.Butterfree,10,'level_up'],
    '独角虫': [insect.Kakuna,7,'level_up'],
    '铁壳蛹': [insect.Beedrill,10,'level_up'],
    '波波': [fly.Pidgeotto, 18, 'level_up'],
    '比比鸟': [fly.Pidgeot, 36, 'level_up'],
    '小拉达': [normal.Raticate,20,'level_up'],
    '烈雀': [fly.Fearow, 20, 'level_up'],
    '阿柏蛇': [poison.Arbok, 22, 'level_up'],
    '皮卡丘': [electric.Raichu,'雷之闪','stone_up'],
    '穿山鼠': [ground.Sandslash,22,'level_up'],
    '尼多兰': [poison.Nidorina,16,'level_up'],
    '尼多娜': [poison.Nidoqueen,'月之露','stone_up'],
    '尼多朗': [poison.Nidorino,16,'level_up'],
    '尼多王': [poison.Nidoking,'月之露','stone_up'],
    '皮皮': [fairy.Clefable,'月之露','stone_up'],
    '六尾': [fire.Ninetales,'火之焰','stone_up'],
    '胖丁': [fairy.Wigglytuff,'月之露','stone_up'],
    '超音蝠': [poison.Golbat,22,'level_up'],
    '走路草': [wood.Gloom,21,'level_up'],
    '臭臭花': [wood.Vileplume,'叶之翠','stone_up'],
    '派拉斯': [insect.Parasect,24,'level_up'],
    '毛球': [insect.Venomoth,31,'level_up'],
    '地鼠': [ground.Dugtrio,26,'level_up'],
    '喵喵': [normal.Persian,28,'level_up'],
    '喇叭芽': [wood.Weepinbell,21,'level_up'],
    '口呆花': [wood.Victreebel,'叶之翠','stone_up'],
    '小拳石': [rock.Graveler,25,'level_up'],
    '隆隆石': [rock.Golem,'岩之心','stone_up'],
    '玛瑙水母':[water.Tentacruel,30,'level_up'],
    '墨海马':[water.Seadra,32,'level_up'],
    '角金鱼':[water.Seaking,33,'level_up'],
    '海星星':[water.Starmie,'水之滴','stone_up'],
    '臭泥':[poison.Muk,38,'level_up'],
    '小磁怪':[electric.Magneton,30,'level_up'],
}
def canEvolveOrNot(obj,stone=None):
    '''
    判断是否又进化形态
    :param obj:
    :return:
    '''
    if obj.name in evolve_dict:
        if evolve_dict[obj.name][2] == 'level_up':
            if obj.level >= evolve_dict[obj.name][1]:
                return True
        elif evolve_dict[obj.name][2] == 'stone_up':
            if stone == evolve_dict[obj.name][1]:
                return True

    return False


def isEvolve(obj):
    '''
    进化属性 重载
    :param obj:
    :return:
    '''
    new_obj = evolve_dict[obj.name][0](level= obj.level,
                                    skill_list=obj.skill_list,
                                    exp_for_current=obj.exp_for_current,
                                    #realize_skill_list=obj.realize_skill_list,
                                    #status=obj.status,
                                    carry_prop=obj.carry_prop,
                                    base_points_list = [obj.health_base_point,
                                                       obj.attack_base_point,
                                                       obj.defense_base_point,
                                                       obj.spell_power_base_point,
                                                       obj.spell_defense_base_point,
                                                       obj.speed_base_point],
                                    has_trainer=True,
                                    is_autoAi=False)
    new_obj.realize_skill_list = obj.realize_skill_list
    new_obj.status = obj.status
    new_obj.health_indi = obj.health_indi,
    new_obj.attack_indi = obj.attack_indi
    new_obj.defense_indi = obj.defense_indi
    new_obj.spell_power_indi = obj.spell_power_indi
    new_obj.spell_defense_indi = obj.spell_defense_indi
    new_obj.speed_indi = obj.speed_indi

    print("你的 %s 进化成了 %s ！" % (obj.name, new_obj.name))
    time.sleep(5)
    evolveUp(obj,new_obj)
    #判断是否获得进化技能～
    if new_obj.pet_no in skilltree.pet_skill_tree:
        if 'evolve' in skilltree.pet_skill_tree[new_obj.pet_no]:
            for skill_code in skilltree.pet_skill_tree[new_obj.pet_no]['evolve']:
                learnskill.learnSkill(new_obj,skill_code)

    show.showPetStatus(new_obj)
    return new_obj

def evolveUp(obj,new_obj):
    health_up = new_obj._max_health - obj._max_health
    new_obj.health = obj.health + health_up
    attack_up = new_obj.attack - obj.attack
    defense_up = new_obj.defense - obj.defense
    spell_power_up = new_obj.spell_power - obj.spell_power
    spell_defense_up = new_obj.spell_defense - obj.spell_defense
    speed_up = new_obj.speed -obj.speed

    show.propertyUp(health_up,attack_up,defense_up,spell_power_up,spell_defense_up,speed_up)