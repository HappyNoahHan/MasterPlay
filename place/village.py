from place import  placebase,hospital,town,grassfrom,wildpetlist,treasure
class Village(placebase.Place):

    maplist = {
        '1': hospital.Hospital(name="格林医疗中心"),
        '2': town.Town(name='格林镇'),
        '3': grassfrom.Grassform(name='1号草丛',
                                 wild_pet_list=wildpetlist.wild_pet_list_in_grass_no_1,
                                 treasure_box_list=treasure.treasure_box_for_grass_no_1),
    }

