from bs4 import BeautifulSoup
from urllib.request import  urlopen
from database import petdata

class DownLoader(object):
    def __init__(self):
        self.server = 'http://www.pokemon.name'
        self.target = 'http://www.pokemon.name/w/index.php?title=%E4%B8%BB%E9%A2%98:%E5%AE%9D%E5%8F%AF%E6%A2%A6/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8&printable=yes'
        self.names = []
        self.urls = []
        self.nums = 0

    def getPetMessage(self):
        '''
        获取下载地址
        :return:
        '''
        bs_obj = BeautifulSoup(urlopen(self.target),features="html.parser")
        obj = bs_obj.find_all('li',{'class':None,'id':None})

        list=[]
        for pet_title in obj:
            pet_no = pet_title.get_text().split('.')[0].strip()
            pet_name = pet_title.get_text().split('.')[1].strip()
            pet_url = pet_title.contents[3].get('href')
            list.append((pet_no,pet_name,self.server+pet_url))

        return list


if __name__ == "__main__":
    dl = DownLoader()
    pet_message_list = dl.getPetMessage()

    for msg in pet_message_list[0:3]:
        petdata.insert_data(msg)
