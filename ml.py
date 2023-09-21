import xgboost as xgb
import seaborn as sns
import numpy as np # linear algebra
import matplotlib.pyplot as plt
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from matplotlib.pyplot import figure

train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("storeitem_test.csv")
df = pd.concat([train_data,test_data],sort=False)
print(df.head(10))


#Look at best selling store
stores_stats = df.groupby(["store"]).agg({"sales": ["count","sum", "mean", "median", "std", "min", "max"]})
print(stores_stats.head(10))
#Look at Best Selling Item
item_stats = df.groupby(["item"]).agg({"sales": ["count","sum", "mean", "median", "std", "min", "max"]})
print(item_stats.head(50))


stores_sum = df.groupby(["store"],as_index=False).agg({"sales": "sum"}).sort_values(by="sales",ascending=False)
sns.barplot(data=stores_sum,x='store',y='sales',color="green",order=stores_sum.sort_values('sales').store)