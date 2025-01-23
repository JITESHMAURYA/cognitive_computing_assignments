import pandas as pd
data=pd.read_csv('file.csv')

data.drop(4,axis=0,inplace=True)  
data.drop("RNO",axis=1,inplace=True) 
print(data)

import csv

with open('employees.csv','w',newline='') as file:
  writer=csv.writer(file)
  writer.writerow(["Employee_ID","Name","Department","Age","Salary","Years_of_Experience","Joining_Date","Gender","Bonus","Rating"])
  writer.writerow([101,"Jitesh","HR",29,50000,4,"2020-03-15","Male",6000,7.0])
  writer.writerow([102,"Gordon","IT",34,70000,8,"2017-07-19","Male",5000,5.0])
  writer.writerow([103,"James","IT",41,65000,10,"2013-06-01","Male",4000,4.9])
  writer.writerow([104,"Kringle","Marketing",28,55000,3,"2021-02-10","Female",5500,6.8])
  writer.writerow([105,"Carmine","Sales",38,60000,12,"2010-11-25","Male",7500,8.5])
