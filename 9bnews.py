import streamlit as st
from scraping_news import pull_articles

st.title("Planet Mountain News Roundup")

user_input = st.text_input("What would you like to search for? (Default: '9b')", '9b')
num_pages = st.slider("Number of pages to scan", min_value=1, max_value=20)
scan_button = st.button("Scan")

c1, c2, c3 = st.beta_columns(3)

if scan_button:
    articles, thumbs, links = pull_articles(num_pages, user_input)
    for article in range(len(articles)):
        c1.write(thumbs[article])
        c2.write(articles[article])
        c3.write(links[article])
else:
    pass








# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def counter():
#     return render_template('9bnews.html', posts=posts)

