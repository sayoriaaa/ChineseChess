# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 20:27:29 2021

@author: sayori
"""
import tkinter
import time
import tkinter.messagebox as tkmbox
from PIL import Image,ImageTk
import logic

root=tkinter.Tk()
cv=tkinter.Canvas(root,bg='white',width=1920,height=1000)

root.title("中国象棋——sayoriaaa")
root.geometry("1920x1080")

imgs=[tkinter.PhotoImage(file='assets\\'+str(i)+'.png')for i in range(14)]

image = Image.open('assets\\bk.png')
bk= ImageTk.PhotoImage(image)

board=logic.chess_plane()

def drawbroad():
    p1=cv.create_image((0,0),image=bk)
    cv.coords(p1,(400,400)) #图像文件是中心点的坐标
    
def loadchess():
    current_board=board.board 
    
    for t in range(14):
        for i in range(10):
            for j in range(9):
                if current_board[t][i][j]==1:
                    schess=imgs[t]
                    cv.create_image((79*j+83),(-78.33*i+753),image=schess)
    
    

def callback(event):
    print("clicked at",event.x,event.y)
    x=round((event.x-83)/79)
    y=round((event.y-753)/(-1*78.33))
    print("clicked at",y,x)

            
            
                
                
            
            
    
    
#------------------------------------------------------------------------------   
drawbroad()
loadchess()
#------------------------------------------------------------------------------

#button1=tkinter.Button(root,fg='red',bg='black',text='red first')
#button1.pack(side=tkinter.RIGHT)

cv.bind('<Button-1>',callback)
cv.pack()



root.mainloop()


print("hello")
time.sleep(1)

root.destroy()