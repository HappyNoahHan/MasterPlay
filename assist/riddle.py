riddle_dict={
    '绿叶学徒A': ('2',True,'trainer'),
    '绿叶学徒B': ('3',True,'trainer'),
}


def openTheRiddle(trainer):
    '''
    解锁 解开谜语
    :param trainer:
    :return:
    '''
    return riddle_dict[trainer.name]