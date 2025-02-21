import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Step 1: Load the CSV file
data = pd.read_csv('body.csv')  # Make sure 'body.csv' is in the same directory

# Step 2: Check the data structure
print("Data Preview:")
print(data.head())

# Step 3: Clean the text
def clean_text(text):
    if not isinstance(text, str):
        return ""  # Return empty string if the text is not valid
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)  # Remove numbers
    return text

# Apply the cleaning function to the Body column
data['cleaned_body'] = data['Body'].apply(clean_text)

print("\nCleaned Data Preview:")
print(data['cleaned_body'].head())

# Step 4: Create labels (Dummy categories for demonstration)
data['category'] = [1, 2, 1, 3, 2]  # Replace with real categories if available

# Step 5: Vectorize the text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['cleaned_body'])
y = data['category']

# Step 6: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=162)

# Step 7: Train a Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Step 8: Test the model's accuracy
accuracy = model.score(X_test, y_test)
print(f"\nModel Accuracy: {accuracy:.2f}")

# Step 9: Make predictions on user input
def predict_category(text):
    cleaned_text = clean_text(text)
    vectorized_text = vectorizer.transform([cleaned_text])
    predicted_category = model.predict(vectorized_text)
    return predicted_category[0]

# Step 10: Get user input and predict category
while True:
    user_input = input("\nEnter text to classify (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    predicted_category = predict_category(user_input)
    print(f"Predicted Category: {predicted_category}")
