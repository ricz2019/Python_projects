import pandas as pd
 
XYZ_web= {'Day':[1,2,3,4,5,6], "Visitors":[1000, 700,6000,1000,400,350], 
"Bounce_Rate":[20,20, 23,15,10,34]}
 
df= pd.DataFrame(XYZ_web)
 
print(df)
print(df.head(2))
print(df.tail(2))
print(df.to_numpy())
print(df.sort_index())
print(df.describe())
print()


dates = pd.date_range('2001', periods=4)
df1= pd.DataFrame({ "HPI":[80,90,70,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]}, 
	index=dates)
print(dates)
print()
print(df1)
print(df1.to_numpy())
print()
 
df2=pd.DataFrame({ "HPI":[80,90,70,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]}, 
	index=[2005,2006,2007,2008])
print(df2)
merged= pd.merge(df1,df2)
 
print(merged)
print()

merged = pd.merge(df1, df2, on = "HPI")

print(merged)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'