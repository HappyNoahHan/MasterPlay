from pets import fly,fire,wood,poison
from players import play,battering
from battle import skill
from props import berrymap,propmap



if __name__ == '__main__':
    #for test
    a = poison.Zubat(level=5,skill_list={'1':skill.StoredPower(),'2':skill.MudSport()},has_trainer=True,autoAi=False)
    c = fire.Charmeleon(level=5,skill_list={'1':skill.FlareBlitz()},has_trainer=True,autoAi=False)
    b = wood.Bellsprout(level=15,skill_list={'1':skill.Earthquake()},has_trainer=True,autoAi=False)
    a.berry = berrymap.berry_dict['零余果']
    a.carry_prop = propmap.prop_dict['攻击之爪']
    #a.setStatus('ST008',2)
    pet_list = {
        'Master': a,
        '1': b,
        '2': c,
    }
    player = play.Player(name='小智',pet_list=pet_list)


    print("Welcome to Pet Master World!")
    print("Command bag to open the bag！")
    print("Command back to back up!")
    print("Command pet to open pet system")

    player.current_place.showMap(player)






