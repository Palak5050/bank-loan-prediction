import pandas as pd
import streamlit as st
import plotly.express as px
import joblib
import numpy as np

from catboost import CatBoostClassifier
from catboost import Pool

from corpus_backend import get_chatbot_response


st.markdown(r"""
    <style>
    .stApp {
        background-image: url("https://image2url.com/images/1760272830534-be75a8a2-04b6-4189-a1dd-bd814748afe9.jpeg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
 </style>
""", unsafe_allow_html=True) 
# cbc= CatBoostClassifier()
cbc=joblib.load("catboost_classifier.pkl")

# title 
st.title("🏧 Bank Portal ")

# load the data
try:
    df = pd.read_csv("data/bank_data.csv",sep=";")
    st.success("👍 Dataset loaded")

except FileNotFoundError:
    st.error("❌ Data not found. Please ensure 'file' is in the correct directory.")
    st.stop()

# sidebar navigation using radio buttons    
section=st.sidebar.radio("Select Section",
                         ["Dataset Preview","Dataset Information","Numerical Summary"])
# section=st.sidebar.checkbox("Select Section",
#                          ["Dataset Preview","Dataset Information","Numerical"])

# Display selected section output in the sidebar
if section=="Dataset Preview":
    view_1=st.sidebar.radio("View Dataset",["Hide","Show"])
    if view_1=="Show":
        st.sidebar.subheader("🎇Dataset Preview")
        st.sidebar.dataframe(df.head())

elif section=="Dataset Information":
    st.sidebar.subheader("ℹ️ Dataset Information")
    col1,col2=st.sidebar.columns(2)
    col1.metric(label="Rows",value=df.shape[0])
    col2.metric(label="Columns",value=df.shape[1])
   
elif section=="Numerical Summary": 
    with st.sidebar.expander("🧮Numerical Summary Options",expanded=False):
        st.write(df.describe())

st.subheader("👽AI ChatBot")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("Ask me anything :")

# simple rule based response 
# def chat_response(text):
#     text = text.lower()
#     if "hi" in text:
#         return "Hello! I am a ChatBot. Designed by Palak."
#     elif "who" in text:
#         return "I am BCA Graduate."
#     else:
#         return "I am still learning.Not able to answering."

# Handle user input
if user_input:
    response = get_chatbot_response(user_input)
    st.session_state.chat_history.append(("you:" +user_input,"Bot:" +response))  

# Display chat history
for user_msg, bot_msg in st.session_state.chat_history:
    st.write(user_msg)
    st.write(bot_msg)

# clear chat history button  

# Manual login section
# sample credentials
credentials = {
    "palak": "password1",
    "admin": "password2",
    "gagan": "password3"
 }
# initilize sesson state for login 
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

## login form
if not st.session_state.logged_in:
    st.subheader("🔐Login Required")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if username in credentials and credentials[username] == password:
            st.session_state.logged_in = True
            st.success(f"🤗 Welcome, {username}!")
        else:
            st.error("❌ Invalid username or password.")

# display the FAQ and prediction section AFTER login
if st.session_state.logged_in:
    st.write(" 😊Welcome to the Bank Portal! ")
    st.subheader("❓ FAQ Section")
        # Q1:Age Distribution
    with st.expander("Q1: What is the Age Distribution of Customers?"):    
            st.write("Most clients are aged 20-50,fewer 50-90")
            fig = px.histogram(df, x="age", nbins=20,title ="Age Distribution")
            st.plotly_chart(fig,use_container_width=True)
        # Q2:Job Distribution
    with st.expander("Q2: What is the Job Distribution of Customers?"):    
            st.write("Most clients are blue-collar,management and technician")
            fig = px.pie(df, names="job", title ="Job Distribution")
            st.plotly_chart(fig,use_container_width=True)
        # Q3:Marital Status Distribution
    with st.expander("Q3: What is the Marital Status Distribution of Customers?"):    
            st.write("Most clients are married")
            fig = px.pie(df, names="marital", title="Marital Status Distribution")
            st.plotly_chart(fig, use_container_width=True)
        # Q4:Education Distribution
    with st.expander("Q4: What is the Education Distribution of Customers?"):    
            st.write("Most clients have secondary and tertiary education")
            fig = px.pie(df, names="education",title ="Education Distribution")
            st.plotly_chart(fig,use_container_width=True)
        # Q5:Housing Loan Distribution
    with st.expander("Q5: What is the Housing Loan Distribution of Customers?"):    
            st.write("Most clients do not have housing loan")
            fig = px.pie(df, names="housing",title ="Housing Loan Distribution")
            st.plotly_chart(fig,use_container_width=True)


        # -----------------------------
# 🏦 Bank Data Prediction (Inputs)
# -----------------------------
    st.subheader("🏦 Bank Data Prediction")
    st.write("Enter client details to predict whether they will subscribe to a term deposit.")

    col1, col2 = st.columns(2)

# === Numerical Inputs ===
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        job = st.selectbox("Job", df["job"].unique())
        marital = st.selectbox("Marital Status", df["marital"].unique())
        education = st.selectbox("Education Level", df["education"].unique())
        default = st.selectbox("Default (Has Credit in Default?)", df["default"].unique())
        housing = st.selectbox("Housing Loan", df["housing"].unique())
        loan = st.selectbox("Personal Loan", df["loan"].unique())
        contact = st.selectbox("Contact Communication Type", df["contact"].unique())
        month = st.selectbox("Month of Contact", df["month"].unique())
        day_of_week = st.selectbox("Day of Week", ["mon", "tue", "wed", "thu", "fri"])

    with col2:
        duration = st.number_input("Call Duration (seconds)", min_value=0, max_value=5000, value=100)
        campaign = st.number_input("Campaign (number of contacts)", min_value=1, max_value=50, value=1)
        pdays = st.number_input("Pdays (days since last contact)", min_value=-1, max_value=999, value=-1)
        previous = st.number_input("Previous (contacts before this campaign)", min_value=0, max_value=50, value=0)
        poutcome = st.selectbox("Previous Campaign Outcome", df["poutcome"].unique())
        emp_var_rate = st.number_input("Employment Variation Rate", value=1.0)
        cons_price_idx = st.number_input("Consumer Price Index", value=93.0)
        cons_conf_idx = st.number_input("Consumer Confidence Index", value=-40.0)
        euribor3m = st.number_input("Euribor 3 Month Rate", value=0.5)
        nr_employed = st.number_input("Number of Employees", value=5000.0)

         
# feature array (Without DataFrame) ===
# NOTE: CatBoost must have been trained with encoded features for this to work directly
    columns = ["age", "job", "marital", "education", "default", "housing", "loan", "contact",
           "month", "day_of_week", "duration", "campaign", "pdays", "previous", "poutcome",
           "emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m", "nr.employed"]
    features = pd.DataFrame([[age, job, marital, education, default, housing, loan, contact,
                          month, day_of_week, duration, campaign, pdays, previous, poutcome,
                          emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed]],
                        columns=columns)
    
    
    

    cat_features = ["job","marital","education","default","housing","loan","contact","month","day_of_week","duration","poutcome"]
    input_pool = Pool(data=features, cat_features=cat_features)

    if st.button("Predict"):
         pred_cb = cbc.predict(input_pool)[0]
 
         st.success(f"✅ Loan approval prediction for this client: {pred_cb}")
         

    # === Predict Button ===
    # if st.button("🔮predict"):
    #     try:
    #         pred_cb = cbc.predict(input_pool)[0]
    #         st.success(f"✅ The predicted class for this client is: {pred_cb}")
    #     except Exception as e:
    #         st.error(f"⚠️ Prediction failed: {e}")
            


