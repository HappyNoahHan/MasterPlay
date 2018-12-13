from props import  prop

prop_dict ={
    '攻击之爪': prop.PropertyUpProp(per=0.3,up_type='attack')
}


def checkCarryProp(obj):
    if obj.carry_prop != None:
        if obj.carry_prop.prop_type == 'basic':
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

    return True