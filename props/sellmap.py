sell_dict = {


    'SELL01':[{
        '1': ('精灵球',100),
        '2': ('火焰球',200)
    },'petball'],

    'SELL02':[{
        '1': ('精灵球', 100),
        '2': ('火焰球', 200)

    },'petball'],#如果字典后面有逗号会报错，会成为1个元组

}


def getSellList(sell_id):
    return sell_dict[sell_id][0]

def getSellType(sell_id):
    return sell_dict[sell_id][1]