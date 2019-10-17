import random
import time
import battle.skilllistmap
import battle.hitrate
import assist.show
import assist.ppvalue
import assist.life
import assist.petattr
from assist import changepet,rancom
from battle import skilldamage
from pets import statusmap
from props import propmap,bag
from players import battering

def damageCount(obj_defense,obj_attack,obj_skill,place):
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

        if obj_skill.fixed_damage == False:
            # 得到技能威力
            if obj_skill.power_changed:
                power = obj_skill.getPower(obj_attack,obj_defense)
            else:
                power = obj_skill.getPower()
            damage = skilldamage.skillDamage(obj_attack,obj_defense,obj_skill,power,place)

            if obj_skill.hit_status:
                obj_skill.addStatus(obj_defense,place)  # 附加状态

            if obj_skill.side_effect != None:
                obj_skill.getSideEffect(obj_attack,damage) #副作用

            if obj_skill.clean_status and damage > 0: #清除效果
                obj_skill.cleanStatus(obj_attack)

            if obj_skill.berry_effect: #树果效果
                obj_skill.eatBerry(obj_attack,obj_defense)

            if obj_skill.self_effect:# 附加效果 等其他
                obj_skill.selfSideEffect(obj_attack,obj_defense,damage)

            if obj_skill.remove_status: #移除对方状态
                obj_skill.removeStatus(obj_defense)

            if obj_skill.prize_effect: #赏金
                obj_skill.setPrize(obj_defense)
        else:
            damage = obj_skill.getDamage(obj_attack,obj_defense)

        if damage > 0:
            obj_defense.hp -= damage
            print("造成了%s 的伤害" % damage)

            if obj_skill.recover_by_damage: #吸取回复
                obj_skill.recover(obj_attack,damage)
        else:
            obj_defense.hp -= 1
            assist.show.noDamage()

        assist.show.showPetErrorStatus(obj_defense)

    elif obj_skill.skill_model == '0004':
        obj_skill.addStatus(obj_defense,place)

        if obj_skill.need_user:
            obj_skill.setStatusGiver(obj_attack)

        if obj_skill.side_effect:
            obj_skill.sideEffect(obj_attack)
        print(obj_defense.status)

    elif obj_skill.skill_model == '0012':
        if obj_skill.doubleEffect(place.weather):
            obj_skill.addStatus(obj_attack,place,double=2)
        else:
            obj_skill.addStatus(obj_attack,place)
        print(obj_attack.status)

    elif obj_skill.skill_model == '0008':
        if obj_skill.recover_health:
            if obj_skill.weather_condition == None:
                    index_per = obj_skill.getIndexPer()
            else:
                index_per = obj_skill.getIndexPer(place.weather)

            if not obj_skill.max_recover_allowable:
                if obj_attack.hp == obj_attack._max_health:
                    print("技能使用失败~~")
                    #return True
            assist.life.healthRecoverBySkill(obj_attack, index_per)

        if obj_skill.recover_status:
            if obj_skill.remove_status:
                obj_skill.removeStatus(obj_defense)
            if obj_skill.clean_status:
                obj_skill.cleanStatus(obj_attack)

        if obj_skill.hit_status:
            obj_skill.setStatus(obj_attack,place)
            #obj_skill.setStatusGiver(obj_attack)

    elif obj_skill.skill_model == '0011':
        if obj_skill.imprint_level == 1:
            obj_skill.addStatus(obj_attack)
        else:
            if obj_skill.status in obj_attack.status:
                if obj_skill.imprint_type == 'restore':
                    assist.life.healthRecoverFromImprintSkill(obj_attack,obj_attack.status[obj_skill.status])
                    statusmap.removeStatus(obj_attack,obj_skill.status)
                elif obj_skill.imprint_type == 'damage':

                    damage = skilldamage.skillDamage(obj_attack, obj_defense, obj_skill,
                                                     obj_attack.status[obj_skill.status] * 100,place)
                    if damage > 0:
                        obj_defense.hp -= damage
                        print("造成了%s 的伤害" % damage)
                    else:
                        obj_defense.hp -= 1
                        assist.show.noDamage()
            else:
                print("无蓄力,没有任何效果")

    elif obj_skill.skill_model == '0013':
        if obj_skill.addStatus(obj_attack,obj_defense):
            return False
        else:
            print("没有任何效果")

    elif obj_skill.skill_model == '0014':
        if obj_skill.copy_skill_or_not:
            copy_skill = obj_skill.useOrNot(obj_defense)
            if copy_skill != None:
                return damageCount(obj_defense,obj_attack,copy_skill,place)
            else:
                print("没有任何效果")
        else:
            statusmap.getGainStatusFromDefenser(obj_attack,obj_defense)

    elif obj_skill.skill_model == '0015':
        result = statusmap.checkDelayStatus(obj_attack)
        if result == 0:
            obj_skill.useSkill(obj_attack)
        elif result == 2 or result == 3:
            obj_skill.removeStatus(obj_attack)

        if not obj_skill.delay_effect or result == 3:
            damage = skilldamage.skillDamage(obj_attack,obj_defense,obj_skill,obj_skill.getPower(obj_attack),place)
            #obj_skill.addStatus(obj_defense)  # 附加状态
            if damage > 0:
                obj_defense.hp -= damage
                print("造成了%s 的伤害" % damage)
            else:
                obj_defense.hp -= 1
                assist.show.noDamage()

            assist.show.showPetErrorStatus(obj_defense)

    elif obj_skill.skill_model == '0016':
        if obj_skill.skill_code == 'N021':
            if obj_attack.berry == None:
                print("没有任何效果~~")
                return True
            obj_skill.skill_power,obj_skill.property= obj_skill.getPowerAndProperty(obj_attack.berry)
            # 消耗树果
            print("%s 使用%s 消耗了 一枚 %s " % (obj_attack.getName(), obj_skill.show_name, obj_attack.berry.show_name))
            obj_attack.berry = None
        damage = skilldamage.skillDamage(obj_attack, obj_defense, obj_skill, obj_skill.skill_power,place)
            # obj_skill.addStatus(obj_defense)  # 附加状态
        if damage > 0:
            obj_defense.hp -= damage
            print("造成了%s 的伤害" % damage)
        else:
            obj_defense.hp -= 1
            assist.show.noDamage()


        assist.show.showPetErrorStatus(obj_defense)

    elif obj_skill.skill_model == '0017':
        if not obj_skill.weather_change:
            place.setPlaceStatus(obj_skill.status,obj_skill.turns)
        else:
            place.setPlaceWeather(obj_skill.weather)

    elif obj_skill.skill_model == '0019':
        obj_skill.addStatus(obj_defense,obj_attack)



    if obj_defense.hp <= 0: #战斗结束  debuff不会死亡
        #诅咒技能效果
        if 'ST119' in obj_defense.status:
            if obj_skill.skill_model in ['0001','0015']:
                obj_skill.pp = 0

        assist.show.petDie(obj_defense)
        assist.show.battleOver()
        if obj_attack.hp <= 0:  # 反弹死
            assist.show.petDie(obj_attack)
            assist.show.battleOver()
        return False

    if obj_attack.hp <= 0: #反弹死
        assist.show.petDie(obj_attack)
        assist.show.battleOver()
        return False


    else:
        #检查战斗后特性检查
        #if obj_attack.talent != None:
        #    if talentmap.checkTalent(obj_attack,'after'):
        #        talentmap.talentEffectAfter(obj_attack,obj_skill)
        return True

def battleRun(player,obj1,obj2,place):
    '''
    攻击模块
    :param obj1:
    :param obj2:
    :return:
    '''
    print("=" * 15 + '当前状态' + "=" * 15)
    assist.show.showPetStatus(obj1)
    assist.show.showPetStatus(obj2)
    assist.show.showPlaceMessage(place)
    print("=" * 30)
    assist.show.showSelect()
    print("=" * 30)
    if obj1.autoAi == True:
        #为测试方便，都指定为1
        command = '1'
        assist.show.petThink(obj1.getName())
        time.sleep(3)
    elif obj1.autoAi == 'lost':
        command = '1'
        print("%s 正处于某种强大的状态,从而暂时失去控制" % obj1.getName())
        time.sleep(3)
    else:
        print("玩家请选择指令：")
        command = input(">>")
    if command == '1':
        if obj1.autoAi == True:
            assist.show.petSelectSkill(obj1.getName())
            time.sleep(3)
            try:
                skill_number = random.choice(rancom.canChoiceList(obj1))
            except IndexError:
                print("%s 陷入了自我挣扎~" % obj1.getName())
                obj1.hp = 0
                assist.show.petDie(obj1)
                assist.show.battleOver()
                return True
        elif obj1.autoAi == 'lost':
            skill_number = 'delay'
        else:
            for key, value in obj1.skill_list.items():
                if value != None and key != 'delay':
                    print("技能" + key, ":", value.show_name, ' PP:', value.pp_value)
            print('0','返回上级！')
            print("请选择使用的技能：")
            skill_number = input(">>")
            if skill_number == '0':
                print("返回上级")
                return battleRun(player,obj1,obj2,place)
            if skill_number not in obj1.skill_list:
                print("指令错误！")
                return battleRun(player,obj1,obj2,place)
            if not assist.ppvalue.ppCount(obj1.skill_list[skill_number]):
                print("指令失败,重新选择！")
                return battleRun(player,obj1, obj2,place)
            if obj1.skill_list[skill_number].use_condition != None:
                if obj1.skill_list[skill_number].use_condition not in obj1.status:
                    print("技能无法使用！")
                    return battleRun(player,obj1,obj2,place)
            if obj1.skill_list[skill_number].limit_skill:
                if obj1.last_used_skill:
                    print("技能无法使用！")
                    return battleRun(player, obj1, obj2, place)
            if obj1.skill_list[skill_number].lock:
                print("技能被锁,无法使用！")
                return battleRun(player,obj1,obj2,place)
            if 'ST122' in obj1.status:
                if obj1.skill_list[skill_number].spell_skill == None:
                    print("技能无法使用！")
                    return battleRun(player,obj1,obj2,place)
        #记录最后使用的技能
        obj1.last_used_skill = obj1.skill_list[skill_number]
        # 战斗前的buff
        #asscount.checkBuffBeforeBattle(obj1, obj2)
        # 道具检查
        assist.show.useSkill(obj1,obj1.skill_list[skill_number])
        print(obj1.skill_list[skill_number]) #显示技能描述;'
        #检查畏缩 优先级最高
        if statusmap.checkShrinkaOrNot(obj1):
            # 回合结束检查是否中毒  中毒死亡
            if not statusmap.checkStatusAfterTurn(obj1,place):
                assist.show.petDie(obj1)
                assist.show.battleOver()
                return True

            assist.show.printTurn(obj2)
            return battleRun(player,obj2,obj1,place)
        #异常状态
        if statusmap.checkStatusBeforeBattle(obj1,obj1.skill_list[skill_number]):
            # 回合结束检查是否中毒  中毒死亡
            if not statusmap.checkStatusAfterTurn(obj1,place):
                assist.show.petDie(obj1)
                assist.show.battleOver()
                return True

            assist.show.printTurn(obj2)
            return battleRun(player,obj2,obj1,place)
        #检查是否混乱,会攻击自己
        if statusmap.checkChaosOrNot(obj1):
            damage = skilldamage.chaosDamage(obj1.level,obj1.getAttack(),obj1.getDefense())
            print("%s 混乱中, 对自己造成了 %s 伤害" % (obj1.getName(),damage))
            obj1.hp -= damage
            if obj1.hp <= 0:
                assist.show.petDie(obj1)
                assist.show.battleOver()
                return True
            else:
                # 回合结束检查是否中毒  中毒死亡
                if not statusmap.checkStatusAfterTurn(obj1,place):
                    assist.show.petDie(obj1)
                    assist.show.battleOver()
                    return True
                assist.show.printTurn(obj2)
                return battleRun(player,obj2,obj1,place)


        #命中与否判断
        hit = obj1.skill_list[skill_number].hit_rate
        #判断命中是否提高 携带物品
        try:
            hit_up = propmap.checkCarryPropForHit(obj1)
            print("命中提高: ", hit_up)
        except AttributeError:
            hit_up = 0

        if obj1.skill_list[skill_number].skill_code not in ['N064']:
            try:
                dodge_up = propmap.checkCarryPropFoeDodge(obj2)
            except AttributeError:
                dodge_up = 0
        else:
            dodge_up = 0
        print("闪避提高: ",dodge_up)
        #状态检查 命中降低或者提高
        hit = statusmap.checkStatusHitIndexBeforeBattle(obj1,hit)
        print("真实命中: ",hit+hit_up)
        #多段技能结算
        if obj1.skill_list[skill_number].multi_step == False:
            try:
                if obj1.skill_list[skill_number].one_hit_kill:
                    if battle.hitrate.hitForOneHitKill(obj1,obj2,obj1.skill_list[skill_number]):
                        print("%s 一击必杀" % obj1.getName())
                        obj2.hp = 0
                        assist.show.petDie(obj2)
                        assist.show.battleOver()
                        return True
                    else:
                        print("%s 技能使用失败！" % obj1.getName())
                        # 回合结束检查是否中毒  中毒死亡
                        if not statusmap.checkStatusAfterTurn(obj1, place):
                            assist.show.petDie(obj1)
                            assist.show.battleOver()
                            return True

                        assist.show.printTurn(obj2.getName())
                        return battleRun(player, obj2, obj1, place)
            except AttributeError:
                pass
            if not battle.hitrate.hitOrNot(obj1.skill_list[skill_number],hit + hit_up,obj1,obj2,obj2.dodge + dodge_up):
                #清0
                try:
                    if obj1.skill_list[skill_number].power_change_by_hit:
                        obj1.skill_list[skill_number].hit_count = 0
                except AttributeError:
                    pass
                #未命中状态回合增加
                statusmap.statusTurnsAddIfNotHit(obj1)

                #asscount.checkBuffAfterBattle(obj1)
                # 回合结束检查是否中毒  中毒死亡
                if not statusmap.checkStatusAfterTurn(obj1,place,hit_or_not=False):
                    assist.show.petDie(obj1)
                    assist.show.battleOver()
                    return True
                assist.show.printTurn(obj2.getName())
                return battleRun(player,obj2,obj1,place)
            #命中计数
            try:
                if obj1.skill_list[skill_number].power_change_by_hit:
                    obj1.skill_list[skill_number].hit_count += 1
            except:
                pass
            #改写结算 直接把技能扔进去
            if damageCount(obj2,obj1,obj1.skill_list[skill_number],place):
                # 回合结束检查是否中毒  中毒死亡
                if not statusmap.checkStatusAfterTurn(obj1,place):
                    assist.show.petDie(obj1)
                    assist.show.battleOver()
                    return True
                assist.show.printTurn(obj2.getName())
                return battleRun(player,obj2,obj1,place)
            else:
                return True
        #多段
        else:
            counts = obj1.skill_list[skill_number].getStepOfSkill()
            for count in range(counts):
                print("第 %s 次 攻击 " % (count+1))
                print("=" * 30)
                if battle.hitrate.hitOrNot(obj1.skill_list[skill_number], hit + hit_up, obj1, obj2,obj2.dodge + dodge_up):
                    if not damageCount(obj2, obj1, obj1.skill_list[skill_number],place):
                        return True
                else:
                    continue
                time.sleep(1)

            if not statusmap.checkStatusAfterTurn(obj1,place):
                assist.show.petDie(obj1)
                assist.show.battleOver()
                return True
            assist.show.printTurn(obj2.getName())
            return battleRun(player, obj2, obj1,place)

    elif command == '2':
        #交换精灵模块
        if statusmap.checkNoChange(obj1):
            if changepet.changePet(player):
                statusmap.resetStatusAfterChange(obj1)
                #加一个经验状态减半的效果 ST999 经验减半
                #obj2.exp_status.append('ST999')
                #因未返回到explore层，换精灵结算顺序正常
                return battering.battleing(player,obj2,change_pet=True,place=place)
            else:
                return battleRun(player,obj1,obj2,place)
        else:
            print("%s 无法被替换的状态" % obj1.getName())
            return battleRun(player,obj1,obj2,place)

    elif command == '4':
        assist.show.petUseRun(obj1.getName())
        if statusmap.checkUnlockOrNot(obj1):
            x = random.randint(1,100)
            if x in range(1,100):
                print("逃跑成功")
                player.battle_run_success = True
                return True
        else:
            print("%s 被锁定了！ 无法脱逃 ~" % obj1.getName())
        print("逃跑失败")
        assist.show.printTurn(obj2.getName())
        return battleRun(player,obj2,obj1,place)

    elif command == '3':
        #测试 得到一个道具
        #propmap.getProp(propmap.prop_dict['五彩迷光'])
        use_or_not = bag.showBattleBagOrNot(player,obj2)
        if use_or_not == True:
            if obj2.captured == False:
                # 回合结束检查是否中毒  中毒死亡
                if not statusmap.checkStatusAfterTurn(obj1,place):
                    assist.show.petDie(obj1)
                    assist.show.battleOver()
                    return True
                assist.show.printTurn(obj2)
                return battleRun(player,obj2,obj1,place)
            else:
                #捕获成功 战斗结束
                return True
        elif use_or_not == None:
            return battleRun(player,obj1, obj2,place)
        else:
            #print("重新选择！")
            #assist.show.printTurn(obj2)
            if not statusmap.checkStatusAfterTurn(obj1,place):
                assist.show.petDie(obj1)
                assist.show.battleOver()
                return True
            return battleRun(player,obj2, obj1,place)

    else:
        print("指令错误!")
        return battleRun(player,obj1,obj2,place)

