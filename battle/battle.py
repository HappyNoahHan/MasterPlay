import random
import time
import math
import battle.skill
import battle.skilllistmap
import assist.show
import battle.buff
import assist.ppvalue
import assist.life
import props.drug


def damageCount(obj1,obj2,obj_skill):
    '''
    伤害计算模块
    :param obj1: 2P
    :param obj2: 1P
    :param :
    :return:
    :model : 0001:伤害加成  0002： 防御临时提高
    '''
    #技能使用前buff 检查
    if obj2.buff_dict:
        battle.buff.buffCount(obj2)
        battle.buff.buffIndex(obj2)
    else:
        print("没有buff")

    if obj_skill.skill_model == '0001':
        #计算属性增幅，道具增幅
        pro_buff_index = 0
        if obj2.property_buff:
            pro_buff_list = battle.buff.proBuffCount(obj2)
            if pro_buff_list:
                pro_buff_index = sum(pro_buff_list)
        if obj2.getAttack() - obj1.getDefense() > 0:
            #tmpdamage 测试伤害计算
            tmpdamage = round(((obj2.getAttack() - obj1.getDefense()) * obj_skill.index_per) * (1+pro_buff_index))
            obj1.health -= tmpdamage
            print("造成了%s 的伤害" % tmpdamage)
        else:
            assist.show.noDamage()
    elif obj_skill.skill_model == '0002':
        tmp_defense_value = round(obj2.defense * obj_skill.index_per)
        obj2.setBuff(obj_skill,[obj_skill.effect_turns-1,tmp_defense_value])
        battle.buff.buffCount(obj2)

        for key,value in obj2.buff_dict.items():
            print(key.skill_show_name,':',value)

    elif obj_skill.skill_model == '0003':
        obj1.setDebuff(obj_skill,[obj_skill.effect_turns,obj_skill.index_per])
        for key,value in obj1.debuff_dict.items():
            print(key.skill_show_name, ':', value)

    elif obj_skill.skill_model == '0004':
        tmp_attack_value = round(obj2.attack * obj_skill.index_per)
        obj2.setBuff(obj_skill,[obj_skill.effect_turns-1,tmp_attack_value])
        battle.buff.buffCount(obj2)
        for key,value in obj2.buff_dict.items():
            print(key.skill_show_name, ':', value)

    elif obj_skill.skill_model == '0007':
        assist.life.healthRecover(obj2,obj_skill)
        obj2.setBuff(obj_skill,[obj_skill.effect_turns-1,0])
        for key,value in obj2.buff_dict.items():
            print(key.skill_show_name, ':', value)
    elif obj_skill.skill_model == '0008':
        assist.life.healthRecover(obj2,obj_skill)

    elif obj_skill.skill_model == '0009':
        obj2.setProBuff(obj_skill,[obj_skill.effect_turns,obj_skill.index_per])
        for key,value in obj2.property_buff.items():
            print(key.skill_show_name, ':', value)

    if obj2.debuff_dict:
        battle.buff.debuffCount(obj2) #行动后debuff 计算

    if obj1.health <= 0:
        assist.show.petDie(obj1.name)
        return False

    else:

        assist.show.showPetStatus(obj1)
        assist.show.showPetStatus(obj2)
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
        print(obj1.skill_list[skill_number]) #显示技能描述
        #改写结算 直接把技能扔进去
        if damageCount(obj2,obj1,obj1.skill_list[skill_number]):
            assist.show.printTurn(obj2.name)
            return battleRun(obj2,obj1)
        else:
            pass


    elif int(command) == 2:
        #交换精灵模块
        pass
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