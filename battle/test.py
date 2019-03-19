from battle import battle,asscount,skilldamage,hitrate
from assist import show,rancom
from pets import statusmap
from props import propmap
import time

def newbattle(player,obj_attack,obj_defense,attack_skill,defense_skill,place):

    if attack_skill.speed_level > defense_skill.speed_level:
        if not newBattleTrun(player, obj_attack, obj_defense, attack_skill, place):
            return False
        if not newBattleTrun(player, obj_defense, obj_attack, defense_skill, place):
            return False
    elif attack_skill.speed_level < defense_skill.speed_level:
        if not newBattleTrun(player, obj_defense, obj_attack, defense_skill, place):
            return False
        if not newBattleTrun(player, obj_attack, obj_defense, attack_skill, place):
            return False
    else:
        if obj_attack.getSpeed() >= obj_defense.getSpeed():
            if not newBattleTrun(player,obj_attack,obj_defense,attack_skill,place):
                return False
            if not newBattleTrun(player,obj_defense,obj_attack,defense_skill,place):
                return False
        else:
            if not newBattleTrun(player,obj_defense,obj_attack,defense_skill,place):
                return False
            if not newBattleTrun(player,obj_attack,obj_defense,attack_skill,place):
                return False

def newBattleTrun(player,obj1,obj2,skill,place):
    # 战斗前的buff
    asscount.checkBuffBeforeBattle(obj1, obj2)
    # 道具检查
    show.useSkill(obj1, skill)
    print(skill)  # 显示技能描述
    # 检查畏缩 优先级最高
    if statusmap.checkShrinkaOrNot(obj1):
        # 回合结束检查是否中毒  中毒死亡
        if not statusmap.checkStatusAfterTurn(obj1, place):
            show.petDie(obj1)
            show.battleOver()
            return False
    # 异常状态
    if statusmap.checkStatusBeforeBattle(obj1, skill):
        # 回合结束检查是否中毒  中毒死亡
        if not statusmap.checkStatusAfterTurn(obj1, place):
            show.petDie(obj1)
            show.battleOver()
            return False

    # 检查是否混乱,会攻击自己
    if statusmap.checkChaosOrNot(obj1):
        damage = skilldamage.chaosDamage(obj1.level, obj1.getAttack(), obj1.getDefense())
        print("%s 混乱中, 对自己造成了 %s 伤害" % (obj1.name, damage))
        obj1.health -= damage
        if obj1.health <= 0:
            show.petDie(obj1)
            show.battleOver()
            return False
        else:
            # 回合结束检查是否中毒  中毒死亡
            if not statusmap.checkStatusAfterTurn(obj1, place):
                show.petDie(obj1)
                show.battleOver()
                return False
    # 命中与否判断
    hit = skill.hit_rate
    # 判断命中是否提高 携带物品
    hit_up = propmap.checkCarryPropForHit(obj1)
    print("命中提高: ", hit_up)
    dodge_up = propmap.checkCarryPropFoeDodge(obj2)
    print("闪避提高: ", dodge_up)
    # 状态检查 命中降低或者提高
    hit = statusmap.checkStatusHitIndexBeforeBattle(obj1, hit)
    print("真实命中: ", hit + hit_up)
    # 多段技能结算
    if skill.multi_step == False:
        if skill.skill_model == '0018':
            if hitrate.hitForOneHitKill(obj1, obj2):
                print("%s 一击必杀" % obj1.name)
                obj2.health = 0
                show.petDie(obj2)
                show.battleOver()
                return False
            else:
                print("%s 技能使用失败！" % obj1.name)
                # 回合结束检查是否中毒  中毒死亡
                if not statusmap.checkStatusAfterTurn(obj1, place):
                    show.petDie(obj1)
                    show.battleOver()
                    return False

        if not hitrate.hitOrNot(skill, hit + hit_up, obj1, obj2, obj2.dodge + dodge_up):
            # 清0
            try:
                if skill.power_change_by_hit:
                    skill.hit_count = 0
            except:
                pass
            # 未命中状态回合增加
            statusmap.statusTurnsAddIfNotHit(obj1)

            asscount.checkBuffAfterBattle(obj1)
            # 回合结束检查是否中毒  中毒死亡
            if not statusmap.checkStatusAfterTurn(obj1, place):
                show.petDie(obj1)
                show.battleOver()
                return False
        # 命中计数
        try:
            if skill.power_change_by_hit:
                skill.hit_count += 1
        except:
            pass
        # 改写结算 直接把技能扔进去
        if battle.damageCount(obj2, obj1, skill, place):
            # 回合结束检查是否中毒  中毒死亡
            if not statusmap.checkStatusAfterTurn(obj1, place):
                show.petDie(obj1)
                show.battleOver()
                return False
        else:
            return False
    # 多段
    else:
        counts = rancom.getStepOfSkill()
        for count in range(counts):
            print("第 %s 次 攻击 " % (count + 1))
            print("=" * 30)
            if hitrate.hitOrNot(skill, hit + hit_up, obj1, obj2, obj2.dodge + dodge_up):
                if not battle.damageCount(obj2, obj1, skill, place):
                    return False
            else:
                continue
            time.sleep(1)

        if not statusmap.checkStatusAfterTurn(obj1, place):
            show.petDie(obj1)
            show.battleOver()
            return False