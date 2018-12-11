import battle.skilllistmap
import assist.show

import time

def learnSkill(obj,skill_code):
    #判断是否已经领悟
    if skill_code in obj.realize_skill_list:
        return False

    if skill_code[0] not in obj.can_learn_skills:
        print("属性不符合，无法学习该系别技能")
        return False

    print("%s 领悟了 %s 技能！" % (obj.name, battle.skilllistmap.skill_dict[skill_code].skill_show_name))
    for key in ['1','2','3','4']:
        if key not in obj.skill_list:
            obj.skill_list[key] = battle.skilllistmap.skill_dict[skill_code]
            obj.realize_skill_list.append(skill_code)
            return True


    print("技能格已满！")

    print("请选择要遗忘的技能：")
    assist.show.showPetSkills(obj)
    forget_id = input(">")

    print("正在遗忘",obj.skill_list[forget_id].skill_show_name,'技能！')
    time.sleep(3)
    obj.skill_list[forget_id] = battle.skilllistmap.skill_dict[skill_code]

    #加入已经领悟的列表
    obj.realize_skill_list.append(skill_code)
    return True