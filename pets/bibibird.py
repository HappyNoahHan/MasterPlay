import pets.pet
import battle.skill

class WildBBBird(pets.pet.Pet):
    talent_skills = battle.skill.scream()
    autoAi = True

    skill_list = {
       '1': talent_skills,
    }

    debuff_dict = {}
    buff_dict = {}
    property_buff = {}

    property = ['fly','normal']

    can_learn_skills = ['N','F']