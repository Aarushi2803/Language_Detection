# 🌍 Language Detection Using Machine Learning

## 📌 Project Overview

This project is a Machine Learning-based Language Detection application that predicts the language of a given text. It uses Natural Language Processing (NLP) techniques to convert text into numerical features and a Multinomial Naive Bayes classifier to identify the language.

The trained model is integrated into a Streamlit web application, allowing users to enter text and receive a predicted language.

## 🎯 Objectives

- Build a language detection model using Machine Learning.
- Apply text vectorization using CountVectorizer.
- Train a Multinomial Naive Bayes classifier.
- Evaluate model performance using accuracy.
- Deploy the trained model through a user-friendly Streamlit application.

## ✨ Features

- Detects the language of user-provided text.
- Uses NLP-based text vectorization.
- Predicts language using a trained ML model.
- Simple and interactive Streamlit interface.
- Saves the trained model and vectorizer for reuse.
- Reports **95% accuracy** on the model's evaluation dataset.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- CountVectorizer
- Multinomial Naive Bayes
- Streamlit
- Pickle

## ⚙️ Machine Learning Workflow

1. Load and explore the language dataset.
2. Separate the text features and language labels.
3. Split the dataset into training and testing sets.
4. Convert text into numerical features using CountVectorizer.
5. Train a Multinomial Naive Bayes classifier.
6. Evaluate the model on held-out test data.
7. Save the trained model and vectorizer as pickle files.
8. Build a Streamlit application for language prediction.

## 📊 Model Performance

- **Model:** Multinomial Naive Bayes
- **Feature Extraction:** CountVectorizer
- **Reported Accuracy:** 95%

Accuracy represents the proportion of correctly predicted language labels in the evaluation dataset. Actual performance may vary for unseen text, short inputs, and languages or writing styles that are underrepresented in the dataset.

## 📁 Project Structure

```text
language-detection/
└── data/
    ├── dataset.csv
└── notebooks/
   ├── app.py
   ├── model.pkl
   ├── vectorizer.pkl
   ├── requirements.txt
   └── LanguageDetection.ipynb
├── README.md
```

## 🚀 Live Demo

**Try the application here:** [Language Detection App](https://language-detection-17.streamlit.app/)

Explore the deployed application by entering text and seeing the predicted language.


## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd language-detection
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal.

## ☁️ Deployment

This application can be deployed using Streamlit Community Cloud.

1. Push the project files to a GitHub repository.
2. Open https://share.streamlit.io/
3. Connect your GitHub account.
4. Select the repository and `app.py`.
5. Deploy the application.

## 🔮 Future Improvements

- Support additional languages and larger datasets.
- Evaluate performance using a confusion matrix and classification report.
- Improve predictions for short or mixed-language text.
- Add confidence scores where appropriate.
- Enhance the user interface and error handling.

## 👩‍💻 Author

**Aarushi Mandloi**

Machine Learning | Natural Language Processing | Python

---

*This project demonstrates the application of classical Machine Learning and NLP techniques to a real-world text classification task.*