# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 10:28:59 2017

@author: aditya royal
"""
from sklearn.svm import SVC
import numpy as np
import csv
import pandas as pd
from StringIO import StringIO
train=pd.read_csv('D:/MLsoftaware_projects/titanic/train.csv')
train = train.drop(['Survived'], axis=1)
x_train = np.array(train)
titanic=np.genfromtxt('D:/MLsoftaware_projects/titanic/train.csv',skip_header=1,delimiter=',',dtype=None)
csv_open=open('D:/MLsoftaware_projects/titanic/train.csv','rb')
csv_obj=csv.reader(csv_open)
csv_obj.next()
data=[]
for row in csv_obj:
    data.append(row)
data=np.array(data)   
survived=data[:,1].astype(int)
x=data[:,5:8].astype(int)
from sklearn.svm import SVC
svc=SVC()
svc.fit(x,survived)
new=[]
with open('D:/MLsoftaware_projects/titanic/test.csv','rb') as openr:
    csv_obj=csv.reader(openr)
    csv_obj.next()
    for row in csv_obj:
        new.append(row)
def f(x):
    return np.float(x)
    f2=np.vectorize(f)
new=np.array(new) 
pd.DataFrame(new).fillna(0)
#float_fun(new[:,4:7])
x_test=f2(new[:,4:7])
#svc.predict(x_test)
#sv.predict()