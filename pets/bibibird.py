import pets.pet
import battle.skill

class WildBBBird(pets.pet.Pet):
    talent_skills = battle.skill.scream()
    autoAi = True

    skill_list = {
       '1': talent_skills,
    }