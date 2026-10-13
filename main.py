#print("welcome to sudent analytic dashboard")
from operator import index

import pandas as pd
import numpy as np

df=pd.read_csv("student.csv")  #ye ek variable h jo stud k details ko store kiya h
print(df)  #ya df.head()
print(df.shape)
df.info()  #har col ka type or kitn value h
print("missing values before cleaning:")  #check krega kiska value missing h

print(df.isnull().sum())  #how many value missing in each column
Java_avg=df["Java"].mean()
df["Java"]=df["Java"].fillna(Java_avg)
print("missing values after cleaning:")  #missing value ko java k mean se fill kiya
print(df.isnull().sum())
Subjects=["C++","Java","Python","Sql"]
df["Total"]=df[Subjects].sum(axis=1)
df["Average"]=df[Subjects].mean(axis=1).round(2)
df["Percentage"]=((df["Total"]/(len(Subjects)*100))*100).round(2)
condition1=df["Percentage"]>=90
condition2=df["Percentage"]>=80
condition3=df["Percentage"]>=70
condition4=df["Percentage"]>=60
condition5=df["Percentage"]>=40
choices=["A+","A","B+","B","C"]
df["Grade"]=np.select([condition1, condition2, condition3, condition4, condition5], choices,default="F")
df["Result"]=np.where(df["Percentage"]>=40,"Pass","Fail")
print(df[["Name","Total","Average","Percentage","Grade","Result"]])
df["Rank"]=df["Total"].rank(ascending=False,method="min").astype(int)  #har student k total marks k hisab se rank assign kiya
print("student Result Table")
print(df[["Name","Total","Average","Percentage","Grade","Result","Rank"]])
df.sort_values(by="Rank",inplace=True)  #rank k hisab se sort kiya
print(df.head(3))  #top 3 student ko print kiya
df[Subjects].mean()  #har subject k average marks ko calculate kiya
print("Subject wise average marks")
print(df[Subjects].mean().round(2))
df[Subjects].max()   #har subject k max or min marks ko calculate kiya
print("Subject wise maximum marks")
print(df[Subjects].max())
print("Subject wise minimum marks")
print(df[Subjects].min())
df[Subjects].std()  #har subject k standard deviation ko calculate kiya
print("Subject wise standard deviation")
print(df[Subjects].std().round(2))
print("Subject wise topper student")
top_idx=df[Subjects].idxmax()  #har subject k topper student k index ko calculate kiya
print(dict(zip(Subjects,df.loc[top_idx,"Name"])))  #har subject k topper student k name ko print kiya

df["index"]=df.index  #index ko ek col me store kiye

df.loc[df["index"]==0,"Name"]  #index 0 wale student k name ko print kiya


#DEPARTMENT WISE ANALYSIS
print("Department wise average marks")
print(df.groupby("Department")["Percentage"].mean())   #department wise average marks ko calculate kiya
print("Department wise student count")
print(df["Department"].value_counts())  #department wise student count ko calculate kiya

#ATTENDENCE ANALYSIS
low_attendance_students=df[df["Attendance"]<75]
print("low attendance students")
print(low_attendance_students[["Name","Attendance"]])
print("Total low attendance students:",len(low_attendance_students))  #low attendance student k count ko calculate kiya
print("average attendence:",df["Attendance"].mean().round(2))  #average attendance ko calculate kiya
print("attendence percentage of each student")
print((df["Attendance"]/100).round(2))


#RESULT SUMMARY
print("Result Pass/Fail Summary")
print(df["Result"].value_counts())  #pass or fail student ko count kiya
print("Grade Summary")
print(df["Grade"].value_counts())  #har grade k student ko count kiya
pass_percentage=(df["Result"]=="Pass").mean()*100  #pass student k percentage ko calculate kiya
print("Pass percentage:",pass_percentage.round(2))
df.to_csv("final_result.csv",index=False)  #final result ko csv file me save kiya  (index false isliye likhte h taki csv file koi extra index col na bnae)
print("final result saved to final_result.csv")