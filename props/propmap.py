from props import  prop

prop_dict ={
    '攻击之爪': prop.PropertyUpProp(per=1.3,up_type='attack')
}


def checkCarryProp(obj):
    if obj.carry_prop.prop_type == 'basic':
        if obj.carry_prop.up_type == 'attack':
            obj.attack = obj.carry_prop.propCarry(obj.attack)
        elif obj.carry_prop.up_type == 'defense':
            obj.defense = obj.carry_prop.propCarry(obj.defense)
        elif obj.carry_prop.up_type == 'spell_power':
            obj.spell_power = obj.carry_prop.propCarry(obj.spell_power)
        elif obj.carry_prop.up_type == 'spell_defense':
            obj.spell_defense = obj.carry_prop.propCarry(obj.spell_defense)
        elif obj.carry_prop.up_type == 'speed':
            obj.speed = obj.carry_prop.propCarry(obj.speed)
        else:
            return False

    return True