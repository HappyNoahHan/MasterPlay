import battle.skill
#old verson skill setting
#技能列表与代号
#当实例里面有参数有使用次数 用同一个类实例会出现问题
#2.0 pp value 内部固定

skill_dict = {
    'A001': battle.skill.fireBall,
    'A004': battle.skill.fireSpin,
    'A009': battle.skill.flameAffinity,
    'N001': battle.skill.scream,
    'N002': battle.skill.steadiness,
    'N003': battle.skill.strengthCre,
    'B002': battle.skill.azorLeaf,
    'B003': battle.skill.lifeRecovery,
    'B004': battle.skill.lifeChains,
    'B005': battle.skill.vinesTied,
    'S001': battle.skill.illuminatiom,
    'S002': battle.skill.HolyLight,
    'T001': battle.skill.disperse,
    'T002': battle.skill.threaten,
    'C001': battle.skill.StunSpore,
    'C002': battle.skill.SleepingPowder,
    'D001': battle.skill.WaterJump,
    'D002': battle.skill.WaterBall,
    'D003': battle.skill.WaterCannon,

}

#背包概念 名称 数量
skill_bag_dict={
    1:[skill_dict['A001'],99],
    2:[skill_dict['C002'],99],
}

#得到技能道具
def getSkill(skill_code,number = 1):
    print("获得了 %s X %d !" % (skill_dict[skill_code].show_name,number))
    for key,value in skill_bag_dict.items():
        if value[0] == skill_dict[skill_code]:
            value[1] += number
            return True

    for key in range(1,101):
        if key not in skill_bag_dict:
            skill_bag_dict[key] = [skill_dict[skill_code],number]
            return True

    return False
