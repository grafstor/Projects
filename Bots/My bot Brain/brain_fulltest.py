# Bot Brain Test

'''
    author: graf stor
    date: 21.12.19
'''

__version__ = "2.0" 

from brain import Bot
import time

Asgard = Bot()

def test1():
    print(Asgard.filemanager("allfiles D:\\projects\\bots\\norm"))
    print('------------------------------------------')
    print(Asgard.home_work())
    print('------------------------------------------')
    print(Asgard.home_work_second())
    print('------------------------------------------')
    print(Asgard.marks('all'))
    print('------------------------------------------')
    print(Asgard.last_marks())
    print('------------------------------------------')
    print(Asgard.translate("hello",'en-ru'))
    print('------------------------------------------')
    print(Asgard.gen_key())
    print('------------------------------------------')
    print(Asgard.wiki("Google",1))
    print('------------------------------------------')
    print(Asgard.google("itpedia"))
    print('------------------------------------------')
    print(Asgard.youtube("https://www.youtube.com/channel/UCk73U4QT3cNDvqb_PaWM8AA"))
    print('------------------------------------------')
    print(Asgard.gdz("алгебра 123"))
    print('------------------------------------------')
    print(Asgard.synon("болшой"))
    print('------------------------------------------')

def test2():
    timing = []
    naming = []

    ttime = time.time()
    Asgard.filemanager("newfile lol.txt")
    timing.append(time.time() - ttime)
    naming.append("filemanager")
    print('filemanager  {} секунд'.format(str(time.time() - ttime)))

    ttime = time.time()
    Asgard.home_work()
    timing.append(time.time() - ttime)
    naming.append("home_work")
    print('home_work  {} секунд'.format(str(time.time() - ttime)))

    ttime = time.time()
    Asgard.home_work_second()
    timing.append(time.time() - ttime)
    naming.append("home_work_second")
    print('home_work_second  {} секунд'.format(str(time.time() - ttime)))

    ttime = time.time()
    Asgard.marks('алгебра геометрия')
    timing.append(time.time() - ttime)
    naming.append("marks")
    print('marks  {} секунд'.format(str(time.time() - ttime)))

    ttime = time.time()
    Asgard.last_marks()
    timing.append(time.time() - ttime)
    naming.append("last_marks")
    print('last_marks  {} секунд'.format(str(time.time() - ttime)))

    ttime = time.time()
    Asgard.translate("hello",'en-ru')
    timing.append(time.time() - ttime)
    naming.append("translate")
    print('translate  {} секунд'.format(str(time.time() - ttime)))

    ttime = time.time()
    Asgard.gen_key()
    timing.append(time.time() - ttime)
    naming.append("gen_key")
    print('gen_key  {} секунд'.format(str(time.time() - ttime)))

    ttime = time.time()
    Asgard.wiki("Google",1)
    timing.append(time.time() - ttime)
    naming.append("wiki")
    print('wiki  {} секунд'.format(str(time.time() - ttime)))

    ttime = time.time()
    Asgard.google("itpedia")
    timing.append(time.time() - ttime)
    naming.append("google")
    print('google  {} секунд'.format(str(time.time() - ttime)))

    ttime = time.time()
    Asgard.youtube("https://www.youtube.com/channel/UC6bTF68IAV1okfRfwXIP1Cg")
    timing.append(time.time() - ttime)
    naming.append("youtube")
    print('youtube  {} секунд'.format(str(time.time() - ttime)))

    ttime = time.time()
    Asgard.gdz("алгебра 123")
    timing.append(time.time() - ttime)
    naming.append("gdz")
    print('gdz  {} секунд'.format(str(time.time() - ttime)))

    N = len(timing)
    for by in range(1, N):
        for k in range(0,N - by):
            if timing[k] > timing[k+1]:
                timing[k], timing[k+1] = timing[k+1], timing[k]
                naming[k], naming[k+1] = naming[k+1], naming[k]

    print("-------------------------------------")

    timing = timing[::-1]
    naming = naming[::-1]
    for i in range(len(timing)):
        if timing[i] != 0.0:
            print('{} {} секунд'.format(naming[i],timing[i]))
if __name__ == "__main__":
    test1()
    test2()