def buffCount(obj):
    obj.tmp_defense = 0
    obj.tmp_attack = 0

    for key,value in obj.buff_dict.items():
        if key.skill_model == '0002':
            if value[0] > 0:
                obj.tmp_defense += value[1]
            else:
                value[1] = 0
        else:
            pass


def buffIndex(obj):
    for key,value in obj.buff_dict.items():
        if value[0] >= 1:
            value[0] -= 1
        else:
            obj.buff_dict.pop(key)
        print("buff 效果渐渐减弱")
        print(key.skill_show_name,value)
