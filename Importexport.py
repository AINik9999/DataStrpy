# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:19:23 2021

@author: JanweBros
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:58:59 2021
@author: Admin
"""
#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('H:/MACHINE LEARNING/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('H:/MACHINE LEARNING/IITk.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('H:/MACHINE LEARNING/User_Data.xlsx')

df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('IIT-B.xlsx')
df3 = pandas.DataFrame(df1)
print (df2)
df.describe()
df2.describe(include='all')
df.to_excel('Trytocsvexcel.xlsx')
