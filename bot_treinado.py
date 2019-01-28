# encoding=utf8
import os
import sys
#import pyttsx3
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from gtts import gTTS


mr_robot = ChatBot("Chatterbot",read_only=True)
print("\nEliot: Olá eu sou um robô educacional.")
print("\nEliot: Digite \"vazar\" caso queira sair.")
while True:
	
	resq = input('\nVocê: ')
	#inicio = time.time()
	resp = mr_robot.get_response(resq)
	tts = gTTS(str(resp), lang='pt-br')
	tts.save("fala.mp3")
	os.system("mpg321 fala.mp3")
	 
	print('\nEliot: ' + str(resp))
	if resq == 'vazar':
		exit(0)