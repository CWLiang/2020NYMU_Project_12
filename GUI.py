import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import *
import sys
from os import listdir
from os.path import isdir
from PIL import ImageTk, Image
import argparse

scale = 1
W, H = 800, 600


class Data:
    def __init__(self, database):
        self.name = None
        self.height = None
        self.weight = None
        self.gender = None
        self.age = None
        self.exercise = None
        
        print(database)
        d = list(listdir(database))
        print(d)
        sys.exit()
        for d in listdir(database):
            for f in listdir(f'{database}/{d}'):
                print(f)
        sys.exit()
        self.items = list()
        for idx, f in enumerate(files):
            item = Item(self.scrollable_frame, f, idx)
            item.pack(side=TOP, fill=X, expand=True)
            self.items.append(item)

        self.breakfast = None
        self.lunch = None

class Item(tk.Frame):
    def __init__(self, master, name, idx):
        tk.Frame.__init__(self, master)
        self.configure(bg='white')
        textSize = 18
        fontStyle = tkFont.Font(family="Noto Sans Mono CJK TC", size=textSize, weight='bold')
 
        self.labelName = tk.Label(self, text=name, font=fontStyle, bg='white')
        self.labelName.pack(side='left')
        amount = list(range(100))
        self.comb = ttk.Combobox(self, width=5, values=amount, font=fontStyle)
        self.comb.current(0)
        self.comb.pack(side='right')

class Menu(tk.Frame):
    def __init__(self, master, cat):
        tk.Frame.__init__(self, master)
        
        canvas = tk.Canvas(self, bg='blue')
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg='red')
        self.scrollable_frame.pack(side=LEFT, fill=X, expand=True)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor=NW)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        files = listdir(f'{database}/{cat}')
        self.items = list()
        for idx, f in enumerate(files):
            item = Item(self.scrollable_frame, f, idx)
            item.pack(side=TOP, fill=X, expand=True)
            self.items.append(item)
        
        textSize = 18
        fontStyle = tkFont.Font(family="Noto Sans Mono CJK TC", size=textSize, weight='bold')

        buttonUpdate = tk.Button(canvas, text="確認", bg='#2E75B6', fg='white', font=fontStyle, command=lambda: self.update())
        buttonUpdate.pack(side=RIGHT, anchor=SE, padx=(0,20), pady=(0,20))

    def update(self):
        for item in self.items:
            print(item.labelName.cget('text'), item.comb.get())

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = None
        self.title('2020 NYMU Final Project No.12')
        self.geometry(f'{W}x{H}')
        self.configure(background='white')
        self.resizable(0, 0)
        self.switch_frame(StartPage)
        
    
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack(fill=BOTH,expand=True)

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.configure(bg='black')

        textSize = 18
        fontStyle = tkFont.Font(family="Noto Sans Mono CJK TC", size=textSize, weight='bold')
        
        frame = tk.Frame(self, bg='orange')
        frame.pack(fill=BOTH, expand=True, padx=120, pady=100)

        frameName = tk.Frame(frame, bg='white')
        frameName.pack(side=TOP, anchor=NW)
        labelName = tk.Label(frameName, text="使用者姓名：", font=fontStyle, bg='white')
        labelName.pack(side='left')
        textName = tk.Text(frameName, width=10, height=1, bg='#F2F2F2', font=fontStyle)
        textName.pack(side='left')

        frameH = tk.Frame(frame, bg='white')
        frameH.pack(side=TOP, anchor=NW)
        labelH = tk.Label(frameH, text="身高：", font=fontStyle, bg='white')
        labelH.pack(side='left')
        textH = tk.Text(frameH, width=10, height=1, bg='#F2F2F2', font=fontStyle)
        textH.pack(side='left')

        frameW = tk.Frame(frame, bg='white')
        frameW.pack(side=TOP, anchor=NW)
        labelW = tk.Label(frameW, text="體重：", font=fontStyle, bg='white')
        labelW.pack(side='left')
        textW = tk.Text(frameW, width=10, height=1, bg='#F2F2F2', font=fontStyle)
        textW.pack(side='left')

        frameS = tk.Frame(frame, bg='white')
        frameS.pack(side=TOP, anchor=NW)
        labelS = tk.Label(frameS, text="生理性別：", font=fontStyle, bg='white')
        labelS.pack(side='left')
        combS = ttk.Combobox(frameS, width=5, values=['男性','女性'], font=fontStyle)
        combS.pack(side='left')

        ages = list(range(1,100))
        frameA = tk.Frame(frame, bg='white')
        frameA.pack(side=TOP, anchor=NW)
        labelA = tk.Label(frameA, text="年齡：", font=fontStyle, bg='white')
        labelA.pack(side='left')
        combA = ttk.Combobox(frameA, width=5, values=ages, font=fontStyle)
        combA.pack(side='left')

        exercise = ['久坐(辦公室工作、沒有運動習慣)',
                    '輕度(運動1-2天/週)',
                    '中度(運動3-5天/週)',
                    '高度(運動6-7天/週)',
                    '極高度(運動員等級，每天運動2次)']
        frameE = tk.Frame(frame, bg='white')
        frameE.pack(side=TOP, anchor=NW)
        labelE = tk.Label(frameE, text="運動習慣：", font=fontStyle, bg='white')
        labelE.pack(side='left')
        combE = ttk.Combobox(frameE, values=exercise, font=fontStyle)
        combE.pack(side='left')

        
        buttonNext = tk.Button(frame, text="下一步", bg='#2E75B6', fg='white', font=fontStyle, command=lambda: master.switch_frame(PageOne))
        buttonNext.pack(side=TOP, anchor=SE)
        
class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.menu = None
        self.buttonNext = None
        self.configure(bg='green')
        
        textSize = 18
        fontStyle = tkFont.Font(family="Noto Sans Mono CJK TC", size=textSize, weight='bold')

        frameBtn = tk.Frame(self, bg='white')
        frameBtn.pack(side=TOP)
        labelBtn = tk.Label(frameBtn, text="今日早餐：", font=fontStyle, bg='white')
        labelBtn.pack(side='left')

        buttonTmp = tk.Button(frameBtn, text='奶類', bg='#D9D9D9', fg='black', font=fontStyle, command=lambda: self.switch_frame(Menu, '奶類'))
        buttonTmp.pack(side='right',padx=3)
        buttonTmp = tk.Button(frameBtn, text='穀飲', bg='#D9D9D9', fg='black', font=fontStyle, command=lambda: self.switch_frame(Menu, '穀飲'))
        buttonTmp.pack(side='right',padx=3)
        buttonTmp = tk.Button(frameBtn, text='飯類', bg='#D9D9D9', fg='black', font=fontStyle, command=lambda: self.switch_frame(Menu, '飯類'))
        buttonTmp.pack(side='right',padx=3)
        buttonTmp = tk.Button(frameBtn, text='麵包', bg='#D9D9D9', fg='black', font=fontStyle, command=lambda: self.switch_frame(Menu, '麵包'))
        buttonTmp.pack(side='right',padx=3)
        buttonTmp = tk.Button(frameBtn, text='麵類', bg='#D9D9D9', fg='black', font=fontStyle, command=lambda: self.switch_frame(Menu, '麵類'))
        buttonTmp.pack(side='right',padx=3)
        buttonTmp = tk.Button(frameBtn, text='點心', bg='#D9D9D9', fg='black', font=fontStyle, command=lambda: self.switch_frame(Menu, '點心'))
        buttonTmp.pack(side='right',padx=3)

    def switch_frame(self, frame_class, cat):
        new_frame = frame_class(self, cat)
        if self.menu is not None:
            self.menu.destroy()
        self.menu = new_frame
        self.menu.pack(side=TOP, fill=BOTH, expand=True, padx=50, pady=30)
        textSize = 18
        fontStyle = tkFont.Font(family="Noto Sans Mono CJK TC", size=textSize, weight='bold')
        if self.buttonNext is not None:
            self.buttonNext.destroy()
        self.buttonNext = tk.Button(self, text="下一步", bg='#2E75B6', fg='white', font=fontStyle)
        self.buttonNext.pack(side=TOP, anchor=SE, padx=(0,30), pady=(0,30))


if __name__ == '__main__':
    database = 'data'
    data = Data(database)
    gui = GUI()
    gui.mainloop()
