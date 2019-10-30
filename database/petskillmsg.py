from bs4 import BeautifulSoup
from urllib.request import urlopen
from database import petdata


class PetSkillMsg():

    def __init__(self):
        self.detail_msg_list = []

    def getDeatilMessage(self, target):
        bs_obj = BeautifulSoup(urlopen(target), features="html.parser")
        body = bs_obj.body
        try:
            obj = body.find_all('table',{'style':'table-layout:fixed;'})
        except:
            return 0

        return obj


    def getMsg(self,messages,no):
        message=[]
        for msg in messages[1:]:
            detail_msg = '|'.join(msg.get_text().strip('\n').split())
            if detail_msg.split('|').__len__() == 8:
                message.append(str(no)+'|' + detail_msg)
            else:
                message.append(str(no) + '|' + detail_msg+'|-')

        return message


if __name__ == '__main__':
    for no in range(25,152):
        datas = []
        print("正在获取%d pet的技能列表" % no)
        if len(str(no)) == 1:
            no = '00'+str(no)
        elif len(str(no)) == 2:
            no = '0'+str(no)
        else:
            no = str(no)
        target = 'http://www.pokemon.name/wiki/%E6%95%B0%E6%8D%AE:Pokemon/Learnset7/' + no

        pet = PetSkillMsg()
        full_msg = pet.getDeatilMessage(target)
        for sub_msg in full_msg:
            skill_msg = sub_msg.find_all('tr')
            skill_message = pet.getMsg(skill_msg, no)
            datas.append(skill_message)
            #print(skill_message)
        print("正在存储%s pet的升级技能列表" % no)
        petdata.insert_skill_data(datas)





