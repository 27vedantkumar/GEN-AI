'''This is file which is made to the install the streamlit dependencies and practice the same here .'''
# To Run the code : streamlit run project2.py
import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# First Streamlit app

# st.title("My first Streamlit App")
# st.write("Hello,Welcome to my first Streamlit Application")
# st.write("Streamlit allows us to build apps using only python!")

# text and markdow display

# st.title("text display in streamlit")
# st.header("this is a header")
# st.subheader("this is a sub-header")
# st.text("this is a plain text.")
# st.markdown("""
# ###Markdown support  
# you can write **bold-text**,*italic-text*, and create list:
# - Item 1
# - Item 2
# - Item 3
#             """)

# User Input & Text Input

# st.title("User Input Example")
# name=st.text_input("Enter your name")
# if name:
#     st.write(f"Hello {name} , Welcome to my streamlit app.")

# Sliders & Numbers Input

# st.title("Interative Sliders")
# age=st.slider("Select your age", 0, 100, 25)
# st.write("Your age is:",age)
# number=st.number_input("Enter a number",min_value=0,max_value=100)
# st.write(f"You entered: {number}")

# select buttons & actions 

# st.title("Button Example")
# if st.button("Click Me"):
#     st.success("You clicked the button!!")

#select box & dropdown 

# st.title("Select Box Example")
# language=st.selectbox("Choose your fav programming language",[" ","A","B","C","D"])
# st.write("You selected : ",language)

# SideBar Layout

# st.title("Main Page ")
# st.sidebar.title("SieBar Menu")
# option=st.sidebar.selectbox("Choose a page",
#                    ["","Home","About","Contact"]  )
# st.write(f"You selected: {option}")

# Column Layout

# st.title("Column Layout")
# col1,col2=st.columns(2)
# with col1:
#     st.header("Column 1")
#     st.write("This is the first column")
# with col2:
#     st.header("Column 2")
#     st.write("This is the second column")

#  Display Data in UI

# st.write("Displaying Data")
# data={
#     "Name": ["Vishal","Mudhu","Alexandar"],
#     "City": ["Kolkata","Bihar","Himachal Pradesh"]}
# df=pd.DataFrame(data)
# st.dataframe(df)

# #  Charts in StreamLit

# st.title("Charts Example")
# data=pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=["A", "B", "C"]
# )
# st.line_chart(data)

# File Upload

# st.title("File Upload Example")
# uploaded_file = st.file_uploader("Upload a CSV file", type=["csv","xlsx"])
# if uploaded_file is not None:
#     df=pd.read_csv(uploaded_file)
#     st.write("Preview of uploaded Data")
#     st.dataframe(df.head())

# Containers

# st.title("container Example")
# with st.container():
#     st.write("This is inside a conainer.")
#     st.write("Useful for grouping Components.")

# st.write("Outside the Container.")

# Session State

# st.title("Session State example")
# if "counter" not in st.session_state:
#     st.session_state.counter=0
# if st.button("Increase Counter"):
#     st.session_state.counter += 1
# st.write("Container value:",st.session_state.counter)

# Capstone project

st.set_page_config(page_title="personal Finance dashboard",layout="wide")
st.title("Personal Finance Dashboard")
st.write("Upload your Expense CSV file to analyse your spending habits.")

st.sidebar.header("Upload your data")
uploaded_file=st.sidebar.file_uploader("Upload Expense CSV",type=["csv"])
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    df["Date"] = pd.to_datetime(df["Date"])
    st.sidebar.header("Filters")
    category_filter=st.sidebar.multiselect(
        "Select Category",
        options=df["Category"].unique(),
        default=df["Category"].unique()
    )
    payment_filter=st.sidebar.multiselect(
        "Payment Mode",
        options=df["Payment_Mode"].unique(),
        default=df["Payment_Mode"].unique()
    )
    filtered_df=df[
        (df["Category"].isin(category_filter)) & (df["Payment_Mode"].isin(payment_filter))
    ]
    total_spent =filtered_df["Amount"].sum()
    avg_spent =filtered_df["Amount"].mean()
    max_spent =filtered_df["Amount"].max()
    col1,col2,col3=st.columns(3)

    col1.metric("Total Spending ", f"Rs.{total_spent:,.2f}")
    col2.metric("Average Spending ", f"Rs.{avg_spent:,.2f}")
    col3.metric("Highest Expense", f"Rs.{max_spent:,.2f}")

    st.divider()

    st.subheader("Spending By Category")
    category_data=filtered_df.groupby("Category")["Amount"].sum()
    fig1,ax1=plt.subplots()
    category_data.plot(kind="bar",ax=ax1)
    ax1.set_ylabel("Amount Spent")
    ax1.set_xlabel("Category ")
    st.pyplot(fig1, use_container_width=False)

    st.divider() 

    # Monthly Trend
    st.subheader("📈 Monthly Spending Trend")

    filtered_df["Month"] = filtered_df["Date"].dt.to_period("M")

    monthly_data = filtered_df.groupby("Month")["Amount"].sum()

    # fig2, ax2 = plt.subplots()
    fig2, ax2 = plt.subplots(figsize=(4,2))
    monthly_data.plot(kind="line", marker="o", ax=ax2)
    ax2.set_ylabel("Amount")
    ax2.set_xlabel("Month")

    # st.pyplot(fig2)
    st.pyplot(fig2, use_container_width=False)

    st.divider()

    # Raw Data
    st.subheader("📄 Transaction Data")

    st.dataframe(filtered_df)

else:
    st.info("Please upload a csv file to begin the analysis ")


