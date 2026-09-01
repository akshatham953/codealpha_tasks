# CodeAlpha Task 4: Sentiment Analysis

## Objective
Analyze text data to classify sentiment as Positive, Negative, or Neutral

## Tools Used
Python, TextBlob, Pandas, Matplotlib

## How it Works
Uses TextBlob to calculate polarity score from -1 to 1
> 0.1 = Positive, < -0.1 = Negative, else Neutral

## How to Run
pip install textblob pandas
python -m textblob.download_corpora
python task4_sentiment.py

## Output
sentiment_results.csv, sentiment_chart.png