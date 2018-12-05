import battle.skilllistmap
import assist.show

import time

def learnSkill(obj,skill_code):
    for key in ['2','3','4']:
        if key not in obj.skill_list:
            obj.skill_list[key] = battle.skilllistmap.skill_dict[skill_code]
            return True

    print("请选择要遗忘的技能：")
    assist.show.showPetSkills(obj)
    forget_id = input(">")

    print("正在遗忘",obj.skill_list[forget_id].skill_show_name,'技能！')
    time.sleep(3)
    obj.skill_list[forget_id] = battle.skilllistmap.skill_dict[skill_code]

    return True




