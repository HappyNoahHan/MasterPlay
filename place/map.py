from place import hospital,town,village,grassfrom,wildpetlist,treasure
from players import  trainer
grassfrom_map_basic={
        '1':['野外探险',True],
        '2':['搜索玩家',True],
        '3':['寻宝',False],
}


grassfrom_map_for_no_1={
        '1':['野外探险',True],
        '2':['搜索玩家',True],
        '3':['寻宝',False],
        '4':[grassfrom.Grassform(name='2号草丛',
                                 maplist=grassfrom_map_basic,
                                 wild_pet_list=wildpetlist.wild_pet_list_in_grass_no_1,
                                 ),True],
}



village_map_for_start={
        '1': [hospital.Hospital(name="格林医疗中心"),True],
        '2': [town.Town(name='格林镇'),True],
        '3': [grassfrom.Grassform(name='1号草丛',
                                    maplist=grassfrom_map_for_no_1,
                                 wild_pet_list=wildpetlist.wild_pet_list_in_grass_no_1,
                                 treasure_box_list=treasure.treasure_box_for_grass_no_1,
                                 trainer_list = trainer.trainer_in_grass_no_1),True],
}



