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
from assist import exp,evolve,changepet,rancom
from battle import skilldamage,asscount
from pets import pettalent,talentmap,status,statusmap
from props import propmap,bag
from players import battering
import props.drug

def damageCount(obj_defense,obj_attack,obj_skill,weather):
    '''
    伤害计算模块
    :param obj_defense: 2P
    :param obj_attack: 1P
    :param :
    :return:
    :model : 0001:伤害加成  0002： 防御临时提高
    '''
    #战斗前的buff
    #asscount.checkBuffBeforeBattle(obj_attack,obj_defense)
    #道具检查

    if obj_skill.skill_model == '0001':
        pro_buff_index = battle.buff.proBuffCount(obj_attack,obj_skill)
        damage = skilldamage.skillDamage(obj_attack,obj_defense,obj_skill,pro_buff_index,obj_skill.skill_power)
        obj_skill.addStatus(obj_defense)  # 附加状态
        if damage > 0:
            obj_defense.health -= damage
            print("造成了%s 的伤害" % damage)
        else:
            obj_defense.health -= 1
            assist.show.noDamage()

        assist.show.showPetErrorStatus(obj_defense)

    elif obj_skill.skill_model == '0002':
        obj_attack.setBuff(obj_skill,[obj_skill.effect_turns-1,obj_skill.index_per])
        battle.buff.buffCount(obj_attack)
        for key,value in obj_attack.buff_dict.items():
            print(key.show_name,':',value)

    elif obj_skill.skill_model == '0003':
        obj_defense.setDebuff(obj_skill,[obj_skill.effect_turns,obj_skill.index_per])
        battle.buff.proDebuffCount(obj_defense)
        for key,value in obj_defense.debuff_dict.items():
            print(key.show_name, ':', value)

    elif obj_skill.skill_model == '0004':
        obj_skill.addStatus(obj_defense)
        print(obj_defense.status)

    elif obj_skill.skill_model == '0012':
        if obj_skill.doubleEffect(weather):
            obj_skill.addStatus(obj_attack,double=2)
        else:
            obj_skill.addStatus(obj_attack)
        print(obj_attack.status)

    elif obj_skill.skill_model == '0005':
        obj_skill.useSkill(obj_attack=obj_attack,obj_defense=obj_defense)
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
            print(key.show_name, ':', value)

    elif obj_skill.skill_model == '0010':
        pro_buff_index = battle.buff.proBuffCount(obj_attack, obj_skill)
        damage = skilldamage.skillDamage(obj_attack, obj_defense, obj_skill, pro_buff_index,obj_skill.skill_power)
        if damage > 0:
            obj_defense.health -= damage
            print("造成了%s 的伤害" % damage)
        else:
            obj_defense.health -= 1
            assist.show.noDamage()
        #obj_skill.addStatus(obj_defense)  # 吸取技能无附加状态
        #print(obj_defense.status)
        #吸取血量
        assist.life.healthRecoverFromDamage(obj_attack,damage,obj_skill.suck_per)
        assist.show.showPetErrorStatus(obj_defense)

    elif obj_skill.skill_model == '0011':
        if obj_skill.imprint_level == 1:
            obj_skill.addStatus(obj_attack)
        else:
            if obj_skill.status in obj_attack.status:
                if obj_skill.imprint_type == 'restore':
                    assist.life.healthRecoverFromImprintSkill(obj_attack,obj_attack.status[obj_skill.status])
                    statusmap.removeStatus(obj_attack,obj_skill.status)
                elif obj_skill.imprint_type == 'damage':
                    pro_buff_index = battle.buff.proBuffCount(obj_attack, obj_skill)
                    damage = skilldamage.skillDamage(obj_attack, obj_defense, obj_skill, pro_buff_index,
                                                     obj_attack.status[obj_skill.status] * 100)
                    if damage > 0:
                        obj_defense.health -= damage
                        print("造成了%s 的伤害" % damage)
                    else:
                        obj_defense.health -= 1
                        assist.show.noDamage()
            else:
                print("无蓄力,没有任何效果")

    elif obj_skill.skill_model == '0013':
        if obj_skill.addStatus(obj_attack,obj_defense):
            return False
        else:
            print("没有任何效果")

    elif obj_skill.skill_model == '0014':
        copy_skill = obj_skill.useOrNot(obj_defense)
        if copy_skill != None:
            return damageCount(obj_defense,obj_attack,copy_skill,weather)
        else:
            print("没有任何效果")

    #debuff  增幅buff 次数
    asscount.checkBuffAfterBattle(obj_attack)


    if obj_defense.health <= 0: #战斗结束  debuff不会死亡
        assist.show.petDie(obj_defense.name)
        assist.show.battleOver()
        return False

    if obj_attack.health <= 0: #反弹死
        assist.show.petDie(obj_attack.name)
        assist.show.battleOver()
        return False


    else:
        #检查战斗后特性检查
        #if obj_attack.talent != None:
        #    if talentmap.checkTalent(obj_attack,'after'):
        #        talentmap.talentEffectAfter(obj_attack,obj_skill)
        return True


def battleRun(player,obj1,obj2,weather):
    '''
    攻击模块
    :param obj1:
    :param obj2:
    :return:
    '''
    print("=" * 15 + '当前状态' + "=" * 15)
    assist.show.showPetStatus(obj1)
    assist.show.showPetStatus(obj2)
    print("=" * 30)
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
            skill_number = random.choice(rancom.canChoiceList(obj1))
        else:
            for key, value in obj1.skill_list.items():
                if value != None:
                    print("技能" + key, ":", value.show_name, ' PP:', value.pp_value)
            print('0','返回上级！')
            print("请选择使用的技能：")
            skill_number = input(">>")
            if skill_number == '0':
                print("返回上级")
                return battleRun(player,obj1,obj2,weather)
            if skill_number not in obj1.skill_list:
                print("指令错误！")
                return battleRun(player,obj1,obj2,weather)
            if not assist.ppvalue.ppCount(obj1.skill_list[skill_number]):
                print("指令失败,重新选择！")
                return battleRun(player,obj1, obj2,weather)
            if obj1.skill_list[skill_number].use_condition != None:
                if obj1.skill_list[skill_number].use_condition not in obj1.status:
                    print("技能无法使用！")
                    return battleRun(player,obj1,obj2,weather)
        #记录最后使用的技能
        obj1.last_used_skill = obj1.skill_list[skill_number]
        # 战斗前的buff
        asscount.checkBuffBeforeBattle(obj1, obj2)
        # 道具检查
        assist.show.useSkill(obj1,obj1.skill_list[skill_number])
        print(obj1.skill_list[skill_number]) #显示技能描述
        #检查状态
        if statusmap.checkStatusBeforeBattle(obj1):
            # 回合结束检查是否中毒  中毒死亡
            if not statusmap.checkStatusAfterTurn(obj1):
                assist.show.petDie(obj1.name)
                assist.show.battleOver()
                return True

            assist.show.printTurn(obj2)
            return battleRun(player,obj2,obj1,weather)
        #检查是否混乱,会攻击自己
        if statusmap.checkChaosOrNot(obj1):
            damage = skilldamage.chaosDamage(obj1.level,obj1.getAttack(),obj1.getDefense())
            print("%s 混乱中, 对自己造成了 %s 伤害" % (obj1.name,damage))
            obj1.health -= damage
            if obj1.health <= 0:
                assist.show.petDie(obj1.name)
                assist.show.battleOver()
                return True
            else:
                # 回合结束检查是否中毒  中毒死亡
                if not statusmap.checkStatusAfterTurn(obj1):
                    assist.show.petDie(obj1.name)
                    assist.show.battleOver()
                    return True
                assist.show.printTurn(obj2)
                return battleRun(player,obj2,obj1,weather)


        #命中与否判断
        hit = obj1.skill_list[skill_number].hit_rate
        #判断命中是否提高 携带物品
        hit_up = propmap.checkCarryPropForHit(obj1)
        print("命中提高: ",hit_up)
        dodge_up = propmap.checkCarryPropFoeDodge(obj2)
        print("闪避提高: ",dodge_up)
        #状态检查 命中降低或者提高
        hit = statusmap.checkStatusHitIndexBeforeBattle(obj1,hit)
        print("真实命中: ",hit+hit_up)
        #多段技能结算
        if obj1.skill_list[skill_number].multi_step == False:
            if not battle.hitrate.hitOrNot(obj1.skill_list[skill_number],hit + hit_up,obj1,obj2,obj2.dodge + dodge_up):
                asscount.checkBuffAfterBattle(obj1)
                # 回合结束检查是否中毒  中毒死亡
                if not statusmap.checkStatusAfterTurn(obj1):
                    assist.show.petDie(obj1.name)
                    assist.show.battleOver()
                    return True
                assist.show.printTurn(obj2.name)
                return battleRun(player,obj2,obj1,weather)
            #改写结算 直接把技能扔进去
            if damageCount(obj2,obj1,obj1.skill_list[skill_number],weather):
                # 回合结束检查是否中毒  中毒死亡
                if not statusmap.checkStatusAfterTurn(obj1):
                    assist.show.petDie(obj1.name)
                    assist.show.battleOver()
                    return True
                assist.show.printTurn(obj2.name)
                return battleRun(player,obj2,obj1,weather)
            else:
                return True
        #多段
        else:
            counts = rancom.getStepOfSkill()
            for count in range(counts):
                print("第 %s 次 攻击 " % (count+1))
                print("=" * 30)
                if battle.hitrate.hitOrNot(obj1.skill_list[skill_number], hit + hit_up, obj1, obj2,obj2.dodge + dodge_up):
                    if not damageCount(obj2, obj1, obj1.skill_list[skill_number],weather):
                        return True
                else:
                    continue
                time.sleep(1)

            if not statusmap.checkStatusAfterTurn(obj1):
                assist.show.petDie(obj1.name)
                assist.show.battleOver()
                return True
            assist.show.printTurn(obj2.name)
            return battleRun(player, obj2, obj1,weather)

    elif command == '2':
        #交换精灵模块
        if statusmap.checkNoChange(obj1):
            if changepet.changePet(player):
                statusmap.resetStatusAfterChange(obj1)
                #加一个经验状态减半的效果 ST999 经验减半
                #obj2.exp_status.append('ST999')
                #因未返回到explore层，换精灵结算顺序正常
                return battering.battleing(player,obj2,change_pet=True)
            else:
                return battleRun(player,obj1,obj2,weather)
        else:
            print("%s 无法被替换的状态" % obj1.name)
            return battleRun(player,obj1,obj2,weather)

    elif command == '4':
        assist.show.petUseRun(obj1.name)
        if statusmap.checkUnlockOrNot(obj1):
            x = random.randint(1,100)
            if x in range(1,100):
                print("逃跑成功")
                player.battle_run_success = True
                return True
        else:
            print("%s 被锁定了！ 无法脱逃 ~" % obj1.name)
        print("逃跑失败")
        assist.show.printTurn(obj2.name)
        return battleRun(player,obj2,obj1,weather)

    elif command == '3':
        #测试 得到一个道具
        #propmap.getProp(propmap.prop_dict['五彩迷光'])
        use_or_not = bag.showBattleBagOrNot(player,obj2)
        if use_or_not == True:
            if obj2.captured == False:
                # 回合结束检查是否中毒  中毒死亡
                if not statusmap.checkStatusAfterTurn(obj1):
                    assist.show.petDie(obj1.name)
                    assist.show.battleOver()
                    return True
                assist.show.printTurn(obj2)
                return battleRun(player,obj2,obj1,weather)
            else:
                #捕获成功 战斗结束
                return True
        elif use_or_not == None:
            return battleRun(player,obj1, obj2,weather)
        else:
            #print("重新选择！")
            #assist.show.printTurn(obj2)
            if not statusmap.checkStatusAfterTurn(obj1):
                assist.show.petDie(obj1.name)
                assist.show.battleOver()
                return True
            return battleRun(player,obj2, obj1,weather)

    else:
        print("指令错误!")
        return battleRun(player,obj1,obj2,weather)

