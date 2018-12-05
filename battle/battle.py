import random
import time
import battle.skill
import battle.skilllistmap
import assist.show
import battle.buff
import assist.ppvalue

def randomRange():
    '''
    概率随机数
    :return:
    '''
    x = random.randint(1,100)
    if x in range(1,71):
        return 1
    elif x in range(71,81):
        return 2
    elif x in range(81,91):
        return 3
    else:
        return 4

def damageCount(obj1,obj2,obj_skill):
    '''
    伤害计算模块
    :param obj1: 2P
    :param obj2: 1P
    :param :
    :return:
    :model : 0001:伤害加成  0002： 防御临时提高
    '''
    if obj2.buff_dict:
        battle.buff.buffCount(obj2)
        battle.buff.buffIndex(obj2)

    if obj1.buff_dict:
        battle.buff.buffCount(obj1)


    if obj_skill.skill_model == '0001':
        if obj2.attack - obj1.getDefense() > 0:
            #tmpdamage 测试伤害计算
            tmpdamage = (obj2.attack - obj1.getDefense()) * obj_skill.index_per
            obj1.health -= (obj2.attack - obj1.getDefense()) * obj_skill.index_per
            print("造成了%s 的伤害" % tmpdamage)
        else:
            assist.show.noDamage()
    elif obj_skill.skill_model == '0002':
        #obj2.tmp_defense = obj2.defense * index
        #assist.show.petUseDefense(obj2.name)
        tmp_defense_value = obj2.defense * obj_skill.index_per
        obj2.setBuff(obj_skill,[obj_skill.effect_turns,tmp_defense_value])

        #buff_dict[obj_skill] = [obj_skill.skill_model,tmpdefense]
        #battle.buff.buff_dict[obj2]=buff_dict
        #print(battle.buff.buff_dict[obj2][obj_skill.skill_model])
        for key,value in obj2.buff_dict.items():
            print(key.skill_show_name,':',value)
        #battle.buff.buffCount(obj2)


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
        command = randomRange()
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
        #print("选择的技能是：")
        #index 调整系数 model 技能效果
        #index,model = battle.skilllistmap.skillSelect(obj1.skill_list[skill_number]) 旧版本 使用了中间文件
        #改写结算 直接把技能扔进去
        #计算PP值
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
        #使用道具模块
        pass
        return battleRun(obj2,obj1)
    else:
        print("指令错误!")
        return battleRun(obj1,obj2)