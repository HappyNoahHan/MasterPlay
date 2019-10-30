
from bs4 import BeautifulSoup
from urllib.request import  urlopen
from database import petdata

class PetDetailMsg():
    def __init__(self):
        self.detail_msg_list = []

    def getDeatilMessage(self,target):
        bs_obj = BeautifulSoup(urlopen(target), features="html.parser")
        body = bs_obj.body
        try:
            obj = body.find('tr', {'class': 'pp-tab-content'})
        except:
            return 0

        subobj = obj.find_all('td')

        for msg in subobj[1:]:
            '''去除\xa0'''
            detail_msg = "".join(msg.get_text().strip('\n').split())
            msg_len = len(detail_msg)
            if msg_len > 0:
                self.detail_msg_list.append(detail_msg)

        return self.detail_msg_list

if __name__ == '__main__':
    #pet = PetDetailMsg()
    for i in range(113,152):
        pet = PetDetailMsg()
        pet_no = petdata.get_pet('petMsg',i)
        print("正在获取%d %s 的资料~~~~" % (pet_no[0],pet_no[1]))
        pet_detail_msg = pet.getDeatilMessage(target=pet_no[2])

        #如果返回值为0 跳出这次循环
        if pet_detail_msg == 0:
            print("无法获取资料,请检查源头!")
            continue


        data_list=[pet_no[0],pet_no[1],
                   pet_detail_msg[2],
                   pet_detail_msg[4],
                   pet_detail_msg[6],
                   pet_detail_msg[8],
                   pet_detail_msg[10],
                   pet_detail_msg[12],
                   pet_detail_msg[15],
                   pet_detail_msg[17],
                   pet_detail_msg[19],
                   pet_detail_msg[21],
                   pet_detail_msg[23],
                   pet_detail_msg[25],
                   pet_detail_msg[27],
                   pet_detail_msg[30],
                   pet_detail_msg[51],
                   pet_detail_msg[53],
                   pet_detail_msg[55],
                   pet_detail_msg[57],
                   pet_detail_msg[59],
                   pet_detail_msg[61],
                   pet_detail_msg[63]]
        petdata.insertDetailData(data_list)