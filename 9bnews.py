import streamlit as st
from scraping_news import pull_articles
import pandas as pd

def make_clickable(link, text):
    return f'<a target="_blank" href="{link}">{text}</a>'

st.title("Planet Mountain News Roundup")

user_input = st.text_input("What would you like to search for? (Default: '9b')", '9b')
num_pages = st.slider("Number of pages to scan", min_value=1, max_value=20)
scan_button = st.button("Scan")

# c1, c2 = st.beta_columns(2)

# if scan_button:
#     articles, thumbs, links = pull_articles(num_pages, user_input)
#     for article in range(len(articles)):
#         c1.image(thumbs[article])
#         link = make_clickable(links[article], articles[article])
#         df = pd.DataFrame(link, columns=['Link'])
#         c2.write(df['Link'].to_html())
# else:
#     pass

if scan_button:
    articles, thumbs, links = pull_articles(num_pages, user_input)
    data = list(zip(thumbs, articles, links))
    df = pd.DataFrame(data)
    df[0][:].to_html()
    st.table(df)
else:
    pass














# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def counter():
#     return render_template('9bnews.html', posts=posts)

