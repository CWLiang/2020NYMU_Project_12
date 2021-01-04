import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import sys

scale = 1
W, H = 800, 400

class Data:
    def __init__(self):
        self.name = None
        self.height = None
        self.weight = None
        self.gender = None
        self.age = None
        self.exerceise = None

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.title('2020 NYMU Final Project No.12')
        self.geometry(f'{W*scale}x{H*scale}')
        self.configure(background='white')
        self.resizable(0, 0)
        self.switch_frame(StartPage)
        
    
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.configure(width = W*scale,
                        height = H*scale,
                        bg='white')
        self.pack(fill='both', expand=True)

        textSize = 18
        fontStyle = tkFont.Font(family="Noto Sans Mono CJK TC", size=textSize, weight='bold')

        frame2 = tk.Frame(self, bg='white')
        frame2.pack(side='top', padx=(60,0),pady=(40,0))
        row = 0
        frameName = tk.Frame(frame2, bg='white')
        frameName.grid(row=row, column=0, sticky=tk.W, ipady=10)
        labelName = tk.Label(frameName, text="使用者姓名：", font=fontStyle, bg='white')
        labelName.pack(side='left')
        textName = tk.Text(frameName, width=10, height=1, bg='#F2F2F2', font=fontStyle)
        textName.pack(side='left')

        row += 1
        frameH = tk.Frame(frame2, bg='white')
        frameH.grid(row=row, column=0, sticky=tk.W, ipady=10)
        labelH = tk.Label(frameH, text="身高：", font=fontStyle, bg='white')
        labelH.pack(side='left')
        textH = tk.Text(frameH, width=10, height=1, bg='#F2F2F2', font=fontStyle)
        textH.pack(side='left')

        row += 1
        frameW = tk.Frame(frame2, bg='white')
        frameW.grid(row=row, column=0, sticky=tk.W, ipady=10)
        labelW = tk.Label(frameW, text="體重：", font=fontStyle, bg='white')
        labelW.pack(side='left')
        textW = tk.Text(frameW, width=10, height=1, bg='#F2F2F2', font=fontStyle)
        textW.pack(side='left')

        row += 1
        frameS = tk.Frame(frame2, bg='white')
        frameS.grid(row=row, column=0, sticky=tk.W, ipady=10)
        labelS = tk.Label(frameS, text="生理性別：", font=fontStyle, bg='white')
        labelS.pack(side='left')
        combS = ttk.Combobox(frameS, width=5, values=['男性','女性'], font=fontStyle)
        combS.pack(side='left')

        row += 1
        ages = list(range(1,100))
        frameA = tk.Frame(frame2, bg='white')
        frameA.grid(row=row, column=0, sticky=tk.W, ipady=10)
        labelA = tk.Label(frameA, text="年齡：", font=fontStyle, bg='white')
        labelA.pack(side='left')
        combA = ttk.Combobox(frameA, width=5, values=ages, font=fontStyle)
        combA.pack(side='left')

        row += 1
        exercise = ['久坐(辦公室工作、沒有運動習慣)',
                    '輕度(運動1-2天/週)',
                    '中度(運動3-5天/週)',
                    '高度(運動6-7天/週)',
                    '極高度(運動員等級，每天運動2次)']
        frameE = tk.Frame(frame2, bg='white')
        frameE.grid(row=row, column=0, sticky=tk.W, ipady=10)
        labelE = tk.Label(frameE, text="運動習慣：", font=fontStyle, bg='white')
        labelE.pack(side='left')
        combE = ttk.Combobox(frameE, values=exercise, font=fontStyle)
        combE.pack(side='left')

        buttonNext = tk.Button(frameE, text="下一步", bg='#2E75B6', fg='white', font=fontStyle, command=lambda: master.switch_frame(PageOne))
        buttonNext.pack(side='right', padx=20)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.configure(width = W*scale,
                        height = H*scale,
                        bg='blue')
        self.pack(fill='both', expand=True)

        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)

if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()
