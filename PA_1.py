import pandas as pd
MT = {'Student':['Ice Bear','Panda','Grizzly'],
      'Math':[80,95,79]}
ELT = {'Student':['Ice Bear','Panda','Grizzly'],
       'Electronics':[85,81,83]}
GS = {'Student':['Ice Bear','Panda','Grizzly'],
      'GEAS':[90,79,93]}
ET = {'Student':['Ice Bear','Panda','Grizzly'],
      'ESAT':[93,89,88]}

math = pd.DataFrame(MT, columns = ['Student','Math'])
electronics = pd.DataFrame(ELT, columns = ['Student','Electronics'])
geas = pd.DataFrame(GS, columns = ['Student','GEAS'])
esat = pd.DataFrame(ET, columns = ['Student','ESAT'])

wbb = pd.merge(math,electronics, how= 'inner', on= 'Student')
wbb2 = pd.merge(wbb,geas, how= 'inner', on= 'Student')
wbb3 = pd.merge(wbb2,esat, how= 'inner', on= 'Student')

looong = pd.melt(wbb3, id_vars = 'Student', value_vars = ['Math','Electronics','GEAS','ESAT'])
fformat = looong.rename(columns = {'variable': 'Subject', 'value': 'Grades'}) 