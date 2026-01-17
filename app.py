# UPDATED ON 17 JAN 2026 - CHATBOT BACKEND CONNECTED

import pandas as pd
import streamlit as st
import plotly.express as px
import joblib
import numpy as np
from catboost import Pool

from corpus_backend import get_chatbot_response

# ---------------- PAGE STYLE ----------------
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://image2url.com/images/1760272830534-be75a8a2-04b6-4189-a1dd-bd814748afe9.jpeg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    button[data-baseweb="tab"] {
    font-size: 14px;
    padding: 6px 10px;
    color: #555;
}
button[data-baseweb="tab"][aria-selected="true"] {
    color: #0d6efd;
    border-bottom: 2px solid #0d6efd;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
cbc = joblib.load("catboost_classifier.pkl")

# ---------------- TITLE ----------------
st.title("🏧 Bank Portal")

# ---------------- LOAD DATA ----------------
try:
    df = pd.read_csv("data/bank_data.csv", sep=";")
    st.success("👍 Dataset successfully loaded")
except FileNotFoundError:
    st.error("❌ Dataset not found")
    st.stop()

# ---------------- SESSION STATES ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- TABS ----------------
tabs = st.tabs(["🏠 Home", "🤖 AI Assistant", "🔐 Login", "📊 Visuals", "🏦 Prediction"])

# ================= TAB 1: HOME =================
with tabs[0]:
    st.subheader("🏠 Welcome to the Bank Loan Prediction Portal")

    st.markdown("""
    The **Bank Loan Prediction Portal** is a Machine Learning based web application 
    that helps analyze customer data and predict loan approval decisions.

    ### 🔑 What you can do here
    • Explore bank customer data  
    • Chat with an AI assistant (no login required)  
    • View visual insights after login  
    • Predict loan approval using an ML model  

    ### 🧠 ML Model
    - Algorithm: **CatBoost Classifier**
    - Task: Binary classification (Loan Approved / Not Approved)

    ### 🔐 Access Note
    Chatbot is publicly accessible, while **visuals and predictions require login**.

    This project demonstrates end-to-end ML deployment using **Streamlit**.
    """)

    st.info("👉 Tip: Try the Chatbot first or Login to access full features.")

# ================= TAB 2: LOGIN =================
# ================= TAB 2: LOGIN =================
with tabs[2]:
    st.subheader("🔐 Demo Login")

    st.markdown("Use the demo credentials below to explore the full application.")

    st.info("""
    **Demo Credentials**

    Username: **palak**  
    Password: **password1**
    """)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # initialize message flag
    if "login_msg" not in st.session_state:
        st.session_state.login_msg = ""

    if st.button("Login"):
        if username == "palak" and password == "password1":
            st.session_state.logged_in = True
            st.session_state.login_msg = "success"
        else:
            st.session_state.login_msg = "error"

    # 🔽 MESSAGE SHOWS **BELOW LOGIN**
    if st.session_state.login_msg == "success":
        st.success("✅ Logged in successfully!")
        st.info("👉 Now you can use the **Visuals** and **Prediction** tabs.")

    elif st.session_state.login_msg == "error":
        st.error("❌ Invalid demo credentials")

# ================= TAB 3: CHATBOT (PUBLIC) =================
with tabs[1]:
    st.subheader("🤖 AI ChatBot")

    # Initialize states
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "chat_key" not in st.session_state:
        st.session_state.chat_key = 0

    # Chat input (dynamic key)
    user_input = st.text_input(
        "Ask me anything:",
        key=f"chat_input_{st.session_state.chat_key}"
    )

    # Handle message
    if user_input:
        response = get_chatbot_response(user_input)
        st.session_state.chat_history.append(("👤 You", user_input))
        st.session_state.chat_history.append(("🤖 Bot", response))
        st.session_state.chat_key += 1   # creates NEW input box
        st.rerun()

    # Display chat
    for sender, msg in st.session_state.chat_history:
        st.markdown(f"**{sender}:** {msg}")

    # Clear chat button 
    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []
        st.session_state.chat_key += 1
        st.rerun()



# ================= TAB 4: VISUALS (LOGIN REQUIRED) =================
with tabs[3]:
    if not st.session_state.logged_in:
        st.warning("🔒 Please login using demo credentials to view visuals.")
    else:
        st.subheader("📊 Data Visualizations")

          # Q1:Age Distribution
        with st.expander("Q1: What is the Age Distribution of Customers?"):    
            st.write("Most clients are aged 20-50,fewer 50-90")
            fig = px.histogram(df, x="age", nbins=20,title ="Age Distribution")
            fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
)
            st.plotly_chart(fig,use_container_width=True)
        # Q2:Job Distribution
        with st.expander("Q2: What is the Job Distribution of Customers?"):    
            st.write("Most clients are blue-collar,management and technician")
            fig = px.pie(df, names="job", title ="Job Distribution")
            fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
)
            st.plotly_chart(fig,use_container_width=True)
        # Q3:Marital Status Distribution
        with st.expander("Q3: What is the Marital Status Distribution of Customers?"):    
            st.write("Most clients are married")
            fig = px.pie(df, names="marital", title="Marital Status Distribution")
            fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
)
            st.plotly_chart(fig, use_container_width=True)
        # Q4:Education Distribution
        with st.expander("Q4: What is the Education Distribution of Customers?"):    
            st.write("Most clients have secondary and tertiary education")
            fig = px.pie(df, names="education",title ="Education Distribution")
            fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
)
            st.plotly_chart(fig,use_container_width=True)
        # Q5:Housing Loan Distribution
        with st.expander("Q5: What is the Housing Loan Distribution of Customers?"):    
            st.write("Most clients do not have housing loan")
            fig = px.pie(df, names="housing",title ="Housing Loan Distribution")
            fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
         )
            st.plotly_chart(fig,use_container_width=True)

        
# ================= TAB 5: PREDICTION (LOGIN REQUIRED) =================
with tabs[4]:
    if not st.session_state.logged_in:
        st.warning("🔒 Please login to predict")
    else:
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
            pred = cbc.predict(input_pool)[0]
            st.success(f"✅ Loan approval prediction for this client: {pred}")
         
