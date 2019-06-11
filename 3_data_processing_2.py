import pandas as pd

a=pd.read_excel("C:\\Users\\karyan\\PycharmProjects\\tens\\name_list.xlsx")

c='M\xdcLLER'

print(str(c))

for i in range(0,len(a.user_name)):
    b = '%s' % a.user_name[i]
    print(b)
