from players import npcmap

riddle_dict={
    'MAP0301': (['MAP0302','MAP0303'],[]),
    'MAP0302': (['MAP0303',],['MAP0301']),
    'MAP0303': ([],['MAP0301','MAP0302']),
}


def openTheRiddle(trainer_id,map_id):
    '''
    解锁 解开谜语 前后挑战顺序
    :param trainer:
    :return:
    '''
    open_riddle_lsit = riddle_dict[trainer_id]

    for id in open_riddle_lsit[0]:
        riddle_dict[id][1].remove(trainer_id)

    for id in open_riddle_lsit[0]:
        if len(riddle_dict[id][1]) == 0:
            npcmap.setNpcList(map_id,id)

