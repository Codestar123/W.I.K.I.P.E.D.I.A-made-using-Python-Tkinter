from tkinter import *
from tkinter import scrolledtext
import wikipedia as wiki
from functools import partial
class Main:
    def __init__(self):
        self.tk = Tk()
        self.tk.title('W.I.K.I.P.E.D.I.A')
        self.tk.resizable(0,0)
        self.tk.wm_attributes('-topmost',1)
        self.tk.geometry('400x600')
        
        self.question = StringVar()
        self.textentry = Entry(self.tk,textvariable = self.question)
        self.textentry.place(x = 0,y = 20,width = 300)

        self.search = Button(self.tk,text = 'Search',command = self.searcher,fg = 'white',bg = 'green')
        self.search.place(x = 300,y = 20,width = 100,height = 20)
        self.tk.bind('<KeyPress-Return>',self.searcher)
        
        self.display_info = scrolledtext.ScrolledText(self.tk,font = ('Times',15))
        self.display_info.place(x = 0,y = 50,height = 550,width = 400)
                        
    def searcher(self,evt = None):
        question = self.question.get()
        if question:
            try:
                info = wiki.summary(question)
                self.display_info.delete(0.0,END)
                self.display_info.insert(0.0,info)
                
            except:
                self.question.set('Something went wrong')
        
    
        
        
        
        
m = Main()
m.tk.mainloop()
        
