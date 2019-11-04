from bs4 import BeautifulSoup
from urllib.request import urlopen

from database import petdata
import time

class AllSkillData(object):
    def get_message(self,target):
        msg=[]
        bs_obj = BeautifulSoup(urlopen('http://www.pokemon.name'+target),features='html.parser')
        body = bs_obj.body
        obj = body.find_all('tr')
        for sub_obj in obj[1:]:
            skill_info = '|'.join(sub_obj.get_text().strip('\n').split())
            if '招式|属性|' not in skill_info:
                if skill_info.split('|').__len__() == 7:
                    skill_info += '|NULL'

                msg.append(skill_info)
        return msg


if __name__ == '__main__':
    sql = 'select * from skillURL'
    datas = petdata.get_data(sql)
    skill_list = AllSkillData()
    for data in datas:
        print("正在获取 %s 属性招式信息" % data[0])
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        message = skill_list.get_message(data[1])
        print("正在存储 %s 属性招式信息" % data[0])
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        petdata.insert_all_skill_data(message)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
