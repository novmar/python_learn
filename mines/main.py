#!/bin/env python3
def preparecanvas(x,y,mines):
    """

    :param x: size of array 10-100
    :param y: size of array  10-100
    :param mines: number of mines in array 10 - 100
    :return: canvas
    canvas:
    0 0 0 0 0 0 0 0 0 0
    0 X 1 0 0 0 0 0 0 0
    0 1 1 0 0 1 1 1 0 0
    0 0 1 1 1 1 X 1 0 0
    0 0 1 X 1 1 2 2 1 0
    0 0 1 X 1 0 1 X 1 0
    0 0 1 X 1 0 1 1 1 0
    0 0 1 1 1 1 1 1 0 0
    0 0 0 0 0 1 X 1 0 0
    0 1 2 3 2 2 1 1 0 0
    0 1 X X X 1 0 0 0 0
    0 0 0 0 0 0 0 0 0 0

    """
    canvas=array{}
    prex=0
    #generate mines
    minemap=[]
    for mine in range(mines):
        addmine=random(x*y)

    for (:x+2):
        canvas[]