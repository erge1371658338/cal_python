# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 20:23:04 2021

@author: 86182
"""

class Doll():    #娃娃类，父类
    def __init__ (self,size,price):
        self.price = price
        self.size  = size       
    def imformation (self):
        print("这是一个玩偶")
class Maomaorou(Doll):      #毛毛肉类，子类
    def __init__ (self,size,price): 
        super().__init__(size,price)  #注意这里没有冒号
    def mao (self,cute):
        self.cute=cute
    def imformation (self):     
        print("毛毛肉"+self.cute)