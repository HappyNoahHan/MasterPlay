from place import placebase,village
import time

class Hospital(placebase.Place):

    def restore(self,player):
        for key,pet in player.pet_list.items():
            #清楚状态
            pet.health = pet._max_health
            pet.debuff_dict.clear()
            pet.buff_dict.clear()
            pet.property_buff.clear()
            pet.status.clear()
            pet.alive = True

            for key,skill in pet.skill_list.items():
                skill.pp_value = skill._pp_value_max

    def showMap(self,player):
        print("欢迎来到 %s " % self.name)
        print("1 恢复")
        print("2 返回")

        select_id = input("请输入指令")
        if select_id == '1':
            self.restore(player)
            time.sleep(3)
            print("所有精灵状态恢复")
            return self.showMap(player)
        elif select_id == '2':
            player.current_place.showMap(player)
        else:
            print("指令错误！")
            return self.showMap(player)



