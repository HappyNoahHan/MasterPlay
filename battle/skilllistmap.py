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
    'F001': battle.skill.StartWind, #起风
    'F002': battle.skill.WingAttack, #翅膀攻击
    'F003': battle.skill.AirSlash, #空气斩
    'F004': battle.skill.AirCutter, #空气利刃
    'N001': battle.skill.Strike,
    'N002': battle.skill.Grab,
    'N003': battle.skill.Supersonic, #超音波
    'N004': battle.skill.Swift, #高速星星
    'N005': battle.skill.MeanLook, #黑色目光
    'N006': battle.skill.Screech,#刺耳声
    'N007': battle.skill.Wrap,#紧束
    'N008': battle.skill.Leer,#瞪眼
    'N009': battle.skill.Glare,#大蛇瞪眼
    'N010': battle.skill.Stockpile,#蓄力
    'N011': battle.skill.Swallow,#吞下
    'N012': battle.skill.SpitUp,#喷出
    'B002': battle.skill.azorLeaf,
    'B003': battle.skill.lifeRecovery,
    'B004': battle.skill.lifeChains,
    'B005': battle.skill.vinesTied,
    'B006': battle.skill.Absorb, #吸取
    'S001': battle.skill.illuminatiom,
    'I001': battle.skill.Haze, #黑雾
    'T001': battle.skill.disperse,
    'T002': battle.skill.threaten,
    'T003': battle.skill.Bite, #咬住
    'T004': battle.skill.Crunch,#咬碎
    'C001': battle.skill.StunSpore,
    'C002': battle.skill.SleepingPowder,
    'C003': battle.skill.LeechLife, #吸血
    'D001': battle.skill.WaterJump,
    'D002': battle.skill.WaterBall,
    'D003': battle.skill.WaterCannon,
    'R001': battle.skill.DownRock,
    'R002': battle.skill.RockFall,
    'E001': battle.skill.Earthquake,#地震
    'E002': battle.skill.MudBomb,#泥巴炸弹
    'Q001': battle.skill.ConfuseRay, #奇异之光
    'Q002': battle.skill.Astonish, #惊吓
    'P001': battle.skill.Toxic, #剧毒
    'P002': battle.skill.PoisonFang, #剧毒牙
    'P003': battle.skill.Venoshock, #毒液冲击
    'P004': battle.skill.PoisonSting, #毒针
    'P005': battle.skill.Acid, #溶解液
    'P006': battle.skill.AcidSpray,#酸液炸弹
    'P007': battle.skill.GastroAcid,#胃液
    'P008': battle.skill.Belch,#打嗝
    'P009': battle.skill.Coil,#盘蜷

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
