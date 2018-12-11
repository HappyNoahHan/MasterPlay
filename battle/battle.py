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
from assist import exp,evolve
from battle import skilldamage
from pets import pettalent,talentmap
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
    #技能使用前buff 检查
    if obj_attack.buff_dict:
        battle.buff.buffCount(obj_attack)
        battle.buff.buffIndex(obj_attack)
    else:
        print("没有buff")

    #检查战斗前天赋技能
    if talentmap.checkTalent(obj_attack,'before'):
        pass
    if talentmap.checkTalent(obj_defense,'before'):
        pass

    if obj_skill.skill_model == '0001':
        pro_buff_index = battle.buff.proBuffCount(obj_attack,obj_skill)
        skilldamage.skillDamage(obj_attack,obj_defense,obj_skill,pro_buff_index)

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

    #0006 - 0007 移除buff debuff
    elif obj_skill.skill_model == '0006':
        battle.buff.removeObjBuff(obj_defense,obj_skill.remove_num)

    elif obj_skill.skill_model == '0007':
        battle.buff.removeOwnDebuff(obj_attack,obj_skill.remove_num)

    elif obj_skill.skill_model == '0008':
        assist.life.healthRecover(obj_attack,obj_skill)

    elif obj_skill.skill_model == '0009':
        obj_attack.setProBuff(obj_skill,[obj_skill.effect_turns,obj_skill.index_per])
        for key,value in obj_attack.property_buff.items():
            print(key.skill_show_name, ':', value)

    if obj_attack.debuff_dict:
        battle.buff.damageDebuffCount(obj_attack) #行动后debuff 计算

    if obj_attack.property_buff:
        battle.buff.proBuffindex(obj_attack) #属性增强buff 次数计算


    if obj_defense.health <= 0: #战斗结束
        assist.show.petDie(obj_defense.name)
        return False

    else:
        #检查战斗后特性检查
        if talentmap.checkTalent(obj_attack,'after'):
            talentmap.talentEffectAfter(obj_attack,obj_skill)

        assist.show.showPetStatus(obj_defense)
        assist.show.showPetStatus(obj_attack)
        return True

def battleRun(obj1,obj2):
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
    if int(command) == 1:
        for key,value in obj1.skill_list.items():
            if value != None:
                print("技能" + key,":", value.skill_show_name,' PP:',value.pp_value)
        if obj1.autoAi:
            assist.show.petSelectSkill(obj1.name)
            time.sleep(3)
            skill_number = str(random.randint(1,len(obj1.skill_list)))
        else:
            print("请选择使用的技能：")
            skill_number = input(">>")
            if skill_number not in obj1.skill_list:
                print("指令错误！")
                return battleRun(obj1,obj2)
            if not assist.ppvalue.ppCount(obj1.skill_list[skill_number]):
                print("指令失败,重新选择！")
                return battleRun(obj1, obj2)
        assist.show.useSkill(obj1,obj1.skill_list[skill_number])
        print(obj1.skill_list[skill_number]) #显示技能描述
        #命中与否判断
        if not battle.hitrate.hitOrNot(obj1.skill_list[skill_number].hit_rate):
            assist.show.printTurn(obj2.name)
            return battleRun(obj2,obj1)

        #改写结算 直接把技能扔进去
        if damageCount(obj2,obj1,obj1.skill_list[skill_number]):
            assist.show.printTurn(obj2.name)
            return battleRun(obj2,obj1)
        else:
            return True

    elif int(command) == 2:
        #交换精灵模块
        return battleRun(obj2,obj1)
    elif int(command) == 4:
        assist.show.petUseRun(obj1.name)
        x = random.randint(1,100)
        if x in range(1,11):
            print("逃跑成功")
            print("游戏结束")
        else:
            print("逃跑失败")
            assist.show.printTurn(obj2.name)
            return battleRun(obj2,obj1)
    elif int(command) == 3:
        assist.show.showProps()
        command = input(">")
        if int(command) == 1:
            #drup_to_use = props.drug.ppDrug()
            for key, value in obj1.skill_list.items():
                if value != None:
                    print("技能" + key, ":", value.skill_show_name, ' PP:', value.pp_value)
            print("请选择要恢复的技能")
            skill_number = input(">")
            print(obj1.skill_list[skill_number].skill_show_name)
            assist.ppvalue.ppRecoverMax(obj1.skill_list[skill_number])

        return battleRun(obj2,obj1)
    else:
        print("指令错误!")
        return battleRun(obj1,obj2)

