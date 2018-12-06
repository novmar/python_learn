#!/bin/env python3
from pprint import pprint
import random

class mines:


    def __init__(self,x,y,mines):
        self.mines = mines
        self.minesPlaced=0
        self.resize_field(x,y)

    def resize_field(self,x,y):
        self.x = x
        self.y = y
        self.create_field()

    def create_field(self):
        self.field=[]
        self.minesPlaced=0
        for ix in range(self.x):
           line=[]
           for iy in range(self.y):
                line.append("0")
           self.field.append(line)


    def place_mines(self):
        if self.mines > self.x*self.y:
            self.mines=(self.x*self.y)
        if self.minesPlaced < self.mines:
            rx=random.randint(0,self.x-1)
            ry=random.randint(0,self.y-1)
            if self.field[rx][ry] == "0":
                self.field[rx][ry] = "X"
                self.minesPlaced+=1
            self.place_mines()

    def calculate_field(self,x,y):
        if self.field[x][y] !="X":
            mines=0
            for sx in range(x-1,x+2):
                for sy in range(y-1,y+2):
                    print(sx,":",sy,end='')
                    if (-1<sx<self.x) and (-1<sy<self.y):
                        print(" test ",end='')

                        if self.field[sx][sy]=="X" :
                            mines+=1
                            print("mine",end="")
                    print()

            return (str(mines))
        else:
            return ("X")

    def random_test(self,times):
        for _ in range(times):
            tryx=random.randint(1,self.x)-1
            tryy=random.randint(1,self.y)-1
            print("testing: ",tryx,",",tryy,"as: ",self.calculate_field(tryx,tryy))
    def fill_field(self):
        for fx in range(self.x):
            for fy in range(self.y):
                self.field[fx][fy]=self.calculate_field(fx,fy)









hra=mines(10,15,50);

hra.place_mines()
hra.fill_field()
pprint(hra.field)
pprint(hra.calculate_field(0,0))
pprint(hra.field)

