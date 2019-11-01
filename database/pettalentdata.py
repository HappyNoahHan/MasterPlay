from bs4 import BeautifulSoup
from urllib.request import urlopen

from  database import petdata
import time

class PetTalentMsg(object):
    def get_msg(self,target):
        msg = []
        bs_obj = BeautifulSoup(urlopen(target),features="html.parser")
        obj = bs_obj.body.find_all('tr')
        for sub_obj in obj[1:]:
            msg.append(sub_obj.get_text().strip('\n').split())

        return msg

if __name__ == '__main__':

    talent = PetTalentMsg()
    target ='http://www.pokemon.name/wiki/%E7%89%B9%E6%80%A7/%E6%8C%89%E4%B8%96%E4%BB%A3%E5%88%86%E7%B1%BB'

    whole_msgs = talent.get_msg(target)

    dup_msgs =[]
    for msg in whole_msgs:
        if '日文' not in msg:
            if len(msg) == 5:
                msg[2] = msg[2] + ' ' + msg[3]
                msg.pop(3)
            elif len(msg) == 6:
                msg[2] = msg[2] + ' ' + msg[3] + ' ' + msg[4]
                msg.pop(4)
                msg.pop(3)
            dup_msgs.append(msg)

    petdata.insert_talent_info(dup_msgs)


