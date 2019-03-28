from assist import cap,show,evolve
from battle import learnskill,asscount
from pets import  skilltree
from props import propmap
import time


def getExpForUp(lv):
    '''
    求升级经验值
    :param lv:
    :return:
    '''
    if lv > 1:
        return pow(lv + 1, 3) - pow(lv, 3)
    else:
        return 1


def getBattleSuccessExp(player,obj,exp_basic = 1,ai_index=1,carry_prop=1):
    '''
    战斗获胜经验
    :param lv:
    :return:
    '''
    if obj.autoAi == True:
        if obj.has_trainer == None:
            ai_index = 10

    if len(player.battle_pet_list) > 1:
        exp_basic = 0.5

    print("经验基数",exp_basic)
    print("调整基数",ai_index)
    print("经验学习机器基数",carry_prop)

    #后续版本 随身道具
    #if withExpfruit == True:
    #    fruit_index = 1.5
    #else:
    #    fruit_index = 1

    got_exp = int((obj.level * obj.basic_exp_value)/7 * ai_index * exp_basic * carry_prop)

    return got_exp




def isLevelUp(obj):
    '''
    判断是否升级
    :param obj:
    :return:
    '''
    if obj.level == 100:
        print("%s 已经是最高等级" % obj.name)
        return True

    if obj.exp_for_current >= getExpForUp(obj.level):

        obj.exp_for_current -= getExpForUp(obj.level)
        obj.level += 1
        print('%s 升到 %s 级！' % (obj.name, obj.level))

        levelUp(obj)
        #增加点执行时间
        time.sleep(1)

        #判断是否学习可以学习新技能
        try:
            if obj.level in skilltree.pet_skill_tree[obj.pet_no]:
                if not isinstance(skilltree.pet_skill_tree[obj.pet_no][obj.level],list):
                    learnskill.learnSkill(obj,skilltree.pet_skill_tree[obj.pet_no][obj.level])
                else:
                    for skill_code in skilltree.pet_skill_tree[obj.pet_no][obj.level]:
                        learnskill.learnSkill(obj,skill_code)

        except AttributeError and KeyError:
            print("测试代码,该精灵未添加技能树")


        return isLevelUp(obj)
    else:
        return True


def levelUp(obj):
    '''
    升级 属性增加
    :param obj:
    :return:
    '''
    health_up = cap.gethpCapValue(obj.health_basic, obj.level, obj.health_indi,obj.health_base_point) - obj._max_health
    attack_up = cap.getCapValue(obj.attack_basic, obj.level, obj.attack_indi,obj.attack_base_point) - obj.attack
    defense_up = cap.getCapValue(obj.defense_basic, obj.level, obj.defense_indi,obj.defense_base_point) - obj.defense
    spell_power_up = cap.getCapValue(obj.spell_power_basic, obj.level, obj.spell_power_indi,obj.spell_power_base_point) - obj.spell_power
    spell_defense_up = cap.getCapValue(obj.spell_defense_basic, obj.level, obj.spell_defense_indi,obj.spell_defense_base_point) -obj.spell_defense
    speed_up = cap.getCapValue(obj.speed_basic, obj.level, obj.speed_indi,obj.speed_base_point) - obj.speed

    #属性改变
    obj._max_health += health_up
    if obj.alive:
        obj.health += health_up
    obj.attack += attack_up
    obj.defense += defense_up
    obj.spell_power += spell_power_up
    obj.spell_defense += spell_defense_up
    obj.speed += speed_up

    show.propertyUp(health_up,attack_up,defense_up,spell_power_up,spell_defense_up,speed_up)


def accountAfterBattleEnd(player,pet):
    for get_exp_pet in player.battle_pet_list:
        # 检查是否携带学习机器
        exp_up = propmap.checkCarryPropForExpUp(get_exp_pet)
        # 清除buff
        #get_exp_pet.buff_dict.clear()
        #get_exp_pet.property_buff.clear()

        got_exp = 0

        # 计算获得的基础点数
        if pet.basic_point_getter == get_exp_pet:
            print("基础点数获得者", pet.basic_point_getter)
            asscount.getBasePoint(get_exp_pet, pet.can_get_base_point_type,
                                  pet.can_get_base_point)
        # 战斗结束之后结算
        # 经验值计算
        got_exp += getBattleSuccessExp(player, pet, carry_prop=exp_up)
        print("%s 获得 %s 经验值" % (get_exp_pet.name, got_exp))
        get_exp_pet.exp_for_current += got_exp

        if isLevelUp(get_exp_pet):
            show.showPetStatus(get_exp_pet)
        # 进化判断
        if evolve.canEvolveOrNot(get_exp_pet):

            print("精灵是否进化！ 1 yes  2 no ")
            isEvo = input(">")
            if int(isEvo) == 1:
                player.setPet('Master', evolve.isEvolve(get_exp_pet))

            else:
                print("精灵停止进化！")
