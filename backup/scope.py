import requests,sys
from bs4 import BeautifulSoup

class DownLoader(object):
    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'https://www.biqukan.com/1_1408/'
        self.names = []
        self.urls = []
        self.nums = 0

    def getDownLoadUrl(self):
        '''
        获取下载地址
        :return:
        '''
        req = requests.get(url=self.target)
        html = req.text
        bf = BeautifulSoup(html,"html.parser")
        div = bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]),"html.parser")
        a = a_bf.find_all('a')
        self.nums = len(a[13:])
        for each in a[13:]:
            self.names.append(each.string)
            self.urls.append(self.server+each.get('href'))


    def getContents(self,url):

        req = requests.get(url=url)
        bf = BeautifulSoup(req.text,'html.parser')
        textA = bf.find_all('div',class_='showtxt')
        texts = textA[0].text.replace(' ','\n\n')
        return texts

    def writer(self,name,path,text):
        write_flag = True
        with open(path,'a',encoding='utf-8') as f:
            f.write(name+'\n')
            f.writelines(text)
            f.write('\n\n')



if __name__ == "__main__":
    dl = DownLoader()
    dl.getDownLoadUrl()
    #print(dl.getContents(dl.urls[0]))
    #print('《一年永恒》开始下载：')
    dl.writer(dl.names[0], '飞剑问道.txt', dl.getContents(dl.urls[0]))
    #sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums) + '\r')
    #sys.stdout.flush()
    #print('《一年永恒》下载完成')