from pets import fly,fire,wood
from players import play,battering
from battle import skill



if __name__ == '__main__':
    #for test
    a = fire.Charmander(level=1,skill_list={'1':skill.fireBall()},has_trainer=True,autoAi=False)
    b = fire.Charmeleon(level=10,skill_list={'1':skill.fireBall()},has_trainer=True,autoAi=False)
    c = fire.Charmeleon(level=15,skill_list={'1':skill.fireBall()},has_trainer=True,autoAi=False)
    pet_list = {
        'Master': c,
        '1': a,
        '2': b,
    }
    player = play.Player(name='小智',pet_list=pet_list)


    print("Welcome to Pet Master World!")
    print("Command 9 or bag to open the bag！")

    player.current_place.showMap(player)






