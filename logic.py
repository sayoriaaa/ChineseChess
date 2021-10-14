# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:38:05 2021

@author: sayori
"""
import numpy as np
class chess_plane():
    #红方为1，黑方为0
    #board0-6为红方7-13为黑方,车、马、象、士、将、炮、兵
    board=np.zeros(14*10*9).reshape(14,10,9)#(n,y,x)
    board_2d=np.zeros(10*9).reshape(10,9)#y,x
    board1_2d=np.zeros(10*9).reshape(10,9)#y,x
    board0_2d=np.zeros(10*9).reshape(10,9)#y,x
    
    y=['0','1','2','3','4','5','6','7','8','9']
    x=['a','b','c','d','e','f','g','h','i']
    x_trans={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8}
    def __init__(self):
        self.current_player=1
        self.round=1
        for i in range(5):
            self.board[i][0][i]=1
            self.board[i][0][8-i]=1
            self.board[i+7][9][i]=1
            self.board[i+7][9][8-i]=1
            if (i+2)%2==0:
                self.board[6][3][i]=1
                self.board[6][3][8-i]=1
                self.board[13][6][i]=1
                self.board[13][6][8-i]=1
        self.board[5][2][1]=1
        self.board[5][2][7]=1
        self.board[12][7][1]=1
        self.board[12][7][7]=1
        #初始化总棋盘
        for i in range(10):
            for j in range(9):
                for k in range(14):
                    if self.board[k][i][j]==1:
                        self.board_2d[i][j]=1
                        if k<7: self.board1_2d[i][j]=1
                        else: self.board0_2d[i][j]=1
                        break
        #初始化2d棋盘
        
    def valid_moves(self):
        return_arr=[]
        for k in range(7):
            for i in range(10):
                for j in range(9):
                    if self.board[k][i][j]==1: 
                        if k==0:#车的情况
                            y_co1=10
                            y_co2=0
                            x_co1=9
                            x_co2=0

                            for y_axis in range(10):#获得四周最近棋子的坐标
                                if y_axis<i:
                                    if self.board_2d[y_axis][j]==1:
                                        y_co2=y_axis+1
                                if y_axis>i:
                                    if self.board_2d[y_axis][j]==1:
                                        y_co1=y_axis
                                        break
                            for x_axis in range(9):#获得四周最近棋子的坐标
                                if x_axis<j:
                                    if self.board_2d[i][x_axis]==1:

                                        x_co2=x_axis+1
                                if x_axis>j:
                                    if self.board_2d[i][x_axis]==1:
                                        x_co1=x_axis
                                        break
                            if self.board0_2d[y_co2][j]==1: y_co2-=1
                            if y_co1!=10 and self.board0_2d[y_co1][j]==1: y_co1+=1
                            if self.board0_2d[i][x_co2]==1: x_co2-=1
                            if x_co1!=9 and self.board0_2d[i][x_co1]==1: x_co1+=1#防止越界,判断是边界否可吃
                                
                            for t in range(y_co2,i):
                                move=self.x[j]+self.y[i]+self.x[j]+self.y[t]
                                return_arr.append(move)
                            for t in range(i+1,y_co1):#不能把自己也包括了
                                move=self.x[j]+self.y[i]+self.x[j]+self.y[t]
                                return_arr.append(move)

                            for t in range(x_co2,j):
                                move=self.x[j]+self.y[i]+self.x[t]+self.y[i]
                                return_arr.append(move)
                            for t in range(j+1,x_co1):
                                move=self.x[j]+self.y[i]+self.x[t]+self.y[i]
                                return_arr.append(move)
                        if k==5:#炮的情况，相当于车的情况减去边界检测加上越子检测
                            y_co1=10
                            y_co2=0
                            x_co1=9
                            x_co2=0
                            for y_axis in range(10):#获得四周最近棋子的坐标
                                if y_axis<i:
                                    if self.board_2d[y_axis][j]==1:
                                        y_co2=y_axis+1
                                elif y_axis>i:
                                    if self.board_2d[y_axis][j]==1:
                                        y_co1=y_axis
                                        break
                            for x_axis in range(9):#获得四周最近棋子的坐标
                                if x_axis<j:
                                    if self.board_2d[i][x_axis]==1:
                                        x_co2=x_axis+1
                                if x_axis>j:
                                    if self.board_2d[i][x_axis]==1:
                                        x_co1=x_axis
                                        break
                            
                                
                            for t in range(y_co2,i):
                                move=self.x[j]+self.y[i]+self.x[j]+self.y[t]
                                return_arr.append(move)
                            for t in range(i+1,y_co1):#不能把自己也包括了
                                move=self.x[j]+self.y[i]+self.x[j]+self.y[t]
                                return_arr.append(move)

                            for t in range(x_co2,j):
                                move=self.x[j]+self.y[i]+self.x[t]+self.y[i]
                                return_arr.append(move)
                            for t in range(j+1,x_co1):
                                move=self.x[j]+self.y[i]+self.x[t]+self.y[i]
                                return_arr.append(move)
                                
                                
                                
        return return_arr
                            
                               
                                            
                                    
                
                
                
            

    
        
        
        
        
x=chess_plane()
print(x.board)
print("##########")
print(x.board_2d)
print(x.valid_moves())