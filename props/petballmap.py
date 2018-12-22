from props import petball
import random
petball_dict={
    '精灵球': petball.PetBall(ball_name='精灵球'),
    '绿叶球': petball.ProptyPetBall(ball_name='绿叶球',property='wood'),
    '火焰球': petball.ProptyPetBall(ball_name='火焰球',property='fire'),
    '大师球': petball.MasterPetBall(),
}

petball_bag_dict = {
    1: [petball_dict['精灵球'],5],
    2: [petball_dict['绿叶球'],1],
    3: [petball_dict['火焰球'],2],
    4: [petball_dict['大师球'],1],
}


def getPetBall(petball,number = 1):
    print("获得了 %s !" % petball.ball_name)
    for key,value in petball_bag_dict.items():
        if value[0] == petball:
            value[1] += number
            if value[1] > 99:
                value[1] = 99
            return True

    for key in range(1,101):
        if key not in petball_bag_dict:
            petball_bag_dict[key] = [petball,number]
            return True

    return False