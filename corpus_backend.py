# Chatbot corpus backend file

import random

chatbot_corpus = {
    "greeting": {
        "keywords": ["hi", "hello", "hey", "hii"],
        "responses": [
            "Hello! 👋 I am your Bank Assistant.",
            "Hi there! How can I help you today?",
            "Welcome to the Bank Portal 😊"
        ]
    },

    "about_project": {
        "keywords": ["project", "about project"],
        "responses": [
            "This is a Bank Loan Prediction project using Machine Learning.",
            "The project predicts whether a customer will get loan approval."
        ]
    },

    "bank_portal": {
        "keywords": ["bank portal", "portal"],
        "responses": [
            "The Bank Portal allows users to explore data and predict loan approval."
        ]
    },

    "model": {
        "keywords": ["model", "algorithm"],
        "responses": [
            "CatBoost classifier is used for loan prediction."
        ]
    },

    "dataset": {
        "keywords": ["dataset", "data"],
        "responses": [
            "The dataset contains customer financial and demographic data."
        ]
    },

    "prediction": {
        "keywords": ["predict", "prediction"],
        "responses": [
            "The model predicts loan approval based on customer details."
        ]
    }
}

def get_chatbot_response(user_text):
    user_text = user_text.lower()

    for intent in chatbot_corpus.values():
        for keyword in intent["keywords"]:
            if keyword in user_text:
                return random.choice(intent["responses"])

    return "I am still learning 🤖 Please ask about the project, model, or dataset."
