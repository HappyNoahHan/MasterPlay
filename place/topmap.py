from place import hospital,wildform,wildpetlist,treasure,shop,petgym,village,town
from players import  npcmap
from assist import prize

top_map_dict={
    'MAP00' : village.Village(name='新手村',map_id='MAP00'),
    'MAP01' : shop.Shop(name='绿叶百货',npc_list=npcmap.shop_npc_list_for_green_town,prize_box_list=prize.prize_box_for_green_town_shop),
    'MAP02' : hospital.Hospital(name="绿叶医疗中心",npc_list=npcmap.hospital_npc_list_for_green_town),
    'MAP03' : petgym.PetGym(name='绿叶道馆',npc_list=npcmap.petgym_npc_list_for_green_town,prize_box_list=None),
    'MAP04' : wildform.WildForm(name='绯红大道',
                                wild_pet_list=wildpetlist.wild_pet_list_in_grass_no_1,
                                #block='绿叶徽章',
                                map_id = 'MAP04',
                                 ),
    'MAP05': wildform.WildForm(name='大漩涡',
                               wild_pet_list=wildpetlist.wild_pet_list_in_maelstrom_no_1,
                               treasure_box_list=treasure.treasure_box_for_maelstrom_no_1,
                               npc_list=npcmap.trainer_in_maelstrom_no_1,
                               block='绿叶徽章',
                               map_id='MAP05'
                                ),
    'MAP06': town.Town(name='激流镇',block='绯红徽章',map_id='MAP06'),
    'MAP07': town.Town(name='绿叶镇',map_id='MAP07'),
    'MAP08': wildform.WildForm(name='绿叶大道',
                                wild_pet_list=wildpetlist.wild_pet_list_in_grass_no_1,
                                treasure_box_list=treasure.treasure_box_for_maelstrom_no_1,
                                weather='W001',
                                npc_list = npcmap.trainer_in_grass_no_1,
                               map_id='MAP08'),
}