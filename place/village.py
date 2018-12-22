from place import  placebase,hospital,town,grassfrom
class Village(placebase.Place):

    map = {
        '1': hospital.Hospital(name="格林医疗中心"),
        '2': town.Town(name='格林镇'),
        '3': grassfrom.Grassform(name='1号草丛'),
    }

