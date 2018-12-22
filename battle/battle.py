import random
import time
import math
import battle.skill
import battle.skilllistmap
import battle.hitrate
import assist.show
import battle.buff
import assist.ppvalue
import assist.life
import assist.petattr
from assist import exp,evolve,changepet
from battle import skilldamage,asscount
from pets import pettalent,talentmap,status,statusmap
from props import propmap,bag
from players import battering
import props.drug

def damageCount(obj_defense,obj_attack,obj_skill):
    '''
    伤害计算模块
    :param obj_defense: 2P
    :param obj_attack: 1P
    :param :
    :return:
    :model : 0001:伤害加成  0002： 防御临时提高
    '''
    #战斗前的buff
    asscount.checkBuffBeforeBattle(obj_attack,obj_defense)
    #道具检查

    if obj_skill.skill_model == '0001':
        pro_buff_index = battle.buff.proBuffCount(obj_attack,obj_skill)
        skilldamage.skillDamage(obj_attack,obj_defense,obj_skill,pro_buff_index)
        obj_skill.addStatus(obj_defense) #附加状态
        print(obj_defense.status)

    elif obj_skill.skill_model == '0002':
        obj_attack.setBuff(obj_skill,[obj_skill.effect_turns-1,obj_skill.index_per])
        battle.buff.buffCount(obj_attack)
        for key,value in obj_attack.buff_dict.items():
            print(key.skill_show_name,':',value)

    elif obj_skill.skill_model == '0003':
        obj_defense.setDebuff(obj_skill,[obj_skill.effect_turns,obj_skill.index_per])
        battle.buff.proDebuffCount(obj_defense)
        for key,value in obj_defense.debuff_dict.items():
            print(key.skill_show_name, ':', value)

    elif obj_skill.skill_model == '0004':
        if obj_skill.status.status_code not in obj_defense.status:
            obj_defense.status.append(obj_skill.status.status_code)
            print(obj_defense.status)

    elif obj_skill.skill_model == '0005':
        obj_skill.useSkill(obj_attack)
        print(obj_attack.status)

    #0006 - 0007 移除buff debuff
    elif obj_skill.skill_model == '0006':
        battle.buff.removeObjBuff(obj_defense,obj_skill.remove_num)

    elif obj_skill.skill_model == '0007':
        battle.buff.removeOwnDebuff(obj_attack,obj_skill.remove_num)

    elif obj_skill.skill_model == '0008':
        assist.life.healthRecoverBySkill(obj_attack,obj_skill)

    elif obj_skill.skill_model == '0009':
        obj_attack.setProBuff(obj_skill,[obj_skill.effect_turns,obj_skill.index_per])
        for key,value in obj_attack.property_buff.items():
            print(key.skill_show_name, ':', value)

    if obj_attack.debuff_dict:
        battle.buff.damageDebuffCount(obj_attack) #行动后debuff 计算

    if obj_attack.property_buff:
        battle.buff.proBuffindex(obj_attack) #属性增强buff 次数计算


    if obj_defense.health <= 0: #战斗结束  debuff不会死亡
        assist.show.petDie(obj_defense.name)
        return False

    if obj_attack.health <= 0: #反弹死
        assist.show.petDie(obj_attack.name)
        return False


    else:
        #检查战斗后特性检查
        if talentmap.checkTalent(obj_attack,'after'):
            talentmap.talentEffectAfter(obj_attack,obj_skill)

        assist.show.showPetStatus(obj_defense)
        assist.show.showPetStatus(obj_attack)
        return True

def battleRun(player,obj1,obj2):
    '''
    攻击模块
    :param obj1:
    :param obj2:
    :return:
    '''
    assist.show.showSelect()
    print("=" * 30)
    if obj1.autoAi:
        #为测试方便，都指定为1
        command = '1'
        assist.show.petThink(obj1.name)
        time.sleep(3)
    else:
        print("玩家请选择指令：")
        command = input(">>")
    if command == '1':
        if obj1.autoAi:
            assist.show.petSelectSkill(obj1.name)
            time.sleep(3)
            skill_number = str(random.randint(1,len(obj1.skill_list)))
        else:
            for key, value in obj1.skill_list.items():
                if value != None:
                    print("技能" + key, ":", value.skill_show_name, ' PP:', value.pp_value)
            print('0','返回上级！')
            print("请选择使用的技能：")
            skill_number = input(">>")
            if skill_number == '0':
                print("返回上级")
                return battleRun(player,obj1,obj2)
            if skill_number not in obj1.skill_list:
                print("指令错误！")
                return battleRun(player,obj1,obj2)
            if not assist.ppvalue.ppCount(obj1.skill_list[skill_number]):
                print("指令失败,重新选择！")
                return battleRun(player,obj1, obj2)
        assist.show.useSkill(obj1,obj1.skill_list[skill_number])
        print(obj1.skill_list[skill_number]) #显示技能描述
        #检查时否是睡眠状态
        if statusmap.checkSleepingOrNot(obj1):
            print("%s 处于睡眠状态，无法使用技能！" % obj1.name)
            assist.show.printTurn(obj2)
            return battleRun(player,obj2,obj1)
        #状态判断是否可以行动
        if statusmap.checkParalysisOrNot(obj1):
            print("%s 没有成功使用技能" % obj1.name)
            assist.show.printTurn(obj2)
            return battleRun(player,obj2,obj1)
        #命中与否判断
        #判断命中是否提高
        hit_up = propmap.checkCarryPropForHit(obj1)
        print("命中提高",hit_up)
        dodge_up = propmap.checkCarryPropFoeDodge(obj2)
        print("闪避提高",dodge_up)


        if not battle.hitrate.hitOrNot(obj1.skill_list[skill_number].hit_rate + hit_up,obj1,obj2,obj2.dodge + dodge_up):
            assist.show.printTurn(obj2.name)
            return battleRun(player,obj2,obj1)

        #改写结算 直接把技能扔进去
        if damageCount(obj2,obj1,obj1.skill_list[skill_number]):
            assist.show.printTurn(obj2.name)
            return battleRun(player,obj2,obj1)
        else:
            return True

    elif command == '2':
        #交换精灵模块
        if changepet.changePet(player):
            #加一个经验状态减半的效果 ST999 经验减半
            obj2.exp_status.append('ST999')
            return battering.battleing(player,obj2,change_pet=True)
    elif command == '4':
        assist.show.petUseRun(obj1.name)
        x = random.randint(1,100)
        if x in range(1,11):
            print("逃跑成功")
            print("游戏结束")
        else:
            print("逃跑失败")
            assist.show.printTurn(obj2.name)
            return battleRun(player,obj2,obj1)
    elif command == '3':
        #测试 得到一个道具
        #propmap.getProp(propmap.prop_dict['五彩迷光'])
        if bag.showBattleBagOrNot(obj1,obj2):
            if obj2.captured == False:
                assist.show.printTurn(obj2)
                return battleRun(player,obj2,obj1)
            else:
                return True
        else:
            #print("重新选择！")
            #assist.show.printTurn(obj2)
            return battleRun(player,obj1, obj2)

    else:
        print("指令错误!")
        return battleRun(player,obj1,obj2)

