# NLP Part of Master Project – Processing Letters of Ivo Andrić

This is tha smaller part of project from my Master's course in **Natural Language Processing (NLP)**. It focuses on processing, analyzing, and extracting insights from **letters written by Ivo Andrić** using various NLP techniques.

## 📂 Project Structure

### 🔹 Data Files
- **`388.txt`** – Contains a letter written by Ivo Andrić, which serves as the primary text for processing.
- **`annotations.json`** – Stores annotated data for training and testing a **Named Entity Recognition (NER)** model.
- **`data.tsv`** – Used for **sentence classification**.
- **`teme.csv`** – Contains data for **topic modeling**.

### 🔹 NLP Processing Scripts
- **`text_formatter.py`** – Handles **text cleaning** (removes extra blanks, corrects OCR errors).
- **`page388.py`** – Performs **linguistic analysis** on Andrić’s letters using **spaCy** and **NLTK**.
- **`page388_ner.py`** – Trains and tests a **Named Entity Recognition (NER)** model for Croatian using **spaCy**.
- **`sentence_classification_svm.py`** – Implements **sentence classification** using **Support Vector Machines (SVM)**.
- **`key_words_sentiment_analysis_and_topic_modeling.py`** – Extracts **keywords**, performs **sentiment analysis**, and applies **topic modeling** to Andrić’s letters.

### 🔹 Chatbot Implementation
- **`andric_chatbot.py`** – Implements a **chatbot** with a **knowledge base** about Ivo Andrić's letters.

## 🚀 How to Use

1. **Prepare the environment**  
   Install the required dependencies:
   
   pip install spacy nltk scikit-learn pandas

   python -m spacy download hr_core_news_sm

