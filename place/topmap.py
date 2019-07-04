from place import hospital,wildform,wildpetlist,treasure,shop,petgym,village,town
from players import  npcmap
from assist import prize

top_map_dict={
    'MAP00' : village.Village(name='新手村',map_id='MAP00'),
    'MAP01' : shop.Shop(name='绿叶百货',prize_box_list=prize.prize_box_for_green_town_shop,map_id='MAP01'),
    'MAP02' : hospital.Hospital(name="绿叶医疗中心",map_id='MAP02'),
    'MAP03' : petgym.PetGym(name='绿叶道馆',map_id='MAP03'),
    'MAP04' : wildform.WildForm(name='绯红大道',
                                block='绿叶徽章',
                                map_id = 'MAP04',
                                 ),
    'MAP05': wildform.WildForm(name='大漩涡',
                               treasure_box_list=treasure.treasure_box_for_maelstrom_no_1,
                               block='绿叶徽章',
                               map_id='MAP05'
                                ),
    'MAP06': town.Town(name='激流镇',block='绯红徽章',map_id='MAP06'),
    'MAP07': town.Town(name='绿叶镇',map_id='MAP07'),
    'MAP08': wildform.WildForm(name='绿叶大道',
                                treasure_box_list=treasure.treasure_box_for_maelstrom_no_1,
                                weather='W001',
                               map_id='MAP08'),
}