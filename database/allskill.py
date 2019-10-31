from bs4 import BeautifulSoup
from urllib.request import  urlopen

from database import petdata

class AllSkillMsg():

    def __init__(self):
        self.detail_msg_list = []

    def getUrlMessage(self, target):
        msg = {}
        bs_obj = BeautifulSoup(urlopen(target), features="html.parser")
        body = bs_obj.body
        obj = body.find_all('a')
        for subobj in obj:
            if subobj.get('title'):
                if "属性的招式" in subobj.get('title'):
                    attr = subobj.get('title').strip('属性的招式')
                    url = subobj.get('href')
                    msg[attr] = url

        return msg


if __name__ == '__main__':
    skill_list = AllSkillMsg()
    target = 'http://www.pokemon.name/wiki/%E4%B8%BB%E9%A2%98:%E6%8B%9B%E5%BC%8F'
    msg = skill_list.getUrlMessage(target)
    petdata.insert_skill_url(msg)

