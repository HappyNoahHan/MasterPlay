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
    'T001': battle.skill.disperse(pp=10),
    'T002': battle.skill.threaten(),

}



def useSkill(code):
    '''
    使用技能模块
    :param code:
    :return:
    '''

    skill_name = skill_dict[code]
    print("使用了 %s " % skill_name.skill_show_name)

    return skill_name.index_per,skill_name.skill_model

    #旧方法
    '''if skill_name.attack_skill:
        damage_coff = skill_name.damage_coefficient
        skill_name.showSkill()
        
        return damage_coff,skill_name.skill_model
    elif skill_name.defense_skill:
        skill_name.showSkill()
        
        return skill_name.defense_per,mode'''



def skillSelect(name):
    '''
    查找使用的技能
    :param name:
    :return:
    '''
    if name == '火球':
        skill_code = 'A001'
    if name == '尖叫':
        skill_code = 'N001'
    if name == '稳固':
        skill_code = 'N002'


    return useSkill(skill_code)