import streamlit as st
from imdb import IMDb
from transformers import pipeline
import torch
import nltk
nltk.download('punkt')  # Needed for tokenization

# Load Hugging Face pipelines
summarizer = pipeline("summarization", model="t5-small")
sentiment_analyzer = pipeline("sentiment-analysis")

# App Title
st.set_page_config(page_title="IMDB Review Summarizer & Sentiment Analyzer", layout="centered")
st.title("🎬 IMDB Review Summarizer & Sentiment Analyzer")

# Movie Name Input
movie_name = st.text_input("Enter a movie name", "")

if movie_name:
    with st.spinner("Fetching movie details from IMDb..."):
        ia = IMDb()
        movies = ia.search_movie(movie_name)

        if not movies:
            st.error("❌ Movie not found. Try another one.")
        else:
            movie = movies[0]
            ia.update(movie)

            title = movie.get('title')
            plot = movie.get('plot outline') or "No plot available."
            full_plot = movie.get('plot', ["No detailed plot found."])[0]

            st.subheader(f"🎞️ Movie: {title}")
            st.write("📝 **Plot Summary:**")
            st.info(plot)

            # Abstractive Summarization
            st.write("🔍 **Summarized Plot (abstractive):**")
            summary = summarizer(full_plot, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
            st.success(summary)

            # Sentiment Analysis
            st.write("💬 **Sentiment Analysis on Plot Summary:**")
            sentiment = sentiment_analyzer(summary)[0]
            st.metric("Sentiment", sentiment['label'], f"Confidence: {sentiment['score']:.2f}")
