from pets import fly,fire,wood
from players import play,battering
from battle import skill



if __name__ == '__main__':
    #for test
    a = fire.Charmander(level=1,skill_list={'1':skill.fireBall()},has_trainer=True,autoAi=False)
    b = fire.Charmeleon(level=10,skill_list={'1':skill.fireBall()},has_trainer=True,autoAi=False)
    c = fire.Charmeleon(level=15,skill_list={'1':skill.fireBall(),'2':skill.fireSpin(),'3':skill.JetFlame()},has_trainer=True,autoAi=False)
    pet_list = {
        'Master': c,
        '1': a,
        '2': b,
    }
    player = play.Player(name='小智',pet_list=pet_list)


    print("Welcome to Pet Master World!")
    print("Command bag to open the bag！")
    print("Command back to back up!")
    print("Command pet to open pet system")

    player.current_place.showMap(player)






