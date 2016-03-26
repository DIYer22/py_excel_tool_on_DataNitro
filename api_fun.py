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
        
#        
#l = get_row(1,6)
#
#print l
#
#raw_input()
#value_col(9,l)
#raw_input()
        

l = get_col(2,43) 
'''获取第二列的43个单元格的值 放入 l 里面'''


def get_qq(mail):
    '''
    传入一个邮箱地址 分析是否是 qq号+qq邮箱的格式 是则返回qq号，否则返回 空
    '''
    if 'qq.com' in mail:
        qq = mail.split('@')[0]
        try:
            qq = int(qq)
            return qq
        except:
            pass
    return None


l = map(get_qq,l)
'''
对l里面的每个元素执行 get_qq() 函数
'''

value_col(3,l)
        
'''
把l里面的数据写在第3列
'''   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
