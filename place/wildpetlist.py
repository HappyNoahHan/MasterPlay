from  pets import fly,wood
from battle import skill
import random

wild_pet_list_for_grass_no1 = {
        wood.aiOodish(level=random.randint(3, 5), skill_list={'1': skill.scream()}): 50,
        fly.aiPidgey(level=random.randint(3, 5), skill_list={'1': skill.scream()}): 50,
    }

def meetWildPet(dict):
    '''
    遭遇野生精灵
    :param dict:
    :return:
    '''
    per_base = list(range(1, 101))
    number = random.randint(1,100)

    for key,value in dict.items():
        key.meeting_random_number=[]

        for i in range(0,value):
            x = random.choice(per_base)
            key.meeting_random_number.append(x)
            per_base.remove(x)

    for key,value in dict.items():
        if number in key.meeting_random_number:
            return key