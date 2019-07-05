from place import hospital,wildform,shop,petgym,village,town
from assist import prize

top_map_dict={
    'MAP00' : village.Village(name='新手村',map_id='MAP00'),
    'MAP01' : shop.Shop(name='绿叶百货',map_id='MAP01'),
    'MAP02' : hospital.Hospital(name="绿叶医疗中心",map_id='MAP02'),
    'MAP03' : petgym.PetGym(name='绿叶道馆',map_id='MAP03'),
    'MAP04' : wildform.WildForm(name='绯红大道',
                                block='绿叶徽章',
                                map_id = 'MAP04',
                                 ),
    'MAP05': wildform.WildForm(name='大漩涡',
                               #block='绿叶徽章',
                               map_id='MAP05',
                               can_fish=True,
                                ),
    'MAP06': town.Town(name='激流镇',block='绯红徽章',map_id='MAP06'),
    'MAP07': town.Town(name='绿叶镇',map_id='MAP07'),
    'MAP08': wildform.WildForm(name='绿叶大道',
                                weather='W001',
                               map_id='MAP08'),
}