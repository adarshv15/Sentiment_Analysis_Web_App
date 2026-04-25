from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['review']
    prediction = model.predict([text])[0]
    probabilities = model.predict_proba([text])[0]
    confidence = max(probabilities) * 100

    if prediction == 1:
        sentiment = "Positive 😄"
        sentiment_class = "positive"
        fill_class = "green-fill"
    elif prediction == 0:
        sentiment = "Negative 😞"
        sentiment_class = "negative"
        fill_class = "red-fill"
    else:
        sentiment = "Neutral 😐"
        sentiment_class = "neutral"
        fill_class = "yellow-fill"

    return render_template('index.html',
                           review=text,
                           sentiment=sentiment,
                           confidence=round(confidence, 2),
                           sentiment_class=sentiment_class,
                           fill_class=fill_class)

if __name__ == '__main__':
    app.run(debug=True)
