#!/usr/bin/env python
# coding: utf-8

# In[8]:



import matplotlib.pyplot as plt
import numpy as np
import csv

car={}

def pic():#圖表

    x = [70,80,90,100,110,120,130,140,150]
    y = [12,82,42,23,27,33,40,29,50]#銷售數量

    t1 = ["Ferrari","Maserrati","Porsche","Tesla","BMW","BENZ",
         "CR-V","HR-V","Yaris"]#車子

    plt.figure(figsize = (8,4))

    plt.bar(x, y,width = 5,tick_label=t1, label = "(\/)@.@(\/)")
    plt.legend()
    plt.xlabel("Car")
    plt.ylabel("Count")
    plt.title("Car sales")


    plt.show()



# In[ ]:





# In[ ]:





# In[ ]:




