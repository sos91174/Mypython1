#!/usr/bin/env python
# coding: utf-8

# In[1]:
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



car={}

def car_name():

    name=input("請輸入車子名字:")
    year=input("請輸入年份:")
    door=input("請輸入幾門車:")
    color=input("請輸入車子顏色:")
    cc=input("請輸入車子CC數:")
    price=input("請輸入價錢(萬):")


    fn = 'data0507.csv'#複寫到CSV
    with open(fn,'a',newline = '',encoding='utf8') as csvFile:
        csvWriter=csv.writer(csvFile)
        csvWriter.writerow(["{d1}".format(d1=name),"{d2}".format(d2=year),"{d3}".format(d3=door),
                           "{d4}".format(d4=color),"{d5}".format(d5=cc),"{d6}".format(d6=price)])
    print("")#空格用
    print("你已經新增完畢")
    print("▼▼▼▼▼▼以下列表是本廠目前有販售的車輛▼▼▼▼▼▼")
    menu=pd.read_csv('data0507.csv',engine='python',encoding='utf8')
    
    print(menu)
    
    
def search():#查詢車子清單
    
    print("")#空格用
    print("")
    print("▼▼▼▼▼▼以下列表是本廠目前有販售的車輛▼▼▼▼▼▼")
    search=pd.read_csv('data0507.csv',engine='python',encoding='utf8')
    
    print(search)
    
    
    
def del_car():
    
    delcar=pd.read_csv('data0507.csv',engine='python',encoding='utf8')
    print("")
    print("▼▼▼▼▼▼你要刪除哪台車子▼▼▼▼▼▼")

    
    delcar.drop([int(input("請輸入數字"))],inplace=True)
    print("")
    print("你已經刪除完畢")
    print("")
    print(delcar)
    
    
    
    
    
#      delcar=pd.read_csv('data0507.csv',engine='python',encoding='utf8')
#      delcar.drop([int(input("你要刪除哪輛車(請輸入數字)"))].index,inplace=True)
#      delcar.to_csv('data0507.csv',index=False)
    
#      fn = 'data0507.csv'#複寫到CSV
#      with open(fn,'r',newline = '',encoding='utf8') as csvFile:
#         csvWriter=csv.writer(csvFile)
    
        

    
#  def car_pic():

#     # x = [70,80,90,100,110,120,130,140,150]
#     y = [1980,570,1000,300,560,300,120,80,60]

#     t1 = ["Ferrari","Maserrati","Porsche","Tesla","BMW","BENZ",
#      "CR-V","HR-V","Yaris"]

#     plt.figure(figsize = (8,4))

#     plt.bar(x, y,width = 5,tick_label=t1, label = "(\/)@.@(\/)")
#     plt.legend()
#     plt.xlabel("Car")
#     plt.ylabel("price  (10K)")
#     plt.title("Car yesterday price menu")


#     plt.show()

    
    
    
    



    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




