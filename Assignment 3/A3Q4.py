import csv

with open('file.csv','w',newline='') as file:
  writer=csv.writer(file)
  writer.writerow(["SNO","NAME","RNO"])
  writer.writerow([1,"jitesh",101])
  writer.writerow([2,"bruce",102])
  writer.writerow([3,"bane",103])
  writer.writerow([4,"oswald",104])
  writer.writerow([5,"salina",105])
  writer.writerow([6,"barbara",106])

import pandas as pd
pd.read_csv('file.csv',nrows=5)