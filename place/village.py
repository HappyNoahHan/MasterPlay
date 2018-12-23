from place import  placebase,hospital,town,grassfrom,wildpetlist
class Village(placebase.Place):

    maplist = {
        '1': hospital.Hospital(name="格林医疗中心"),
        '2': town.Town(name='格林镇'),
        '3': grassfrom.Grassform(name='1号草丛',wild_pet_list=wildpetlist.wild_pet_list_for_grass_no1),
    }

