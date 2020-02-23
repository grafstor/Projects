# Bot Brain

'''
    author: graf stor
    date: 21.12.19
'''

__version__ = "2.0" 

from os import startfile, listdir, remove, rename
from urllib.parse import unquote
from bs4 import BeautifulSoup
from random import randint
import wikipedia
import requests
import datetime
import time

class Bot:
    ''' Graf bot '''
    def __init__(self):
        '''builder'''
        self.yandexKey = "trnsl.1.1.20191029T172108Z.4b8a3759a478f522.8c9da464e32acd3a22edb0a277ce0c15d352450d" #API key
        self.yandexUrl = "https://translate.yandex.net/api/v1.5/tr.json/translate"  #API adress

    def filemanager(self,code):
        '''file manager'''
        ncode = code.split()

        if len(ncode) < 2:
            return "неправильный формат"

        name = ncode[1]

        #-----------------------------------------------------
        if ncode[0] == "newfile":
            f = open(name, 'tw', encoding='utf-8')
            f.close()
            return "файл создан"
        #-----------------------------------------------------
        elif ncode[0] == "writefile":
            code = " ".join(ncode[2:])
            try:
                f = open(name, 'a')
                f.write('\n{}'.format(code))
                f.close()
                return "файл записан"
            except:
                return "нет такого файла"
        #-----------------------------------------------------
        elif ncode[0] == "readfile":
            try:
                f = open(name, 'r', encoding='utf-8')
                f = f.read()
                return 'читаю файл\n{}'.format(f)
            except:
                return "нет такого файла"
        #-----------------------------------------------------
        elif ncode[0] == 'removefile':
            try:
                return "удаляю файл"
                remove(name)
            except:
                return "нет такого файла"
        #-----------------------------------------------------
        elif ncode[0] == 'renamefile':
            name2 = 'files\\' + ncode[2]
            try:
                return "переименовываю файл"
                rename(name, name2)
            except:
                return "нет такого файла"
        #-----------------------------------------------------
        elif ncode[0] == 'allfiles':
            files = listdir(" ".join(ncode[1:]))
            if len(files) != 0:
                allfiles = ''
                for i in files:
                    allfiles+=i+"\n"
                return allfiles
            else:
                return "нет файлов"
        else:
            return "нет такой команды"

    def home_work(self):
        '''dnevni.ru parser'''
        session = requests.Session()

        url = 'https://login.dnevnik.ru/login/esia/nnov'
        
        data = {
            'login':        'silkingeorgii',
            'password':    '301134grafstor',
        }

        main_text = session.post(url, data=data).text

        session.close()

        r1 = main_text.find('"items":[{"subject":')
        main_text = main_text[r1:-1]

        r2 = main_text.find('}]')
        main_text = main_text[0:r2]
            
        sub = []
        work = []
        
        for i in range(1,main_text.count('subject')+1):
            sub.append(self.lrb(main_text,"subject","homeworkText",i,i,10,-3))
            work.append(self.lrb(main_text,"homeworkText","lessonUrl",i,i,15,-3))

        if len(sub) == 0:
            return "Нет заданий на завтра"

        else:
            alltext = ''
            for i in range(len(sub)):
                if work[i] == '':work[i] = 'нет задания'
                alltext+="{} -- {}\n".format(sub[i],work[i])

            return alltext

    def home_work_second(self):
        '''evrika.vyksa parser'''
        now = datetime.datetime.now()
        day = now.day
        month = str(now.month)

        timee = time.time()

        search = "http://xn----7sbbfc7aod2cq2iqa.xn--p1ai/home_kakoninaov"
        resp = requests.get(search)
        soup = BeautifulSoup(resp.text, 'lxml')

        a = soup.find_all('span')
        a = [str(i) for i in a]
        alltext = ''

        for i in range(len(a)):
            lb1 = a[i].find("ание за")
            if lb1 != -1:
                linT = i

            b1 = a[i].find("OGE")
            if b1 != -1:
                titlee = self.lrb(a[linT],">","<",1,2,1)
                texxt = self.lrb(a[i+1],">","<",1,2,1)
                for i in range(6):
                    ddate = str(day - i) + "." + month + "."
                    if titlee.find(ddate) != -1:
                        alltext+=titlee+"\n"+texxt+"\n\n"

        return alltext

    def marks(self,text='all'):
        '''dnevni.ru parser'''
        session = requests.Session()

        url = 'https://login.dnevnik.ru/login/esia/nnov'
        url2 = 'https://schools.dnevnik.ru/marks.aspx?school=7168&index=2&tab=period&homebasededucation=False'
        
        data = {
            'login':        'silkingeorgii',
            'password':    '301134grafstor',
        }
        data2 = {
            'DNT':'1',
            'Host': 'schools.dnevnik.ru',
            'Referer': 'https://schools.dnevnik.ru/marks.aspx?school=7168&tab=week',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
        }

        session.post(url, data=data)
        # page_main = session.post(url2, headers=data2).text

        ff2 = session.post(url2, headers=data2).text

        session.close()

        text = text.split()
        strret = ''
        sublist = []
        marklist = []

        lbg = ff2[ff2.find('<th style ="width:20%" rowspan="2">Предметы</th>') + 48:]

        for i in range(1,ff2.count('<strong class="u">')+1):
            lsb = self.find_nth(ff2,'<strong class="u">',i)
            subjectstr = ff2[lsb+18:]
            rsb = subjectstr.find('</strong>')

            sublist.append(subjectstr[:rsb].lower())

            subjectstr2 = subjectstr[:subjectstr.find('<td>0</td>')]
            allmarks = ''
            ball = []
            for i in range(1,subjectstr2.count('<span class="mark')+1):
                lmb = self.find_nth(subjectstr2,'data-num="0"',i)
                markk = subjectstr2[lmb+13:lmb+14]
                if markk.isdigit():ball.append(int(markk))
                allmarks+='\t{}'.format(markk)
            if len(ball)>0:
                allmarks+='\t средний балл: {}'.format(str(sum(ball)/len(ball))[:4])
            if allmarks == '':
                allmarks = "нет оценок"

            marklist.append(allmarks.lower())

        if text[0] == "all":
            for i in range(len(sublist)):
                strret+='{}\n{}\n\n'.format(sublist[i],marklist[i])
            return strret

        for i in text:
            f = -1
            try:
                f = sublist.index(i)
            except:
                for j in range(len(sublist)):
                    t = sublist[j].find(i)
                    if t != -1:
                        strret+='{}\n{}\n'.format(sublist[j],marklist[j])
                        break
                else:
                    strret+='нет предмета {}\n'.format(i)
            if f != -1:
                strret+='{}\n{}\n'.format(sublist[f],marklist[f])

        return strret

    def last_marks(self,num=5):
        '''dnevni.ru parser'''
        session = requests.Session()

        url = 'https://login.dnevnik.ru/login/esia/nnov'
        
        data = {
            'login':        'silkingeorgii',
            'password':    '301134grafstor',
        }

        main_text = session.post(url, data=data).text

        session.close()

        strret = ''

        for i in range(1,num+1):
            lbp = self.find_nth(main_text,'"marks":[{"value":"',i)
            rbp = self.find_nth(main_text,'"subject":{"name":"',i)
            rrbp = self.find_nth(main_text,'"lesson":{"date":"',i)
            rrrbp = self.find_nth(main_text,'"work":{"name":"',i)

            ewe1 = main_text[lbp+19:lbp+23]
            mark = ewe1[:ewe1.find('",')]

            ewe2 = main_text[rbp+19:rbp+30]
            subj = ewe2[:ewe2.find('",')]

            ewe3 = main_text[rrrbp+16:rrrbp+40]
            impor = ewe3[:ewe3.find('",')].replace("период", "четверть")

            datee = ".".join(main_text[rrbp+18:rrbp+28][5:].split("-")[::-1])

            strret+="{} {}\tза\t{}\t{}\n".format(mark,subj,datee,impor)

        return strret

    def translate(self,text,lang):
        '''yandex translator'''
        params = {"key": self.yandexKey,"text": text,"lang":lang}
        response = requests.get(self.yandexUrl ,params=params)
        tr_text = str(''.join(response.json()["text"]))
        return tr_text

    def gen_key(self,num=16):
        '''return random key'''
        alf = list("abcdefghijklmnopqrstuvwxyz")
        key = ''

        for i in range(num):
            ran1 = randint(0, 25)
            ran2 = randint(1,10)
            ran3 = randint(0,2)
            if ran3 == 1:
                key += alf[ran1]
            elif ran3 == 2:
                key += alf[ran1].upper()
            else:
                key += str(ran2)
        return key

    def wiki(self,body,pred=5):
        '''return information from wikipedia'''
        body = self.translate(body,"ru-en")

        try:
            wcontent = wikipedia.page(body).content
            wcontent = wcontent.split('.')[:pred]
            for i in range(len(wcontent)):
                wcontent[i] = self.translate(wcontent[i]+'.',"en-ru")
            strret = ' '.join(wcontent)
            return strret

        except wikipedia.exceptions.DisambiguationError as e:
            strret = 'Выберите из списка:\n{}'.format(str(e))
            return strret

    def google(self,req,number=5):
        '''google search'''
        search = req

        resp = requests.get("https://www.google.com/search?q={}".format(search))
        soup = BeautifulSoup(resp.text, 'lxml')

        a = soup.find_all('a')
        a = [str(i) for i in a]

        chak = 0
        allurl = []
        t_last = ''

        for i in range(len(a)):
            if a[i].find("url?q=") != -1:
                t =  self.lrb(a[i],"url?q=","&amp",1,1,6)
                m = self.lrb(a[i],">","<",2,3,1)

                t = unquote(t)

                if t != t_last:
                    allurl.append((m,t))

                t_last = t
                chak+=1

            if chak == number:
                break

        return allurl

    def youtube(self,urlu):
        '''return last 5 video from youtube chanal'''
        resp = requests.get(urlu)

        soup = BeautifulSoup(resp.text, 'lxml')

        a = soup.find_all('a')
        a = [unquote(str(i)) for i in a]

        chak = 0
        allurl = ''
        lastT = ''

        for i in range(len(a)):
            if a[i].find('href="/watch?v=') != -1:
                taag = self.lrb(a[i+1],'v=','',1,1,2,13,1)
                if lastT == taag:
                    titlee = self.lrb(a[i+1],">","<",1,2,1)
                    allurl+='{}\n \thttps://www.youtube.com/watch?v={}\n'.format(titlee,taag)
                    chak+=1
                lastT = taag
            if chak == 5:
                break

        return allurl

    def find_nth(self, haystack, needle, n):
        '''return n element'''
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start+len(needle))
            n -= 1
        return start

    def lrb(self,string,lb,rb,lbn=1,rbn=1,lbp=0,rbp=0,men=False):
        '''special parser function'''
        lb = self.find_nth(string, lb, lbn)
        if men:
            return string[lb + lbp:lb + rbp]
        rb = self.find_nth(string, rb, rbn)
        return string[lb + lbp:rb + rbp]

    def synon(self,word):
        resp = requests.get("https://text.ru/synonym/{}".format(word))
        soup = BeautifulSoup(resp.text, 'lxml')

        a = soup.find_all('a')
        a = [unquote(str(i)) for i in a]

        chak = 0
        allwords = ""
        non_fir = False

        for i in range(len(a)):
            if a[i].find('href="/synonym') != -1:
                if non_fir:
                    taag = self.lrb(a[i],'>','<',1,2,1)
                    allwords+="{}\n".format(taag)
                    print(taag)
                    chak+=1
                non_fir = True

            if chak == 20:
                break
        if allwords == "":
            return "нет синонимов"
        return allwords


    def gdz(self,text):
        '''bild gdz request'''
        workpiece = "гдз 9 класс по "
        ntext = text.split()
        for i in ntext:
            if i.find("англ") != -1:
                request = "{} {} Кузовлев {}".format(workpiece, ntext[0], " ".join(ntext[1:]))
            elif i.find("алге") != -1:
                request = "{} {} Колягин {}".format(workpiece, ntext[0], " ".join(ntext[1:]))
            elif i.find("русс") != -1:
                request = "{} {} Троснецова {}".format(workpiece, ntext[0], " ".join(ntext[1:]))
            elif i.find("геом") != -1:
                request = "{} {} Атанасян {}".format(workpiece, ntext[0], " ".join(ntext[1:]))
            elif i.find("геог") != -1:
                request = "{} {} Алексеев {}".format(workpiece, ntext[0], " ".join(ntext[1:]))
            elif i.find("инф") != -1:
                request = "{} {} Босова {}".format(workpiece, ntext[0], " ".join(ntext[1:]))
            elif i.find("физ") != -1:
                request = "{} {} Пёрышкин {}".format(workpiece, ntext[0], " ".join(ntext[1:]))
        return request
