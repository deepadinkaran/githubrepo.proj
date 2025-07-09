import pandas as pd
data=pd.read_excel(r"C:\Users\asus\Downloads\Dataset for Sessions\Coffee Chain - DataModel.xlsx")
data.head()
data.tail()

data.info()
data.isnull().sum()
data.duplicated()

data['Date']=pd.to_datetime(data['Date'],errors='coerce')
print(data)
 

#performing EDA
#sales by product
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
sns.barplot(data=data,x="Product" , y="Sales")
plt.title=("Sales by category")
plt.show()

#Profit by State
plt.figure(figsize=(10,5))
sns.barplot(data=data,x='State',y='Profit')
plt.title=("Profit by state")
plt.show()


import sqlite3
conn=sqlite3.connect("coffee_chain.db")
data.to_sql('coffeesales',conn,if_exists="replace",index=False)


import sqlite3
from  sqlalchemy import create_engine
data=pd.read_excel(r"C:\Users\asus\Downloads\Dataset for Sessions\Coffee Chain - DataModel.xlsx")
engine = create_engine('mysql+mysqlconnector://root:DEEPA_DINAKARN@localhost/coffee_db')
data.to_sql('coffeesales', con=engine, if_exists='replace', index=False)
print(" Data imported into MySQL successfully")
print (data)


