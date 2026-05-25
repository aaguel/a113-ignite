# classifier.py — Multi-label BookTok angle classifier
# Trained on hand-labeled Disney Publishing dataset
# Uses scikit-learn LogisticRegression with one classifier per label

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.multiclass import OneVsRestClassifier
from app.data import BOOKS, LABEL_NAMES, GENRES, TONES, AUDIENCES

# ── Feature engineering ───────────────────────────────────────────────────────
# We treat each book as a feature vector built from its metadata.
# No raw text — just structured signals we defined from the blurb.

def build_features(audience, genre, tone, is_franchise, is_series, has_romance):
    """
    Convert book metadata into a numeric feature vector.
    One-hot encodes categorical fields, keeps binary flags as-is.
    """
    # One-hot encode audience
    aud_vec = [1 if audience == a else 0 for a in AUDIENCES]

    # One-hot encode genre
    genre_vec = [1 if genre == g else 0 for g in GENRES]

    # One-hot encode tone
    tone_vec = [1 if tone == t else 0 for t in TONES]

    # Binary flags
    flags = [int(is_franchise), int(is_series), int(has_romance)]

    # Concatenate everything into one flat vector
    return aud_vec + genre_vec + tone_vec + flags


def build_training_data():
    """
    Build X (feature matrix) and Y (label matrix) from BOOKS.
    X shape: (n_books, n_features)
    Y shape: (n_books, n_labels)
    """
    X, Y = [], []
    for book in BOOKS:
        # Unpack — see data.py for column order
        (title, author, year, audience, genre, tone,
         is_franchise, is_series, has_romance,
         *labels) = book

        features = build_features(audience, genre, tone,
                                  is_franchise, is_series, has_romance)
        X.append(features)
        Y.append(labels)  # 12 binary labels

    return np.array(X), np.array(Y)


# ── Model ─────────────────────────────────────────────────────────────────────

class BookTokClassifier:
    """
    Multi-label classifier — predicts which BookTok angles apply to a book.
    Trains one logistic regression per label (OneVsRest strategy).
    With only 35 training examples, we use strong regularization (C=0.5)
    and class_weight='balanced' to handle label imbalance.
    """

    def __init__(self):
        self.model = OneVsRestClassifier(
            LogisticRegression(
                C=0.5,                  # regularization — keeps model from overfitting small dataset
                max_iter=1000,
                class_weight="balanced" # handles labels that appear less often
            )
        )
        self.trained = False

    def train(self):
        X, Y = build_training_data()
        self.model.fit(X, Y)
        self.trained = True
        print(f"[A113 Ignite] Classifier trained on {len(X)} books, {Y.shape[1]} labels")

    def predict(self, audience, genre, tone, is_franchise, is_series, has_romance, threshold=0.3):
        """
        Returns a dict of {label: probability} for labels above threshold.
        threshold=0.3 means we include a label if model is >30% confident.
        Lower threshold = more angles surfaced, which is better for marketing.
        """
        if not self.trained:
            self.train()

        features = build_features(audience, genre, tone,
                                  is_franchise, is_series, has_romance)
        X = np.array([features])

        # Get probability for each label
        probs = self.model.predict_proba(X)[0]

        results = {}
        for label, prob in zip(LABEL_NAMES, probs):
            if prob >= threshold:
                results[label] = round(float(prob), 3)

        # Sort by confidence descending
        return dict(sorted(results.items(), key=lambda x: -x[1]))


# Singleton — one trained classifier shared across all requests
classifier = BookTokClassifier()
classifier.train()