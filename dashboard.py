import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Analytics", layout="wide")
df = pd.read_csv("final_result.csv")
Subjects = ["C++","Java","Python","Sql"]

st.title("Student Analytics Dashboard")

low = df[df["Attendance"] < 75]
pass_pct = (df["Result"] == "Pass").mean() * 100

c1, c2, c3, c4 = st.columns(4)
c1.metric("Students", len(df))
c2.metric("Pass %", f"{pass_pct:.2f}%")
c3.metric("Avg attendance", f"{df['Attendance'].mean():.2f}%")
c4.metric("Low attendance", len(low))



st.subheader("Student result table")

search = st.text_input("Search student by name or ID")

if search:
    mask = df.astype(str).apply(
        lambda col: col.str.contains(
            search, case=False, na=False
        )
    ).any(axis=1)

    filtered_df = df[mask]
    st.dataframe(filtered_df)

    if filtered_df.empty:
        st.warning("No student found")
else:
    st.dataframe(df)


st.subheader("Top 3 students")
st.dataframe(df.sort_values("Rank").head(3)[["Name","Total","Percentage","Rank"]]) 

st.subheader("Subject-wise average")
st.bar_chart(df[Subjects].mean().round(2))

st.subheader("Department-wise average percentage")
st.bar_chart(df.groupby("Department")["Percentage"].mean().round(2))

st.subheader("Pass / Fail count")
st.bar_chart(df["Result"].value_counts())

st.subheader("Grade-wise count")
st.bar_chart(df["Grade"].value_counts())

st.subheader("Students with attendance below 75%")
st.dataframe(low[["Name","Attendance"]])