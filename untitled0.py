# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 22:21:15 2021

@author: 86182
"""

import copy
alist=[1,2,3,4]
blist=alist+[3]
alist.append(5)
clist=alist
print("a_id is ",id(alist),"b_id is ",id(blist),"c_id is ",id(clist))
#append 函数不改变原有数值的位置，“+”会开辟一个新的空间，“=”是浅拷贝
#新创建的变量和原变量指向同一值
#%%
alist=[1,2,[3,4]]
dlist=copy.copy(alist)
print(id(dlist))
alist[1]=89
alist[2][0]="hahaha"
#浅拷贝只是针对列表中的嵌入部分，对于链表中的
#元素，采取的是深拷贝
#%%

elist=copy.deepcopy(alist)
print(id(elist))
#%%
origin = [1, 2, [3, 4]]
cop1 = copy.copy(origin)
cop2 = copy.deepcopy(origin)
origin[2][0] = "hey!" 
