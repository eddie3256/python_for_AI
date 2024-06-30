import pandas as pd

def to_str(value):
    value = str(value)[::-1]
    for i in range(1, len(value)):
        if i % 3 == 0:
            value = f"{value[:i]},{value[i:]}"
    return value[::-1]
    

df1 = pd.read_csv('上市公司資料.csv')
df2 = df1.iloc[:, 2:7]
df3 = df2.set_index("公司名稱")

df3["公司代號"] = df3["公司代號"].astype(int)
df3["營業收入-當月營收"] = df3["營業收入-當月營收"].map(to_str)
df3["營業收入-上月營收"] = df3["營業收入-上月營收"].map(to_str)
df3 #直接print格式會跑掉