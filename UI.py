
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

first_click=True
second_click=False

board=logic.chess_plane()
player=1#默认玩家红方
first_x=-1
first_y=-1

def encoder(x1,y1,x2,y2):
    en_num=['0','1','2','3','4','5','6','7','8','9']
    en_alp=['a','b','c','d','e','f','g','h','i']
    return en_alp[x1]+en_num[y1]+en_alp[x2]+en_num[y2]

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
    global first_click
    global first_y
    global first_x
    global board
    global player
    print("clicked at",event.x,event.y)
    x=round((event.x-83)/79)
    y=round((event.y-753)/(-1*78.33))
    print("clicked at",y,x)
    if first_click:
        print("first click")
        if player==1:
            if board.board1_2d[y][x]==1:
                first_click=False
                first_x=x
                first_y=y
        if player==0:
            if board.board0_2d[y][x]==1:
                first_click=False
                first_x=x
                first_y=y
    else:
        print("second click",first_y,first_x)
        if player==1:
            options=board.valid_moves_1()
            if encoder(first_x,first_y,x,y) in options:
                if board.board0_2d[y][x]==1:#出现吃子的情况
                    for t in range(7,14):
                        if board.board[t][y][x]==1:
                            board.board[t][y][x]=0
                            break
                    board.board0_2d[y][x]=0
                for t in range(7):
                    if board.board[t][first_y][first_x]==1:
                        board.board[t][first_y][first_x]=0
                        board.board[t][y][x]=1
                        break
                board.board_2d[first_y][first_x]=0
                board.board1_2d[first_y][first_x]=0#原位置清0
                    
                board.board_2d[y][x]=1#不写也可以
                board.board1_2d[y][x]=1
                player=0#测试用！！
            first_click=True#重置
        if player==0:
            options=board.valid_moves_0()
            if encoder(first_x,first_y,x,y) in options:
                first_click=True#重置
                if board.board1_2d[y][x]==1:#出现吃子的情况
                    for t in range(7):
                        if board.board[t][y][x]==1:
                            board.board[t][y][x]=0
                            break
                    board.board1_2d[y][x]=0
                for t in range(7,14):
                    if board.board[t][first_y][first_x]==1:
                        board.board[t][first_y][first_x]=0
                        board.board[t][y][x]=1
                        break
                board.board_2d[first_y][first_x]=0
                board.board0_2d[first_y][first_x]=0#原位置清0
                    
                board.board_2d[y][x]=1#不写也可以
                board.board0_2d[y][x]=1
                player=1#测试用！！
        first_click=True#重置
        
        print(player)    

    drawbroad()
    loadchess()
                
                                   
    
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