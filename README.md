# 🎭 Sentiment Analysis Web App

A machine learning-powered web application that analyzes text reviews and predicts whether the sentiment is **Positive**, **Negative**, or **Neutral** — complete with confidence scoring and emoji-based visual feedback.

---

## 🌟 Overview

This project bridges the gap between raw text data and actionable sentiment insights. Users can input any review or piece of text, and the app instantly classifies the sentiment using a pre-trained machine learning model served via a Flask backend.

Whether it's a product review, a tweet, or customer feedback — this app gives you the sentiment in seconds.

---

## 🚀 Features

- 🎯 **Real-time Sentiment Prediction** — Positive 😄, Negative 😞, or Neutral 😐
- 📊 **Confidence Scoring** — Displays prediction probability so you know how certain the model is
- 🎨 **Clean, Responsive UI** — Minimal, distraction-free interface with custom styling
- ⚡ **Fast Inference** — Pre-trained model loaded via Pickle for near-instant predictions
- 💬 **Emoji Feedback** — Visual indicators for quick sentiment interpretation

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| Machine Learning | scikit-learn |
| Model Storage | Pickle (`.pkl`) |
| Frontend | HTML5, CSS3 |
| Text Processing | CountVectorizer / TF-IDF Vectorizer |

---

## 📁 Project Structure

```
sentiment-analysis/
│
├── app.py                  # Flask application entry point
├── model.pkl               # Pre-trained sentiment classification model
├── vectorizer.pkl          # Fitted text vectorizer (TF-IDF / CountVectorizer)
├── requirements.txt        # Python dependencies
│
├── templates/
│   └── index.html          # Main UI template
│
└── static/
    └── style.css           # Custom CSS styling
```

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.7+
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/adarshv15/sentiment-analysis.git
cd sentiment-analysis
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Visit **http://localhost:5000** in your browser.

---

## 🧠 How It Works

```
User Input (Text Review)
        │
        ▼
Text Preprocessing
(Lowercasing, Punctuation Removal)
        │
        ▼
Vectorization
(TF-IDF / CountVectorizer → Numerical Features)
        │
        ▼
ML Model Inference
(scikit-learn Classifier → Prediction + Probabilities)
        │
        ▼
Flask Response
(Sentiment Label + Confidence Score)
        │
        ▼
UI Display
(Emoji + Label + Confidence %)
```

---

## 🎯 Model Details

- **Algorithm:** Logistic Regression / Naive Bayes / SVM *(based on your trained model)*
- **Vectorizer:** TF-IDF or CountVectorizer fitted on training corpus
- **Classes:** Positive, Negative, Neutral
- **Storage:** Serialized via `pickle` for fast loading at runtime

---

## 📦 requirements.txt

```
flask
scikit-learn
numpy
pandas
pickle5
```

---

## 🖥️ API Reference

### `POST /predict`

Accepts a text input and returns the predicted sentiment.

**Request Body:**
```json
{
  "review": "This product is absolutely amazing!"
}
```

**Response:**
```json
{
  "sentiment": "Positive",
  "confidence": 94.7,
  "emoji": "😄"
}
```

---

## 📸 Screenshots

> *(Add your screenshots here)*

| Input Screen | Prediction Result |
|---|---|
| ![Input](screenshots/input.png) | ![Result](screenshots/result.png) |

---

## 🔮 Future Improvements

- [ ] Support for batch review analysis (CSV upload)
- [ ] REST API with JSON responses for third-party integration
- [ ] Fine-tuned BERT / transformer model for higher accuracy
- [ ] Sentiment trend visualization over multiple inputs
- [ ] Docker containerization for easy deployment

---

## 👨‍💻 Author

**Adarsha V**
- GitHub: [@adarshv15](https://github.com/adarshv15)
- Email: adarsh80737@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with 🐍 Python + Flask + scikit-learn*
