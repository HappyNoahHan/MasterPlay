import battle.skill
#old verson skill setting
#技能列表与代号
#当实例里面有参数有使用次数 用同一个类实例会出现问题
#2.0 pp value 内部固定

skill_dict = {
    'A001': battle.skill.fireBall,
    'A004': battle.skill.fireSpin,
    'A005': battle.skill.JetFlame,
    'A009': battle.skill.flameAffinity,
    'F001': battle.skill.scream,
    'F002': battle.skill.WingAttack,
    'F003': battle.skill.AirCut,
    'F004': battle.skill.AirSword,
    'N001': battle.skill.Strike,
    'N002': battle.skill.Grab,
    'N003': battle.skill.Supersonic, #超音波
    'N004': battle.skill.HighSpeedStar,
    'N005': battle.skill.BlackEye,
    'B002': battle.skill.azorLeaf,
    'B003': battle.skill.lifeRecovery,
    'B004': battle.skill.lifeChains,
    'B005': battle.skill.vinesTied,
    'B006': battle.skill.Assimilate, #吸取
    'S001': battle.skill.illuminatiom,
    'I001': battle.skill.BlackFog,
    'T001': battle.skill.disperse,
    'T002': battle.skill.threaten,
    'T003': battle.skill.Bite,
    'C001': battle.skill.StunSpore,
    'C002': battle.skill.SleepingPowder,
    'D001': battle.skill.WaterJump,
    'D002': battle.skill.WaterBall,
    'D003': battle.skill.WaterCannon,
    'R001': battle.skill.DownRock,
    'R002': battle.skill.RockFall,
    'E001': battle.skill.Earthquake,
    'Q001': battle.skill.SingularLight,
    'Q002': battle.skill.Scare,
    'P001': battle.skill.Toxic,
    'P002': battle.skill.ToxicFang,
    'P003': battle.skill.VenomImpact,

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
