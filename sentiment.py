from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

print("=== CODEALPHA TASK 4: SENTIMENT ANALYSIS ===")

# 1. SAMPLE DATA - You can change these to any reviews/tweets
reviews = [
    "I love this product! It's good and works perfectly.",
    "This is the worst experience ever. Very disappointed.",
    "The product is okay. Nothing special but works fine.",
    "Absolutely fantastic! Best purchase I have made.",
    "Terrible quality. Do not buy this.",
    "It's decent for the price.",
    "I am so happy with the service!",
    "Waste of money. Very bad.",
    "Average product. Could be better.",
    "Excellent! Highly recommend to everyone."
]

# 2. ANALYZE SENTIMENT
sentiment_data = []

for review in reviews:
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity  # -1 to 1
    
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    sentiment_data.append({
        'Review': review,
        'Polarity': round(polarity, 2),
        'Sentiment': sentiment
    })

# 3. CREATE DATAFRAME
df = pd.DataFrame(sentiment_data)

print("\n1. SENTIMENT ANALYSIS RESULTS:")
print(df)

# 4. SUMMARY STATS
print("\n2. SUMMARY:")
print(df['Sentiment'].value_counts())
print(f"\nPositive: {len(df[df['Sentiment']=='Positive'])}")
print(f"Negative: {len(df[df['Sentiment']=='Negative'])}")
print(f"Neutral:  {len(df[df['Sentiment']=='Neutral'])}")

# 5. VISUALIZATION
plt.figure(figsize=(8, 5))
df['Sentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'gray'])
plt.title('Sentiment Analysis Results')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('sentiment_chart.png')
print("\nChart saved as 'sentiment_chart.png'")

# 6. SAVE RESULTS
df.to_csv('sentiment_results.csv', index=False)
print("Results saved as 'sentiment_results.csv'")

print("\n=== SENTIMENT ANALYSIS COMPLETE ===")