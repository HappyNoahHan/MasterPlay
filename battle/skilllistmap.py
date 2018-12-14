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
    1:[skill_dict['A001'],1],
    2:[skill_dict['C002'],2],
}
