from props import petball
import random
petball_dict={
    '精灵球': petball.PetBall(),
}

petball_bag_dict = {
    1: [petball_dict['精灵球'],5]
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