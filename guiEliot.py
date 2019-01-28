from tkinter import filedialog
from tkinter import *
import subprocess
import core
import os

class Janela():
    def __init__(self, toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        
        self.msg = Label(self.fr1, text="Selecione um arquivo para treinamento e teste")
        self.msg.pack()
        
        self.output_button = Button(self.fr1, text="Selecionar", command=self.openFile)
        self.output_button.pack(side="top")
        
        #self.botao2 = Button(self.fr1, text="Treinar", command=self.executeBot)
        #self.botao2.pack(side="top")

        #termf = Frame(self.fr1, height=200, width=600)
        #termf.pack(side="bottom",expand="YES")
        #wid = termf.winfo_id()
        #os.system('xterm -into %d -geometry 160x50 -sb &' % wid)


    def openFile(self):
        raiz.filename =  filedialog.askopenfilename()
        f = raiz.filename
        self.executeBot(f)

    def executeBot(self,path):
        e = core.Chatbot()
        mr_robot = e.trainning(path)
        #e.eliot(mr_robot)
        subprocess.call(['xterm', '-e', 'python3 ./bot_treinado.py'])
        exit(0)

raiz = Tk()        
Janela(raiz)
raiz.title("Trainning Interface - Eliot")
raiz.mainloop()