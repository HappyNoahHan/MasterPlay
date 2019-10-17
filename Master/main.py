from pets import newpets
from players import play,battering
from battle import skill
from props import berrymap,propmap



if __name__ == '__main__':
    #for test
    #a = poison.Zubat(level=5,skill_list={'1':skill.PsychUp(),'2':skill.Slam()},has_trainer=True,autoAi=False)
    a = newpets.Pet(23,level=5,skill_list={'1':skill.PsychUp(),'2':skill.Slam()})
    a.setautoAi(False)

    #a.berry = berrymap.berry_dict['零余果']
    #a.carry_prop = propmap.prop_dict['攻击之爪']
    #a.setStatus('ST029',2)
    pet_list = {
        'Master': a
    }
    player = play.Player(name='小智',pet_list=pet_list)
    a.setOwner(player.name)

    print("Welcome to Pet Master World!")
    print("Command bag to open the bag！")
    print("Command back to back up!")
    print("Command pet to open pet system")

    player.current_place.showMap(player)






