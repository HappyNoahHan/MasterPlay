from place import hospital,town,village,grassfrom,wildpetlist,treasure,shop,petgym
from players import  npcmap
from assist import prize
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

town_map_for_green={
    '1': [shop.Shop(name='绿叶百货',npc_list=npcmap.shop_npc_list_for_green_town,prize_box_list=prize.prize_box_for_green_town_shop),True],
    '2': [hospital.Hospital(name="绿叶医疗中心",npc_list=npcmap.hospital_npc_list_for_green_town),True],
    '3': [petgym.PetGym(name='绿叶道馆',npc_list=npcmap.petgym_npc_list_for_green_town,prize_box_list=None),True]
}



village_map_for_start={

        '1': [town.Town(name='绿叶镇',maplist=town_map_for_green),True],
        '2': [grassfrom.Grassform(name='绿叶大道',
                                    maplist=grassfrom_map_for_no_1,
                                 wild_pet_list=wildpetlist.wild_pet_list_in_grass_no_1,
                                 treasure_box_list=treasure.treasure_box_for_grass_no_1,
                                 npc_list = npcmap.trainer_in_grass_no_1),True],
}



