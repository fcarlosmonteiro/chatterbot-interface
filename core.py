# encoding=utf8
import os
import sys
import pyttsx3
import pyglet
import time
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from gtts import gTTS


class Chatbot():
	#verbose logging
	#import logging
	#logging.basicConfig(level=logging.INFO)

	#reload(sys)
	#sys.setdefaultencoding('utf8')

	def trainning(self, path):
		mr_robot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter",logic_adapters=['chatterbot.logic.BestMatch'])#,read_only=True)
		trainer = ChatterBotCorpusTrainer(mr_robot)
		trainer.train(path)
		return mr_robot
		#trainer.train("./data/portuguese/")

	def eliot(self, mr_robot):
		print("\nEliot: Olá eu sou um robô educacional.")
		
		while True:
			
			resq = input('\nVocê: ')
			#inicio = time.time()
			resp = mr_robot.get_response(resq)
			
			#tts = gTTS(str(resp), lang='pt-br')
			#tts.save("fala.mp3")
			#os.system("mpg321 fala.mp3")
			 
			print('\nEliot: ' + str(resp))
			if resq == 'vazar':
				return
			#fim = time.time()
			#print(fim - inicio)	

	#path="./data/portuguese/"
	#mr_robot=trainning(path)
	#eliot(mr_robot)