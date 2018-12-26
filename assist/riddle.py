riddle_dict={
    '迷途少女': ('3',True),
}


def openTheRiddle(trainer):
    '''
    解锁 解开谜语
    :param trainer:
    :return:
    '''
    return riddle_dict[trainer.name]