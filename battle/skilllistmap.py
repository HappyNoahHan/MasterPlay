import battle.skill
#old verson skill setting
#技能列表与代号
skill_dict = {
    'A001': battle.skill.fireBall(),
    'A004': battle.skill.fireSpin(pp=20),
    'A009': battle.skill.flameAffinity(pp=10),
    'N001': battle.skill.scream(),
    'N002': battle.skill.steadiness(pp=25),
    'N003': battle.skill.strengthCre(pp=20),
    'B002': battle.skill.azorLeaf(pp=20),
    'B003': battle.skill.lifeRecovery(pp=10),
    'B004': battle.skill.lifeChains(),
    'B005': battle.skill.vinesTied(pp=35),
    'S001': battle.skill.illuminatiom(pp=10),
    'S002': battle.skill.HolyLight(pp=5),
    'T001': battle.skill.disperse(pp=10),
    'T002': battle.skill.threaten(),
    'C001': battle.skill.StunSpore(pp=20),
    'C002': battle.skill.SleepingPowder(pp=20),

}

#背包概念 名称 数量
skill_bag_dict={
    #1:[skill_dict['A001'],1],
    #2:[skill_dict['C002'],2],
}

#得到技能道具
def getSkill(skill_code,number = 1):
    print("获得了 %s !" % skill_dict[skill_code].show_name)
    for key,value in skill_bag_dict.items():
        if value[0] == skill_dict[skill_code]:
            value[1] += number
            return True

    for key in range(1,101):
        if key not in skill_bag_dict:
            skill_bag_dict[key] = [skill_dict[skill_code],number]
            return True

    return False
