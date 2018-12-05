import pets.pet
import battle.skill


class FireFox(pets.pet.Pet):

    talent_skills = battle.skill.fireBall()

    skill_list = {
        '1': talent_skills
    }

    debuff_dict = {}
    buff_dict = {}
    property_buff = {}

    property = ['fire']

    can_learn_skills = ['A','N']