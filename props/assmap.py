from props import stone

ass_dict = {
    '叶之石': stone.EvolveStone(name='叶之石'),
    '岩之心': stone.EvolveStone(name='岩之心'),
}

ass_bag_dict={
    1:[ass_dict['岩之心'],99]
}

def getAss(name,number = 1):
    print("获得了 %s X %d !" % (name,number))
    for key,value in ass_bag_dict.items():
        if value[0] == ass_dict[name]:
            value[1] += number
            return True

    for key in range(1,101):
        if key not in ass_bag_dict:
            ass_bag_dict[key] = [ass_dict[name],number]
            return True

    return False