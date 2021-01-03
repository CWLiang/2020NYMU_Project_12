import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import sys
scale = 1
W, H = 800, 400
gui = tk.Tk()
gui.title('2020 NYMU Final Project No.12')
gui.geometry(f'{W*scale}x{H*scale}')
gui.configure(background='black')
gui.resizable(0, 0)

frame1 = tk.Frame(master = gui,
                width = W*scale,
                height = H*scale,
                bg='white')
frame1.pack(fill='both', expand=True)

textSize = 20
fontStyle = tkFont.Font(family="Noto Sans Mono CJK TC", size=textSize, weight='bold')

frame2 = tk.Frame(frame1)
frame2.pack(side='top', pady=(100,0))
row = 0
frameName = tk.Frame(frame2)
frameName.grid(row=row, column=0, sticky=tk.W)
labelName = tk.Label(frameName, text="使用者姓名：", font=fontStyle)
labelName.pack(side='left')
textName = tk.Text(frameName, width=10, height=1, bg='#F2F2F2', font=fontStyle)
textName.pack(side='left')

row += 1
frameH = tk.Frame(frame2)
frameH.grid(row=row, column=0, sticky=tk.W)
labelH = tk.Label(frameH, text="身高：", font=fontStyle)
labelH.pack(side='left')
textH = tk.Text(frameH, width=10, height=1, bg='#F2F2F2', font=fontStyle)
textH.pack(side='left')

row += 1
frameW = tk.Frame(frame2)
frameW.grid(row=row, column=0, sticky=tk.W)
labelW = tk.Label(frameW, text="體重：", font=fontStyle)
labelW.pack(side='left')
textW = tk.Text(frameW, width=10, height=1, bg='#F2F2F2', font=fontStyle)
textW.pack(side='left')

row += 1
frameS = tk.Frame(frame2)
frameS.grid(row=row, column=0, sticky=tk.W)
labelS = tk.Label(frameS, text="生理性別：", font=fontStyle)
labelS.pack(side='left')
combS = ttk.Combobox(frameS, width=5, values=['男性','女性'], font=fontStyle)
combS.pack(side='left')

row += 1
ages = list(range(1,100))
frameA = tk.Frame(frame2)
frameA.grid(row=row, column=0, sticky=tk.W)
labelA = tk.Label(frameA, text="年齡：", font=fontStyle)
labelA.pack(side='left')
combA = ttk.Combobox(frameA, width=5, values=ages, font=fontStyle)
combA.pack(side='left')

row += 1
exercise = ['久坐(辦公室工作、沒有運動習慣)',
            '輕度(運動1-2天/週)',
            '中度(運動3-5天/週)',
            '高度(運動6-7天/週)',
            '極高度(運動員等級，每天運動2次)']
frameE = tk.Frame(frame2)
frameE.grid(row=row, column=0, sticky=tk.W)
labelE = tk.Label(frameE, text="運動習慣：", font=fontStyle)
labelE.pack(side='left')
combE = ttk.Combobox(frameE, values=exercise, font=fontStyle)
combE.pack(side='left')

buttonNext = tk.Button(frameE, text="下一步", bg='#2E75B6', fg='white', font=fontStyle)
buttonNext.pack(side='right', padx=20)

gui.mainloop()
