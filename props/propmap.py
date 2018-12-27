from props import  prop

prop_dict ={
    '攻击之爪': prop.PropertyUpProp(per=0.3,up_type='attack',show_name='攻击之爪'),
    '火焰之心': prop.SkillPowerUpProp(pety='fire',power= 30,show_name='火焰之心'),
    '聚焦之眼': prop.SkillHitUpProp(hit_up=40,show_name='聚焦之眼'),
    '五彩迷光': prop.SkillHitDownProp(dodge=10,show_name='五彩迷光'),
}

#背包概念 名称 数量
prop_bag_dict={
    1:[prop_dict['攻击之爪'],1],
    #2:[prop_dict['火焰之心'],2],
}



def checkCarryPropForObj(obj):
    if obj.carry_prop != None:
        if obj.carry_prop.prop_type == 'basic':
            obj.prop_attack_up = 0
            obj.prop_defense_up = 0
            obj.prop_spell_power_up = 0
            obj.prop_spell_defense_up = 0
            obj.prop_speed_up = 0
            if obj.carry_prop.up_type == 'attack':
                obj.prop_attack_up = obj.carry_prop.propCarry(obj.attack)
                #print(obj.prop_attack_up)
            elif obj.carry_prop.up_type == 'defense':
                obj.prop_defense_up = obj.carry_prop.propCarry(obj.defense)
            elif obj.carry_prop.up_type == 'spell_power':
                obj.prop_spell_power_up = obj.carry_prop.propCarry(obj.spell_power)
            elif obj.carry_prop.up_type == 'spell_defense':
                obj.prop_spell_defense_up = obj.carry_prop.propCarry(obj.spell_defense)
            elif obj.carry_prop.up_type == 'speed':
                obj.prop_speed_up = obj.carry_prop.propCarry(obj.speed)
    else:
        pass

def checkCarryPropForSkill(obj,skill):
    if obj.carry_prop != None:
        if obj.carry_prop.prop_type == 'skill':
            return obj.carry_prop.propCarry(skill)

    return 0

def checkCarryPropForHit(obj):
    if obj.carry_prop != None:
        if obj.carry_prop.prop_type == 'hit':
            return obj.carry_prop.propCarry()

    return 0

def checkCarryPropFoeDodge(obj):
    if obj.carry_prop != None:
        if obj.carry_prop.prop_type == 'dodge':
            return obj.carry_prop.propCarry()
    return 0

def getProp(prop_name,number = 1):
    print("获得了 %s !" % prop_name)
    for key,value in prop_bag_dict.items():
        if value[0] == prop_dict[prop_name]:
            value[1] += number
            return True

    for key in range(1,101):
        if key not in prop_bag_dict:
            prop_bag_dict[key] = [prop_dict[prop_name],number]
            return True

    return False