# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def get_row(row, lenn, begin=1):
    '''
    得到横排的值并返回列表
    row 第几排，lenn 获取多少个数据，begin 从第几列开始
    '''
    listt = []
    for i in range(begin, begin+lenn):
        listt += [Cell(row, i).value]
    return listt



def get_col(col, lenn, begin=1):
    '''
    将横排改为列，功能同上
    '''
    listt = []
    for i in range(begin, begin+lenn):
        listt += [Cell(i, col).value]
    return listt
    
    
    
def value_row(row, l, begin=1):
    '''
    给横排赋值：row 第几排，l 要赋值的列表，begin 从第几列开始
    '''
    lenn = len(l)
    for i in range(lenn):
        Cell(row, begin+i).value = l[i]
        
        

def value_col(col, l, begin=1):
    '''
    将横排改为列，功能同上
    '''
    lenn = len(l)
    for i in range(lenn):
        Cell(begin+i, col).value = l[i]
        
def get_matrix(x_len, y_len, x_begin=1, y_begin=1):
    '''
    获取一个矩阵的值，返回二维列表
    （矩阵的长，矩阵的高，矩阵起始横坐标，矩阵起始纵坐标）
    '''
    listt = []    
    for i in range(y_begin, y_begin + y_len):
        listt += [get_row(i, x_len, x_begin)]
    return listt
    
    
def value_matrix(listt, x=1, y=1):
    '''
    将二维列表的值写入Excel的一块矩阵中
    （二维列表，矩阵起始横坐标，矩阵起始纵坐标）
    '''
    for l in listt:
        value_row(y,l,x)
        y += 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
