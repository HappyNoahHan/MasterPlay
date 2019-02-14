from props import petball
import random
petball_dict={
    '精灵球': petball.PetBall(show_name='精灵球'),
    '绿叶球': petball.ProptyPetBall(show_name='绿叶球',property='wood'),
    '火焰球': petball.ProptyPetBall(show_name='火焰球',property='fire'),
    '激流球': petball.ProptyPetBall(show_name='激流球',property='water'),
    '山岩球': petball.ProptyPetBall(show_name='山岩球',property='rock'),
    '闪电球': petball.ProptyPetBall(show_name='闪电球',property='electricity'),
    '飞禽球': petball.ProptyPetBall(show_name='飞禽球',property='fly'),
    '精英球': petball.PetBall(show_name='精英球',capture_index=1.2),
    '专家球': petball.PetBall(show_name='专家球',capture_index=1.5),
    '大师球': petball.MasterPetBall(),
}

petball_bag_dict = {
    1: [petball_dict['精灵球'],5],
    #2: [petball_dict['绿叶球'],1],
    #3: [petball_dict['火焰球'],2],
    4: [petball_dict['大师球'],99],
    #5: [petball_dict['厚土球'],9],
}


def getPetBall(petball_name,number = 1):
    print("获得了 %s X %d !" % (petball_name,number))
    for key,value in petball_bag_dict.items():
        if value[0] == petball_dict[petball_name]:
            value[1] += number
            if value[1] > 99:
                value[1] = 99
            return True

    for key in range(1,101):
        if key not in petball_bag_dict:
            petball_bag_dict[key] = [petball_dict[petball_name],number]
            return True

    return False