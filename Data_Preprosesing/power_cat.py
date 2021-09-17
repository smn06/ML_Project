import pandas as pd
import random as rd
import numpy as np

data = pd.read_csv('../Data_Set/Final/test_data.csv')
x = pd.DataFrame(data.iloc[:,:].values)

# print(x)
li_1 = [0,-1]
li_2 = [1]
li_3 = [2]

## Characters
# for i in range(len(data)):
for i in range(len(data)):
    # print(x.iloc[i,-1])
    if x.iloc[i,2] in li_1:
        data.iloc[i,7] = rd.randint(1,3)
    elif x.iloc[i,2] in li_2:
        data.iloc[i,7] = rd.randint(4,7)
    elif x.iloc[i,2] in li_3:
        data.iloc[i,7] = rd.randint(8,10)
    print(i)

        
data.to_csv("../Data_Set/Final/test.csv",index = False, header = True)

    



