import streamlit as st
from transformers import pipeline

# Sidebar Section
st.sidebar.title('Example Prompt')
example_prompt = """
The Eurozone, also known as the Euro area, is the economic union of 19 of the 28 member states of the European Union. It is the world's second-largest economy by nominal GDP, after the United States. The Eurozone is characterized by a single currency, the euro, which is used by nearly all Eurozone members. The Eurozone also uses the Euro as a reserve currency, and the ECB serves as the official central bank of the Eurozone. The Eurozone is home to 42% of the world's population and 30% of its GDP.
"""
st.sidebar.write(example_prompt)

# Main Section
st.title('Article Summarizer')

# Input Section
st.write("Enter a long article in the main input section and click the 'Summarize' button to generate a summary.")
article = st.text_area("Enter the Article here:")

# Button to Summarize
if st.button("Summarize"):
    summarizer = pipeline("summarization", model="Falconsai/text_summarization")

    summary = summarizer(article, max_length=100, min_length=30, do_sample=False)
    st.success('Summary:')
    st.write(summary[0]['summary_text'])


# About Section
st.header('About')
st.write("This app uses Hugging Face's Transformers library to summarize articles. It is built using Streamlit, a Python library for building web applications for machine learning and data science.")
st.write("The code is open source and can be found on GitHub:https://github.com/achuajays/AI-Article-Summarizer")

