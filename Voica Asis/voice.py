import speech_recognition as sr
import os
from time import sleep
import sys
import time
import psutil
import win32con
from gtts import gTTS
from random import randint
from bs4 import BeautifulSoup
import requests
import webbrowser
from pygame import mixer
from urllib.parse import unquote

mixer.init(44100, -16, 64, 8192)

def talk(words):
	tts = gTTS(words)

	path = f'sounds/{randint(1,10000)}.mp3'

	tts.save(path)
	mixer.music.load(path)
	mixer.music.play()
# pyautogui

# talk("Привет")
import signal
import pyautogui
import subprocess
proc = None

def recognize():
	zadanie = None

	r = sr.Recognizer()

	with sr.Microphone(chunk_size=4096) as fala:
		print("===@")
		# r.pause_threshold=5
		r.phrase_time_limit=2
		r.operation_timeout=1
		r.instant_energy_threshold=1000

		r.dynamic_energy_threshold=True
		r.dynamic_energy_adjustment_ratio=1.0
		r.adjust_for_ambient_noise(fala)

		# audio = r.listen(fala,timeout=4)
		audio = r.listen(fala)
	print("@++")

	try:
		tt = time.time()
		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		print(time.time() - tt)
		print(zadanie)


	except:
		return

	return zadanie
def find_nth(haystack, needle, n):
		''' return n element '''
		start = haystack.find(needle)
		while start >= 0 and n > 1:
			start = haystack.find(needle, start+len(needle))
			n -= 1
		return start
def lrb(string,lb,rb,lbn=1,rbn=1,lbp=0,rbp=0,men=False):
		lb = find_nth(string, lb, lbn)
		if men:
			return string[lb + lbp:lb + rbp]
		rb = find_nth(string, rb, rbn)
		return string[lb + lbp:rb + rbp]
def youtube(urlu):
	''' return last 5 video from youtube chanal '''
	resp = requests.get(urlu)

	soup = BeautifulSoup(resp.text, 'lxml')

	a = soup.find_all('a')
	a = [unquote(str(i)) for i in a]
	allurl = ''
	lastT = ''
	titlee =''
	for i in range(len(a)):
		if a[i].find('href="/watch?v=') != -1:
			taag = lrb(a[i+1],'v=','',1,1,2,13,1)
			if lastT == taag:
				titlee = lrb(a[i+1],">","<",1,2,1)
				allurl ='https://www.youtube.com/watch?v={}\n'.format(taag)
				break
			lastT = taag

	return (titlee,allurl)
def commands(text):
	global proc
	if "включи" in text:
		# talk("включаю")

		path = "D:\\projects\\graf_player\\Graf_Player\\Graf_Stor_Arch\\main.pyw"
		if text.split()[1] == "что-нибудь":
			proc = subprocess.Popen(f'py {path} 1', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			return

		elif text.split()[1:]:
			arg = " ".join(text.split()[1:])[:-1]
			proc = subprocess.Popen(f'py {path} {arg}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			return

	elif "сверни" in text:
		# talk("свернула")

		pyautogui.keyDown('winleft')
		pyautogui.press('m')
		pyautogui.keyUp('winleft')

	elif "загу" in text:
		# talk("вот что я нашла")
		text = text.split()
		text = " ".join(text[1:])

		webbrowser.open(f"https://www.google.com/search?q={text}")

	elif "покажи" in text:
		text = text.split()
		text = " ".join(text[1:])
		tit, url = youtube(f"https://www.youtube.com/results?search_query={text}")
		# talk(f"смотри {tit}")


		webbrowser.open(url)

	elif "выключись" in text:
		# talk("выкючаю")

		exit()

	elif "выключ" in text:
		# talk("пока")

		os.system(f"TASKKILL /F /PID {proc.pid} /T")

while True:
	text = recognize()
	if text:
		commands(text)
