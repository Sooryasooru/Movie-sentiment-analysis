# Movie-sentiment-analysis
A NLP project using Hugging Face Transformers to summarize IMDB movie reviews and analyze sentiment (Positive, Negative, Neutral). Uses T5 for abstractive summarization and BERT for sentiment classification. Results are saved, visualized, and exported to CSV.


A Natural Language Processing (NLP) project built with Hugging Face Transformers that summarizes IMDB movie reviews using T5 and performs sentiment analysis using a BERT-based model. The final results are visualized and exported for further analysis.
---------------------------
This project overview ::
--------------------------

Takes real-world IMDB reviews (CSV input or user input).

Uses T5 to generate abstractive summaries.

Classifies reviews as Positive, Negative, or Neutral using a BERT sentiment model.

Cleans and standardizes output.

Visualizes sentiment distribution (bar chart and pie chart).

Saves the final results to a CSV file.

---------
Features
--------
✅ Abstractive summarization using t5-base
✅ Sentiment analysis using nlptown/bert-base-multilingual-uncased-sentiment
✅ Data cleaning & mapping of sentiment labels
✅ Visualization using Matplotlib
✅ CSV output for summaries + sentiment + confidence
✅ Works seamlessly in Google Colab


Tech Stack / Tools Used

Tool	                                       Purpose
-----------------------------------------------------------------------------------

Transformers	          -        Load pre-trained models for summarization and sentiment
T5-base	                -                Abstractive summarization
BERT (nlptown)	        -         Multilingual sentiment analysis
pandas	                -       Data handling and CSV I/O
nltk	                  -         Tokenization (punkt)
matplotlib	            -         Data visualization
zipfile, os	            -        File extraction and management
google.colab.files	    -      Upload/download support in Colab



Acknowledgements
----------------
Hugging Face Transformers

IMDB Movie Dataset

NLTK Tokenizers


As a conclusion this project demonstrates the real-world power of NLP by combining transformer-based summarization and sentiment analysis on movie reviews. By automating the understanding of lengthy user opinions, it not only reduces manual effort but also enables faster insights into audience emotions. Whether you're building a review analyzer, a recommender system, or a customer feedback dashboard, this project provides a scalable foundation for intelligent, language-aware applications. Future enhancements like Streamlit integration, live user input, or multilingual support can further extend its impact in real-world deployments.

Thank you
