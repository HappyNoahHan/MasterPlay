from pets import status
from assist import rancom,life,weathermap

import time
'''
    eg:ST009   麻痹 技能无法使用
'''

status_dict={
    'ST001' : status.Cauma(),
    'ST002' : status.Paralysis(),
    'ST003' : status.Sleeping(),
    'ST004' : status.Shrink(),
    'ST005' : status.BigPoisoning(),
    'ST006' : status.Chaos(),
    'ST007' : status.Poisoning(),
    'ST008' : status.Frozen(),
    'ST009' : status.ArmorBreak(), #破甲 防御降低
    'ST010' : status.Bound(),
    'ST011' : status.GuardBreak(), #特防降低
    'ST012' : status.PowerSave(),
    'ST013' : status.HitDown(), #命中降低
    'ST014' : status.Satiate(),
    'ST015' : status.PropUp(status_show_name='命中提升',status_code='ST015',status_info='攻击者技能命中提升'),
    'ST016' : status.PropUp(status_show_name='攻击提升',status_code='ST016',status_info='攻击者攻击能力提升'),
    'ST017' : status.PropUp(status_show_name='防御提升',status_code='ST017',status_info='攻击者防御能力提升'),
    'ST018' : status.PropUp(status_show_name='特攻提升',status_code='ST018',status_info='攻击者特攻能力提升'),
    'ST019' : status.PropUp(status_show_name='特防提升',status_code='ST019',status_info='攻击者特防能力提升'),
    'ST020' : status.PropUp(status_show_name='速度提升',status_code='ST020',status_info='攻击者速度能力提升'),
    'ST021' : status.PropDown(status_show_name='攻击降低',status_code='ST021',status_info='攻击者攻击能力降低'),
    'ST022' : status.PropDown(status_show_name='特攻降低',status_code='ST022',status_info='攻击者特攻能力降低'),
    'ST023' : status.PropDown(status_show_name='速度降低',status_code='ST023',status_info='攻击者速度能力降低'),
    'ST027' : status.DodgeUp(),
    'ST028' : status.DodgeDown(),
    'ST024' : status.Fly(),
    'ST025' : status.Vulnerability(),
    'ST026' : status.LuckyUp(),
    'ST029' : status.HealBlock(),
    'ST030' : status.NoLucky(),
    'ST031' : status.Place(status_show_name='青草场地',status_code='ST031',
                           status_info='5回合内所有站地面上的宝可梦每回合回复少许体力。草属性招式的威力提升50%',
                           place_property='wood',place_type='power'),
    'ST032' : status.WaterSport(status_show_name='玩水',status_code='ST032',
                           status_info='玩水状态持续5回合。全场宝可梦使用的火属性招式威力×1⁄2',
                           place_property='water',place_type='power'),
    'ST033' : status.LightScreen(status_show_name='光墙',status_code='ST033',
                                 status_info='在５回合内，受到的特殊攻击威力会减半',
                                 place_type='damage'),
    'ST034' : status.Place(status_show_name='电气场地',status_code='ST034',
                           status_info='任何地面上的宝可梦的电属性招式威力将会提高50%,并且不会陷入睡眠状态以及瞌睡状态',
                           place_property='electric',place_type='power'),
    'ST035' : status.MudSport(status_show_name='玩泥巴',status_code='ST035'
                              ,status_info='在５回合内,电属性的招式威力会减半',
                              place_property='ground',place_type='power'),
    'ST036' : status.RainDance(status_show_name='求雨',status_code='ST036',
                               status_info='在５回合内一直降雨,从而提高水属性的招式威力,火属性的招式威力则降低',
                               place_property='water',place_type='power'),
    'ST100' : status.NoTalent(),
    'ST099' : status.Lock(),
    'ST098' : status.KnockOff(),
    'ST097' : status.ChangePro(),
    'ST096' : status.AquaRing(),
    'ST095' : status.PropChangeTemp(status_show_name='浸水',status_code='ST095',
                                    status_info='将大量的水泼向对手,从而使其变成水属性',
                                    change_prop='water'),
    'ST094' : status.PropChangeTemp(status_show_name='保护色',status_code='ST094',
                                    status_info='根据所在场所不同,改变属性',
                                    change_prop='water'),#后续 加一个根据场地的变化的函数
    'ST101' : status.Whirlwind(),
    'ST102' : status.PetalDance(),
    'ST103' : status.SolarBeam(),
    'ST104' : status.Lockon(),
    'ST105' : status.Minimize(),
    'ST106' : status.Disable(),
    'ST107' : status.MagnetRise(),
    'ST108' : status.Rollout(),
    'ST109' : status.SmackDown(),
    'ST110' : status.DefenseCurl(),
    'ST111' : status.LeechSeed(),
    'ST112' : status.WorrySeed(),
    'ST113' : status.SkullBash(),
    'ST114' : status.Safeguard(),
    'ST115' : status.FuryCutter(),
    'ST116' : status.Dig(),
    'ST117' : status.Thrash(),
    'ST118' : status.Imprison(),
    'ST119' : status.Grudge(),
    'ST120' : status.Whirlwind(),
    'ST121' : status.Identified(),
    'ST122' : status.Taunt(),
}

#清理清单
clear_list = []
for key,value in status_dict.items():
    clear_list.append(key)

clear_list.remove('ST005')
clear_list.remove('ST007')
clear_list.remove('ST102')

#回合递减
count_index_list=['ST029','ST030','ST106','ST104','ST107','ST114','ST119','ST120','ST122']

#异常状态
abnormal_list = ['ST001','ST002','ST003',
                 'ST005','ST007','ST008']

#所以状态
all_status_list = [ x[0] for x in status_dict.items()]


def checkStatusAfterBattle(obj,skill,damage):
    damage_index = damage
    for key,value in obj.status.items():
        if key == 'ST001':
            if not skill.spell_skill:
                print("物理招式，伤害减半")
                damage_index = round(damage_index / 2)

    return damage_index

def checkParalysisOrNot(obj):
    '''
    检查是否是麻痹状态 有1/4几率无法成功使用技能
    :param obj:
    :return:
    '''
    if 'ST002' in obj.status:
        if status_dict['ST002'].statusEffect():
            print("%s 处于麻痹状态,技能使用失败!" % obj.getName())
            return True
    return False

def checkSleepingOrNot(obj):
    '''
    检查是否是睡眠状态
    :param obj:
    :return:
    '''
    if 'ST003' in obj.status:
        if obj.status['ST003'] > 2 and obj.status['ST003'] <= 4:
            if status_dict['ST003'].statusEffect():
                print("%s 清醒了！" % obj.getName())
                removeStatus(obj,'ST003')
                return False

        elif obj.status['ST003'] > 4:
            removeStatus(obj,'ST003')
            return False
        elif obj.status['ST003'] == 2:
            if status_dict['ST003'].status_giver[1].skill_code == 'S013':
                print("%s 清醒了！" % obj.getName())
                removeStatus(obj, 'ST003')
                return False

        obj.status['ST003'] += 1
        return True

    return False

def checkShrinkaOrNot(obj):
    '''
    检查畏缩状态
    :param obj:
    :return:
    '''
    if 'ST004' in obj.status:
        print("%s 畏缩不前,没有做出任何动作！" % obj.getName())
        return True
    return False

def checkStatusBeforeBattle(obj,skill):
    #技能解除异常状态
    if skill.skill_code in ['B013','I001','S013']:
        return False

    if obj.status:
        if checkParalysisOrNot(obj):
            print("%s 被麻痹,没有成功使用技能~" % obj.getName())
            return True
        if checkSleepingOrNot(obj):
            print("%s 睡眠中,无法使用技能~" % obj.getName())
            time.sleep(3)
            return True
        #if checkShrinkaOrNot(obj):
            #print("%s 畏缩不前,没有成功使用技能~" % obj.name)
        #    return True
        if checkFrozenOrNot(obj,skill):
            print("%s 冰冻中, 无法使用任何技能" % obj.getName())
            return True
    else:
        print("%s 没有处于任何状态！" % obj.getName())
    return False

def checkStatusAfterTurn(obj,place,hit_or_not = True): #默认技能命中
    '''
    检查回合结束 中毒 灼伤 伤害
    水流环 等回复HP 状态
    :param obj:
    :return:
    '''
    if 'ST005' in obj.status:
        damage = status_dict['ST005'].statusEffect(obj.status['ST005'],obj._max_health)
        print("%s 中毒损失了 %s HP" % (obj.getName(),damage))
        obj.hp -= damage
        if obj.hp <= 0:
            return False
        #obj._max_health -= damage
        obj.status['ST005'] += 1

    if 'ST007' in obj.status:
        damage = status_dict['ST007'].statusEffect(obj._max_health)
        print("%s 中毒损失了 %s HP" % (obj.getName(), damage))
        obj.hp -= damage
        if obj.hp <= 0:
            return False

    if 'ST001' in obj.status:
        damage = status_dict['ST001'].statusEffect(obj._max_health)
        print("%s 因灼伤损失了 %s HP" % (obj.getName(), damage))
        obj.hp -= damage
        if obj.hp <= 0:
            return False

    if 'ST111' in obj.status:
        damage = status_dict['ST111'].statusEffect(obj._max_health)
        print("%s 因寄生种子损失了 %s HP" % (obj.getName(), damage))
        obj.hp -= damage
        if status_dict['ST111'].status_giver[0].alive:
            life.healthRecoreByDrug(status_dict['ST111'].status_giver[0],damage)
        if obj.hp <= 0:
            return False


    if 'ST010' in obj.status:
        if obj.status['ST010'] > 4:
            removeStatus(obj,'ST010')
            return True
        elif obj.status['ST010'] == 4:
            if rancom.statusRandom(50):
                removeStatus(obj,'ST010')
                return True
        obj.status['ST010'] += 1
        damage = status_dict['ST010'].statusEffect(obj._max_health)
        print("%s 因束缚损失了 %s HP" % (obj.getName(), damage))
        obj.hp -= damage
        if obj.hp <= 0:
            return False

    if 'ST004' in obj.status:
        removeStatus(obj,'ST004')

    if place.place_status:
        if place.place_status[0] == 'ST031':
            life.healthRecoverBySkill(obj,1/16)

    if 'ST096' in obj.status:
        life.healthRecoverBySkill(obj,1/16)

    #回合生效的状态-1
    for status in count_index_list:
        if status in obj.status:
            obj.status[status] -= 1
            if obj.status[status] == 0:

                if status == 'ST106': #定身法效果解除
                    for key,skill in obj.skill_list.items():
                        skill.lock = False

                removeStatus(obj, status)

    if place.place_status:
        place.place_status[1] -= 1
        if place.place_status[1] == 0:
            place.place_status = None

    if 'ST115' in obj.status:
        if obj.last_used_skill.skill_code != 'C012':
            removeStatus(obj,'ST115')
        if not hit_or_not:
            removeStatus(obj, 'ST115')

    #检查天气情况
    if place.weather != None:
        weathermap.weather_dict[place.weather].weatherEffect(obj)
        if obj.hp < 0:
            return False

        weathermap.weather_dict[place.weather].turns -= 1
        if weathermap.weather_dict[place.weather].turns == 0:
            weathermap.weather_dict[place.weather].turns = weathermap.weather_dict[place.weather]._max_turns
            print("%s 天气结束～～" % weathermap.weather_dict[place.weather].name)
            place.weather = None

    return True


def removeStatus(obj,status_code):
    '''
    移除状态 药品 技能等
    :param obj:
    :param status_code:
    :return:
    '''
    #全能解状态药剂
    #print("使用解除剂")
    if status_code != None:
        if status_code == 'all':
            obj.status.clear()
            return True

        if status_code == 'abnormal':
            for st in abnormal_list:
                if st in obj.status:
                    obj.removeStatus(st)
                    print("%s 解除了 %s 状态：" % (obj.getName(), status_dict[st].status_show_name))
            return True

        if status_code in obj.status:
            obj.removeStatus(status_code)
            print("%s 解除了 %s 状态：" % (obj.getName(), status_dict[status_code].status_show_name))
        else:
            print("并没有什么效果~")

    return True

def checkUnlockOrNot(obj):
    '''
    lock bound 状态下无法逃走
    :param obj:
    :return:
    '''
    if 'ST099' in obj.status or 'ST010' in obj.status:
        return False
    return True

def checkChaosOrNot(obj):
    if 'ST006' in obj.status:
        if obj.status['ST006'] > 2 and obj.status['ST006'] < 5:
            if rancom.statusRandom(25): #1/4 几率自我解除
                print("%s 解除了混乱状态~" % obj.getName())
                removeStatus(obj,'ST006')
                return False

        elif obj.status['ST006'] >= 5:
            print("%s 解除了混乱状态~" % obj.getName())
            removeStatus(obj,'ST006')
            return False

        obj.status['ST006'] += 1
        if status_dict['ST006'].statusEffect():
            return True

    return False


def checkStatusEnd(player):
    '''
    战斗结束之后 检查状态 主要使将某些状态减弱 剧毒-->中毒
    :param player:
    :return:
    '''
    for key,pet in player.pet_list.items():
        if 'ST005' in pet.status:
            removeStatus(pet,'ST005')
            pet.setStatus('ST007')

        if 'ST102' in pet.status:
            removeStatus(pet,'ST102')
            pet.autoAi = False

        if 'ST103' in pet.status:
            removeStatus(pet,'ST103')
            pet.autoAi = False

        if 'ST113' in pet.status:
            removeStatus(pet,'ST113')
            pet.autoAi = False

        if 'ST117' in pet.status:
            removeStatus(pet,'ST117')
            pet.autoAi = False

        if 'ST108' in pet.status:
            removeStatus(pet,'ST108')
            pet.autoAi = False
            for key,skill in pet.skill_list.items():
                try:
                    if skill.power_change_by_hit:
                        skill.hit_count = 0
                except:
                    pass

        if 'ST118' in pet.status:
            removeStatus(pet,'ST118')
            for key,skill in pet.skill_list.items():
                skill.lock = False

        for status in clear_list:
            if status in pet.status:
                removeStatus(pet,status)

        pet.last_used_skill = None #最后使用的技能

def resetStatusAfterChange(pet):
    '''
    交换后重置剧毒状态回合
    :param pet:
    :return:
    '''
    if 'ST005' in pet.status:
        pet.setStatus('ST005')

    if 'ST095' in pet.status:
        removeStatus(pet,'ST095')

def checkFrozenOrNot(obj,skill):
    '''
    检查是否是冰冻状态
    :param obj:
    :return:
    '''
    if skill.skill_code in ['A007']:
        return False

    if 'ST008' in obj.status:
        if status_dict['ST008'].statusEffect():
            print("%s 解除了 冰冻！" % obj.getName())
            removeStatus(obj,'ST008')
            return False
        return True
    return False

def checkArmorBreakOrNot(obj,defense):
    '''
    检查是否破甲
    :param obj:
    :return:
    '''
    if 'ST009' in obj.status:
        return status_dict['ST009'].statusEffect(defense,obj.status['ST009'])

    return defense

def checkNoChange(obj):
    if 'ST010' in obj.status:
        return False

    return True

def checkGuardBreakOrNot(obj,spell_defense):
    '''
    检查特防降低
    :param obj:
    :param spell_defense:
    :return:
    '''
    if 'ST011' in obj.status:
        return status_dict['ST011'].statusEffect(spell_defense,obj.status['ST011'])

    return spell_defense

def checkPowerSave(obj,defense,spell_defense):
    '''
    检查 蓄力
    :param obj:
    :param defense:
    :param spell_defense:
    :return:
    '''
    if 'ST012' in obj.status:
        return status_dict['ST012'].statusEffect(defense,spell_defense)
    return defense,spell_defense

def checkPropBeforeBattle(skill,obj_attack,obj_defense,attack,defense,spell_power,spell_defense,speed):
    if obj_attack.status:
        # 2.2 检查攻击提升
        attack = checkPropUpOrDown(obj_attack, attack, 'ST016')
        attack = checkPropUpOrDown(obj_attack,attack,'ST021')
        # 2.2 检查特攻击
        spell_power = checkPropUpOrDown(obj_attack,spell_power,'ST018')
        spell_power = checkPropUpOrDown(obj_attack,spell_power,'ST022')
        #2.2 检查速度降低或提高
        speed = checkPropUpOrDown(obj_attack,attack,'ST020')
        speed = checkPropUpOrDown(obj_attack,attack,'ST023')
        # 2.0 检查是否在麻痹状态下 速度减半
        if 'ST002' in obj_attack.status:
            speed = int(speed / 2)

    if obj_defense.status:
        if skill.skill_code not in ['N064']:
            # 2.0检查是否破甲
            defense = checkArmorBreakOrNot(obj_defense, defense)
            # 2.0检查破防
            spell_defense = checkGuardBreakOrNot(obj_defense, spell_defense)
            # 2.2 检查防御提升 特防
            defense = checkPropUpOrDown(obj_defense, defense, 'ST017')
            spell_defense = checkPropUpOrDown(obj_defense,spell_defense,'ST019')
            # 2.1 检查是否蓄力
            defense,spell_defense = checkPowerSave(obj_defense,defense,spell_defense)



    return attack,defense,spell_power,spell_defense,speed

#被替代
def checkHitDown(obj,hit):
    if 'ST013' in obj.status:
        return status_dict['ST013'].statusEffect(hit,obj.status['ST013'])
    return hit

def checkStatusHitIndexBeforeBattle(obj_attack,hit):
    #检查命中降低
    hit = checkPropUpOrDown(obj_attack,hit,'ST013')
    #检查命中提高
    hit = checkPropUpOrDown(obj_attack,hit,'ST015')

    return hit


def checkPropUpOrDown(obj,value,status_code):
    if status_code in obj.status:
        return status_dict[status_code].statusEffect(value,obj.status[status_code])
    return value


def checkDogeBeforHitCount(obj_defense,dodge):

    dodge = checkPropUpOrDown(obj_defense,dodge,'ST027')

    dodge = checkPropUpOrDown(obj_defense,dodge,'ST028')

    return dodge

def checkHealBlockOrNot(obj_attack):
    if 'ST029' in obj_attack.status:
        return True
    return False


def placeStatusPowerUp(skill,power,place):
    return status_dict[place.place_status[0]].statusEffect(skill,power)

def placeStatusDamageCheck(skill,place):
    #检查伤害
    return status_dict[place.place_status[0]].statusEffect(skill)


def checkDelayStatus(obj_attack):
    '''
    0: 检查不到 1：true 状态中 正常结算 2：false 状态结束 正常结算 3：第一次 下回合结算
    :param obj_attack:
    :return:
    '''
    if 'ST102' in obj_attack.status:
        if status_dict['ST102'].statusEffect(obj_attack.status['ST102']):
            #obj_attack.status['ST102'] += 1
            return 2
        else:
            obj_attack.status['ST102'] += 1
            return 1
    elif 'ST117' in obj_attack.status:
        if status_dict['ST117'].statusEffect(obj_attack.status['ST117']):
            #obj_attack.status['ST102'] += 1
            return 2
        else:
            obj_attack.status['ST117'] += 1
            return 1
    elif 'ST103' in obj_attack.status:
        return 3

    elif 'ST113' in obj_attack.status:
        return 3

    elif 'ST116' in obj_attack.status:
        return 3

    elif 'ST108' in obj_attack.status:
        if status_dict['ST108'].statusEffect(obj_attack.status['ST108']):
            obj_attack.status['ST108'] += 1
            return 1
        else:
            return 3
    else:
        return 0

def statusTurnsAddIfNotHit(obj_attack):
    if 'ST108' in obj_attack.status:
        obj_attack.status['ST108'] += 1
        if obj_attack.status['ST108'] == 4:
            removeStatus(obj_attack,'ST108')
            obj_attack.autoAi = False


def getGainStatusFromDefenser(obj_attack,obj_defense):
    obj_attack.status = obj_defense.status
    for status in obj_attack.status.keys():
        if status in abnormal_list:
            obj_attack.removeStatus(status)
