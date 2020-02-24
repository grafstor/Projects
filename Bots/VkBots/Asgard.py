# Asgars Bot 
# bot close

'''
    author: graf stor
    date: 15.12.19
'''

__version__ = "3.0" 

# Version 3.0  20/12/19
#     File system 
#     Dnevnik.ru marks

# Version 2.0  15/12/19
#     New Google search
#     YouTube vidos
#     Home work from dnevnik.ru
#     Home work from evrika vyksa
#     New body scaner
#     Gdz request builder

from os import startfile, listdir, remove, rename
from urllib.parse import unquote
from bs4 import BeautifulSoup
from random import randint
import wikipedia
import requests
import datetime
import vk_api
import time

class Bot:
    ''' Vk Bot '''
    def __init__(self):
        '''bot builder'''
        self.vkApi = "xxxxxxxxxxxxxxxxxxxxx"

        self.vk = vk_api.VkApi(token=self.vkApi)
        self.vk._auth_token()

        self.scena = "команды"
        self.repeat = ''

        self.yandexKey = "trnsl.1.1.20191029T172108Z.4b8a3759a478f522.8c9da464e32acd3a22edb0a277ce0c15d352450d" #API key
        self.yandexUrl = "https://translate.yandex.net/api/v1.5/tr.json/translate"  #API adress


        self.manager = True

        self.mainpassword = self.__get_key()
        self.vk.method("messages.send", {"peer_id": 463988739, "message": str(self.mainpassword), "random_id": randint(1, 2147483647)})

    def start(self):
        '''turn bot on'''
        print("Bot working!")
        self.__mainprocess()

    def stop(self):
        '''turn bot off'''
        self.manager = False
        self.__send_message("пока")
        print("Bot stop working!")

    def __mainprocess(self):
        '''main bot process'''
        timeout = 0
        while self.manager:
            try:
                messages = self.vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
                if messages["count"] >= 1:
                    timeout = 0
                    self.id = messages["items"][0]["last_message"]["from_id"]
                    self.body = messages["items"][0]["last_message"]["text"]
                    #-----------------------------------------------------
                    if self.body == self.mainpassword:
                        self.__send_message("пока")
                        print("Bot stop working!")
                        break
                    #-----------------------------------------------------
                    self.scena, self.body = self.__scena_scan(self.body)
                    #-----------------------------------------------------
                    if self.scena == "переводчик":
                        if self.body[:2] == "tj":
                            tr_text = self.__translate(self.body[2:],"ru-ja")
                            if tr_text == self.body[2:]:
                                tr_text = self.__translate(self.body[2:],"ja-ru")
                                self.__send_message(tr_text)
                                continue
                            else:
                                self.__send_message(tr_text)
                                continue
                        tr_text = self.__translate(self.body,"ru-en")
                        if tr_text == self.body:
                            tr_text = self.__translate(self.body,"en-ru")
                            self.__send_message(tr_text)
                        else:
                            self.__send_message(tr_text)
                    #-----------------------------------------------------
                    elif self.scena == "википедия":
                        self.__wiki(self.body,self.repeat)
                        self.repeat = self.body
                    #-----------------------------------------------------
                    elif self.scena == "гугл":
                        self.__search(self.body)
                    #-----------------------------------------------------
                    elif self.scena == "дневник":
                        if self.body.lower() == "дз":
                            self.__home_work()
                        elif self.body.lower() == "дз 2":
                            self.__home_work_second()
                        elif self.body[:6].lower() == "оценки":
                            self.__home_work(1,self.body[7:].lower().split())
                    #-----------------------------------------------------
                    elif self.scena == "гдз":
                        self.__gdz(self.body)
                    #-----------------------------------------------------
                    elif self.scena == "выключение":
                        if self.id == 463988739:
                            self.stop()
                            break
                    #-----------------------------------------------------
                    elif self.scena == "файлы":
                        if self.id == 463988739:
                            self.__filemanager(self.body)
                time.sleep(2)
                    #-----------------------------------------------------
            except Exception as E:
                time.sleep(2)

    def __filemanager(self,code):
        ncode = code.split()
        for i in ncode:
            if -1 != i.find("\\"):
                name = ncode[1]
                break
            else:
                name = 'files\\' + ncode[1]
                break
        #-----------------------------------------------------
        if name == "runfile":
            try:
                self.__send_message("запускаю файл")
                startfile(name)
            except:
                self.__send_message("нет такого файла")
        #-----------------------------------------------------
        elif name == "newfile":
            zagat1 = 'from vk_api import VkApi\nfrom random import randint\nvkApi = "xxxxxxxxxxxxxxxxxxxxx"\nvk = VkApi(token=vkApi)\nvk._auth_token()\n'
            zagat2 = 'def prin(a):\n\tvk.method("messages.send", {"peer_id": 463988739, "message": str(a), "random_id": randint(1, 2147483647)})\n'

            f = open(name, 'tw', encoding='utf-8')
            f.write('{}{}'.format(zagat1,zagat2))
            f.close()

            self.__send_message("файл создан")
        #-----------------------------------------------------
        elif name == "writefile":
            code = " ".join(ncode[2:])
            try:
                f = open(name, 'a')
                f.write('\n{}'.format(code))
                f.close()
                self.__send_message("файл записан")
            except:
                self.__send_message("нет такого файла")
        #-----------------------------------------------------
        elif name == "readfile":
            try:
                self.__send_message("читаю файл")
                f = open(name, 'r', encoding='utf-8')
                f = f.read()
                self.__send_message(f)
            except:
                self.__send_message("нет такого файла")
        #-----------------------------------------------------
        elif name == 'removefile':
            try:
                self.__send_message("удаляю файл")
                remove(name)
            except:
                self.__send_message("нет такого файла")
        #-----------------------------------------------------
        elif name == 'renamefile':
            name2 = 'files\\' + ncode[2]
            try:
                self.__send_message("переименовываю файл")
                rename(name, name2)
            except:
                self.__send_message("нет такого файла")
        #-----------------------------------------------------
        elif name == 'allfiles':
            files = listdir("files")
            if len(files) != 0:
                allfiles = ''
                for i in files:
                    allfiles+=i+"\n"
                self.__send_message(allfiles)
            else:
                self.__send_message("нет файлов")

    def __home_work(self,textik=0,subjj=[]):
        ''' dnevni.ru parser'''
        session = requests.Session()
        url = 'https://login.dnevnik.ru/login/esia/nnov'
        
        data = {
            'login':        'your',
            'password':    'your',
        }

        page_main = session.post(url, data=data)

        if len(subjj) > 0:
            url2 = 'https://schools.dnevnik.ru/marks.aspx?school=7168&index=2&tab=period&homebasededucation=False'
            data2 = {
                'DNT':'1',
                'Host': 'schools.dnevnik.ru',
                'Referer': 'https://schools.dnevnik.ru/marks.aspx?school=7168&tab=week',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
            }
            page_main2 = session.post(url2, headers=data2)
            ff2 = page_main2.text
            session.close()

            lbg = ff2[ff2.find('<th style ="width:20%" rowspan="2">Предметы</th>') + 48:]
            sublist = []
            marklist = []
            for i in range(1,ff2.count('<strong class="u">')+1):
                lsb = self.__find_nth(ff2,'<strong class="u">',i)
                subjectstr = ff2[lsb+18:]

                rsb = subjectstr.find('</strong>')
                sublist.append(subjectstr[:rsb].lower())

                subjectstr2 = subjectstr[:subjectstr.find('<td>0</td>')]
                allmarks = ''
                ball = []

                for i in range(1,subjectstr2.count('<span class="mark')+1):
                    lmb = self.__find_nth(subjectstr2,'data-num="0"',i)
                    markk = subjectstr2[lmb+13:lmb+14]

                    if markk.isdigit():ball.append(int(markk))

                    allmarks+='\t{}'.format(markk)
                if len(ball)>0:
                    allmarks+='\t средний балл: {}'.format(sum(ball) / len(ball))
                if allmarks == '':
                    allmarks = "нет оценок"

                marklist.append(allmarks.lower())
            if subjj[0] == "all":
                allll = ''
                for i in range(len(sublist)):
                    allll+='{}\n\t{}\n\n'.format(sublist[i],marklist[i])
                self.__send_message(allll)
                return

            for i in subjj:
                f = -1
                try:
                    f = sublist.index(i)
                except:
                    for j in range(len(sublist)):
                        t = sublist[j].find(i)
                        if t != -1:
                            self.__send_message('{}\n\t{}'.format(sublist[j],marklist[j]))
                            break
                    else:
                        self.__send_message('нет предмета {}'.format(i))
                if f != -1:
                    self.__send_message('{}\n\t{}'.format(sublist[f],marklist[f]))
            return

        
        now = datetime.datetime.now()
        day = str(now.day)
        main_text = page_main.text

        allmarks = ""

        if textik:
            session.close()
            for i in range(1,6):
                lbp = self.__find_nth(main_text,'"marks":[{"value":"',i)
                rbp = self.__find_nth(main_text,'"subject":{"name":"',i)
                rrbp = self.__find_nth(main_text,'"lesson":{"date":"',i)
                rrrbp = self.__find_nth(main_text,'"work":{"name":"',i)

                ewe1 = main_text[lbp+19:lbp+23]
                mark = ewe1[:ewe1.find('",')]

                ewe2 = main_text[rbp+19:rbp+30]
                subj = ewe2[:ewe2.find('",')]

                ewe3 = main_text[rrrbp+16:rrrbp+40]
                impor = ewe3[:ewe3.find('",')].replace("период", "четверть")

                datee = ".".join(main_text[rrbp+18:rrbp+28][5:].split("-")[::-1])

                allmarks+="{} {}\tза\t{}\t{}\n".format(mark,subj,datee,impor)
            self.__send_message(allmarks)
            return
        session.close()
        r1 = main_text.find('"items":[{"subject":')
        main_text = main_text[r1:-1]

        r2 = main_text.find('}]')
        main_text = main_text[0:r2]
            
        iii = 1
        sub = []
        work = []
        
        for i in range(main_text.count('subject')):
            sub.append(self.__lrb(main_text,"subject","homeworkText",iii,iii,10,-3))
            work.append(self.__lrb(main_text,"homeworkText","lessonUrl",iii,iii,15,-3))
        
            iii+=1
        if len(sub) == 0:
            self.__send_message("Нет заданий на завтра")
        else:
            alltext = ''
            for i in range(len(sub)):
                if work[i] == '':work[i] = 'нет задания'
                alltext+="{} -- {}\n".format(sub[i],work[i])
            self.__send_message(alltext)

    def __home_work_second(self):
        ''' evrika.vyksa parser '''
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
                titlee = self.__lrb(a[linT],">","<",1,2,1)
                texxt = self.__lrb(a[i+1],">","<",1,2,1)
                for i in range(6):
                    ddate = str(day - i) + "." + month + "."
                    if titlee.find(ddate) != -1:
                        alltext+=titlee+"\n"+texxt+"\n\n"
        self.__send_message(alltext)

    def __translate(self,text,lang):
        ''' yandex translator '''
        params = {"key": self.yandexKey,"text": text,"lang":lang}
        response = requests.get(self.yandexUrl ,params=params)
        tr_text = str(''.join(response.json()["text"]))
        return tr_text

    def __send_message(self,message):
        ''' vk message sender '''
        self.vk.method("messages.send", {"peer_id": self.id, "message": message, "random_id": randint(1, 2147483647)})

    def __get_key(self):
        ''' return random key '''
        alf = list("abcdefghijklmnopqrstuvwxyz")
        self.key = ''
        for i in range(16):
            ran1 = randint(0, 25)
            ran2 = randint(1,10)
            ran3 = randint(0,2)
            if ran3 == 1:
                self.key += alf[ran1]
            elif ran3 == 2:
                self.key += alf[ran1].upper()
            else:
                self.key += str(ran2)
        return self.key

    def __wiki(self,body,repeat=0):
        ''' return information from wikipedia '''
        if body == repeat:
            return
        body_2 = body.split("__")
        body = body_2[0]
        if len(body_2)>1:
            pred1 = int(body_2[1])
        else:
            pred1 = 4
        body = self.__translate(body,"ru-en")
        try:
            wcontent = wikipedia.page(body).content
            wcontent = wcontent.split('.')[:pred1]
            for i in range(len(wcontent)):
                wcontent[i] = self.__translate(wcontent[i]+'.',"en-ru")
            self.__send_message(' '.join(wcontent))
        except wikipedia.exceptions.DisambiguationError as e:
            self.__send_message('Выберите из списка:')
            self.__send_message(str(e))

    def __search(self,request,number=5):
        ''' google search '''
        search = request

        resp = requests.get("https://www.google.com/search?q={}".format(search))
        soup = BeautifulSoup(resp.text, 'lxml')

        a = soup.find_all('a')
        a = [str(i) for i in a]
        chak = 0
        self.__send_message('Ща раскажу {}'.format(request))
        allurl = ''
        prop = 0
        for i in range(len(a)):
            if a[i].find("url?q=") != -1:
                t =  self.__lrb(a[i],"url?q=","&amp",1,1,6)
                t = unquote(t)
                m = self.__lrb(a[i],">","<",2,3,1)
                allurl+= m + '\n' + t + '\n'

                if t.find("wikipedia") != -1 and m != '' and m != "Википедия":
                    m = m[:m.find("— Википедия")]
                    self.__wiki(m)
                    return

                elif t.find("www.youtube.com/channel") != -1:
                    self.__youtube(t)
                    return

                else:
                    chak+=1
            if chak == number:
                break
        self.__send_message(allurl)

    def __youtube(self,urlu):
        ''' return last 5 video from youtube chanal '''
        resp = requests.get(urlu)

        soup = BeautifulSoup(resp.text, 'lxml')

        a = soup.find_all('a')
        a = [unquote(str(i)) for i in a]
        chak = 0
        allurl = ''
        lastT = ''
        for i in range(len(a)):
            if a[i].find('href="/watch?v=') != -1:
                taag = self.__lrb(a[i+1],'v=','',1,1,2,13,1)
                if lastT == taag:
                    titlee = self.__lrb(a[i+1],">","<",1,2,1)
                    allurl+='{}:\n https://www.youtube.com/watch?v={}\n'.format(titlee,taag)
                    chak+=1
                lastT = taag
            if chak == 5:
                break
        self.__send_message(allurl)

    def __find_nth(self, haystack, needle, n):
        ''' return n element '''
        start = haystack.find(needle)
        while start >= 0 and n > 1:
            start = haystack.find(needle, start+len(needle))
            n -= 1
        return start

    def __lrb(self,string,lb,rb,lbn=1,rbn=1,lbp=0,rbp=0,men=False):
        lb = self.__find_nth(string, lb, lbn)
        if men:
            return string[lb + lbp:lb + rbp]
        rb = self.__find_nth(string, rb, rbn)
        return string[lb + lbp:rb + rbp]

    def __gdz(self,text):
        ''' bild gdz request '''
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
        self.__search(request,2)

    def __scena_scan(self,body):
        ''' scan body '''
        nbody = body.split()
        nbody = [i.lower() for i in nbody]
        filecom = ["newfile","runfile","readfile","allfiles", "removefile","renamefile", "writefile"]
        for i in nbody:
            if i == "t" or i == "переведи":
                return ("переводчик", " ".join(nbody[1:]))

            elif i == "tj":
                return ("переводчик", " ".join(nbody))

            elif i == "w":
                return ("википедия", " ".join(nbody[1:]))

            elif i == "g":
                return ("гугл", " ".join(nbody[1:]))

            elif i == "z" or i == "гдз":
                return ("гдз", " ".join(nbody[1:]))

            elif i == "дз" or i == "оценки":
                return ("дневник", " ".join(nbody))

            elif i == "выключись":
                return ("выключение", " ".join(nbody))

            for j in filecom:
                if i == j:
                    return ("файлы", " ".join(nbody))

            else:
                return ("гугл", " ".join(nbody))

if __name__ == "__main__":
    Asgard = Bot()
    Asgard.start()
