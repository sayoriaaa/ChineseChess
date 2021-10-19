# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 18:59:00 2021

@author: sayori
"""

import numpy as np

class node(object):
    def __init__(self,prior_p,parent,board):
        self.P=prior_p
        self.Q=0#行动价值
        self.N=0#访问次数
        self.v=0#当前胜率
        self.U=0#Q=1/N*sum(v(next)) 由公式导出
        self.W=0#
        self.parent=parent
        self.child={}
        self.board=board
        
    def q_u(self,c):
        return self.Q+c*self.P*np.sqrt(self.parent.N)/1+self.N
    def select(self,c):
        return max(self.child.items(),key=lambda node:node[1].q_u(c))
    def expand(self,moves,action_prob):#action_probs由神经网络产生
        tol_v=1e-8
        for action in moves:
            mov_v=action_prob[lab2i[action]]#由神经网络返回的棋面下的不同走子的胜率，还没写
            tol_v+=mov_v
            new_node=node(mov_v,self,self.board)#这里的棋面应该是执行完之后的棋面，回头别忘记改！！！
            self.child[action]=new_node
        for _,node in self.child:
            node.P/=tol_v#对子节点的先验概率作归一化
    def backup(self,value,c):
        while self!=None:
            self.N += 1
            self.W += value
            self.v = value
            self.Q = self.W / self.N  # node.Q += 1.0*(value - node.Q) / node.N
            self.U = c* self.P * np.sqrt(self.parent.N) / ( 1 + self.N)

            
        
        