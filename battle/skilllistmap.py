import battle.skill
#old verson skill setting
#技能列表与代号
skill_dict = {
    'A001': battle.skill.fireBall(),
    'N001': battle.skill.scream(),
    'N002': battle.skill.steadiness(pp=25),
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